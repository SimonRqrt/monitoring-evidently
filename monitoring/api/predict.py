from pydantic import BaseModel


class FeaturesInput(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigree: float
    Age: float


class PredictionOutput(BaseModel):
    prediction: float