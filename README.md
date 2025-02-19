# Monitoring d'une API de Prédiction avec Evidently AI, Prometheus et Grafana

## Description
Ce projet met en place un système complet de monitoring pour une API de prédiction basée sur un modèle de Machine Learning. Le modèle est entraîné sur le dataset **Titanic** de `sklearn`. L'objectif est de surveiller les performances du modèle, les dérives de données et la santé de l'API en production.

## Prérequis
Avant de commencer, assurez-vous d'avoir installé :
- **Docker**
- **Docker Compose**

## Installation

Clonez le dépôt :
```bash
git clone <URL_DU_DEPOT>
cd monitoring
```

Construisez et démarrez les services Docker :
```bash
docker-compose up --build
```

## Utilisation
### API
L'API est développée avec **FastAPI** et permet de faire des prédictions avec le modèle Titanic.

- Accédez à la documentation interactive Swagger :
  ```
  http://localhost:8000/docs
  ```
- Endpoint principal :
  ```
  POST /predict
  ```
  Ce point d'entrée permet d'envoyer des données et de recevoir des prédictions en retour.

### Monitoring avec Evidently AI
Les rapports de surveillance des dérives et des performances du modèle sont générés par Evidently AI.

- Exécutez le notebook **monitoring.ipynb** pour analyser les dérives de données et les performances du modèle.
- Le rapport de dérive est enregistré en HTML et accessible dans le notebook.

### Monitoring de l'Infrastructure avec Grafana & Prometheus

**Grafana** est configuré pour visualiser les performances de l'API et l'utilisation des ressources serveur.
- Accédez à Grafana via :
  ```
  http://localhost:3000
  ```
  (Utilisateur par défaut : `admin` / Mot de passe : `password@123`)

**Prometheus** collecte les métriques de l'API et du serveur.
- Accédez à Prometheus via :
  ```
  http://localhost:9090
  ```

## Architecture des services
Le projet est orchestré avec **Docker Compose** et contient les services suivants :
- `api` : FastAPI pour les prédictions.
- `prometheus` : Collecte et stocke les métriques de l'API.
- `grafana` : Visualisation des métriques.
- `node-exporter` : Surveillance des ressources serveur.

## Configuration
Les fichiers de configuration clés sont :
- `docker-compose.yml` : Orchestration des services.
- `monitoring/prometheus/prometheus.yml` : Configuration de Prometheus.
- `monitoring/grafana/provisioning` : Configuration des dashboards Grafana.

## Dépendances
Les bibliothèques Python nécessaires sont listées dans `requirements.txt`.
Installez-les localement si nécessaire avec :
```bash
pip install -r requirements.txt
```

## Contributeurs
N'hésitez pas à contribuer en proposant des pull requests ou en signalant des problèmes !


