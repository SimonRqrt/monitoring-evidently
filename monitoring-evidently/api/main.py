from fastapi import FastAPI
from api.routes import predict, monitoring
from api.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Inclusion des routers
app.include_router(predict.router, prefix=settings.API_V1_STR)
app.include_router(monitoring.router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de prédiction Titanic"}