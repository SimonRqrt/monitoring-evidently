from fastapi import FastAPI
import pandas as pd
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from config import load_model, prediction
from predict import FeaturesInput, PredictionOutput

app = FastAPI()

model = load_model()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Instrumentator().instrument(app).expose(app)


@app.get("/")
async def home():
    return {"hello": "Bienvenue sur l'API de prédiction Diabetes"}


@app.post("/predict")
async def predict(feature_input: FeaturesInput):
    """
    Réalise une prédiction avec le modèle pour classifier un chiffre
    """
    # Conversion des données d'entrée en tableau numpy
    feature_input = {
        "Pregnancies": feature_input.pregnancies,
        "Glucose": feature_input.glucose,
        "BloodPressure": feature_input.blood_pressure,
        "SkinThickness": feature_input.skin_thickness,
        "Insulin": feature_input.insulin,
        "BMI": feature_input.bmi,
        "DiabetesPedigreeFunction": feature_input.diabetes_pedigree,
        "Age": feature_input.age
    }
    feature_df = pd.Dataframe([feature_input])
    feature_df = feature_df.astype(float)
    
    pred = prediction(model, feature_df)
    # Retourne la prédiction (0: non diabétique, 1: diabétique)
    return PredictionOutput(prediction=int(pred[0]))