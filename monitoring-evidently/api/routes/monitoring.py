from fastapi import APIRouter, HTTPException
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset
import pandas as pd
from api.config import settings
from datetime import datetime
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST, Gauge
from fastapi.responses import Response

# Métriques Prometheus
PREDICTION_COUNT = Counter('titanic_predictions_total', 'Nombre total de prédictions')
PREDIpCTION_LATENCY = Histogram('titanic_prediction_latency_seconds', 'Temps de prédiction')
DRIFT_SCORE = Gauge('titanic_drift_score', 'Score de data drift')

router = APIRouter()

@router.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@router.get("/monitoring/data-drift")
async def check_data_drift():
    try:
        # Charger les données de référence
        reference_data = pd.read_csv(settings.REFERENCE_DATA_PATH)
        
        # Charger les données récentes
        current_data = pd.read_csv("data/test.csv")  
        
        # Créer le rapport de drift
        data_drift_report = Report(metrics=[
            DataDriftPreset(),
            TargetDriftPreset()
        ])
        
        data_drift_report.run(reference_data=reference_data, current_data=current_data)
        
        # Calculer le score de drift (exemple simplifié)
        drift_score = len(data_drift_report.metrics_results[0].drifted_features) / len(reference_data.columns)
        DRIFT_SCORE.set(drift_score)
        
        # Sauvegarder le rapport
        report_path = f"{settings.EVIDENTLY_REPORT_PATH}/drift_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        data_drift_report.save_json(report_path)
        
        return {
            "message": "Rapport de drift généré avec succès",
            "report_path": report_path,
            "drift_score": drift_score
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))