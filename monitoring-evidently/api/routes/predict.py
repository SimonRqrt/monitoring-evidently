from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
from api.config import settings
import time
from .monitoring import PREDICTION_COUNT, PREDICTION_LATENCY

router = APIRouter()

class PredictionInput(BaseModel):
    pclass: int
    sex: int
    age: float
    sibsp: int
    parch: int
    fare: float
    embarked: int

class PredictionOutput(BaseModel):
    survival_probability: float
    survival_prediction: bool

@router.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    try:
        start_time = time.time()
        
        # Charger le modèle
        model = joblib.load(settings.MODEL_PATH)
        
        # Convertir l'entrée en DataFrame
        input_df = pd.DataFrame([input_data.dict()])
        
        # Faire la prédiction
        probability = model.predict_proba(input_df)[0][1]
        prediction = probability >= 0.5
        
        # Métriques de monitoring
        PREDICTION_COUNT.inc()
        PREDICTION_LATENCY.observe(time.time() - start_time)
        
        return PredictionOutput(
            survival_probability=float(probability),
            survival_prediction=bool(prediction)
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))