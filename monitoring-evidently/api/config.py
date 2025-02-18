from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Titanic Survival Prediction API"
    
    # Model Configuration
    MODEL_PATH: str = "api/models/model.pkl"
    REFERENCE_DATA_PATH: str = "data/titanic_clean.csv"
    
    # Monitoring Configuration
    MONITORING_ENABLED: bool = True
    EVIDENTLY_REPORT_PATH: str = "monitoring/reports"
    
    class Config:
        case_sensitive = True

settings = Settings()