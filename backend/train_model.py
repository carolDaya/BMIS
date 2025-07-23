import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Leer los datos sintéticos
df = pd.read_csv('datos_biodigestor.csv')

# Dividir variables
X = df[['temperatura', 'presion', 'mq4_gas']].values
y = df['label'].values

# Crear y entrenar el árbol
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Guardar el modelo entrenado
joblib.dump(model, 'biodigestor_model.pkl')

print("Modelo entrenado y guardado como 'biodigestor_model.pkl'")
