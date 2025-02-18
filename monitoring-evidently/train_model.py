import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os
from sklearn import datasets

# Création des dossiers nécessaires
os.makedirs("api/models", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Charger le dataset Titanic depuis OpenML
print("Chargement des données...")
data = datasets.fetch_openml(name='titanic', version=1, as_frame=True)
df = data.frame

# Sélectionner les colonnes utiles
features = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']
target = 'survived'

# Nettoyage et encodage
print("Nettoyage des données...")
df = df[features + [target]].copy()
df['sex'] = df['sex'].map({'male': 0, 'female': 1})
df['embarked'] = df['embarked'].map({'C': 0, 'Q': 1, 'S': 2})

# Gestion des valeurs manquantes
df['age'] = df['age'].fillna(df['age'].median())
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])

# Séparation des données
X = df[features]
y = df[target].astype(int)

# Split des données
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Entraînement du modèle
print("Entraînement du modèle...")
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42
)
model.fit(X_train, y_train)

# Évaluation du modèle
print("\nÉvaluation du modèle:")
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Sauvegarde du modèle
print("\nSauvegarde du modèle...")
model_path = "api/models/model.pkl"
joblib.dump(model, model_path)
print(f"Modèle sauvegardé dans {model_path}")

# Sauvegarde des données nettoyées
print("Sauvegarde des données de référence...")
df.to_csv("data/titanic_clean.csv", index=False)
print("Données sauvegardées dans data/titanic_clean.csv")

# Sauvegarde des données de test pour le monitoring
print("Préparation des données pour le monitoring...")
test_df = pd.concat([X_test, y_test], axis=1)
test_df.to_csv("data/test.csv", index=False)
print("Données de test sauvegardées dans data/test.csv")

print("\nProcessus d'entraînement terminé avec succès!") 