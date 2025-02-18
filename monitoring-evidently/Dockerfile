FROM python:3.9-slim

WORKDIR /app

# Copier les fichiers nécessaires
COPY ./api /app/api
COPY ./data /app/data

# Installer les dépendances
RUN pip install --no-cache-dir -r api/requirements.txt

# Exposer le port
EXPOSE 8000

# Commande de démarrage
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]