import numpy as np
import pandas as pd

np.random.seed(42)

# --- 70 normales ---
normal_temp = np.random.uniform(30, 37, 70)
normal_pres = np.random.uniform(0.8, 1.4, 70)
normal_gas  = np.random.uniform(50, 180, 70)

# --- 30 alerta clara ---
alerta_temp = np.concatenate([
    np.random.uniform(5, 15, 15),   # Muy baja
    np.random.uniform(40, 50, 15)   # Muy alta
])
alerta_pres = np.concatenate([
    np.random.uniform(0.3, 0.7, 15), # Muy baja
    np.random.uniform(1.6, 2.2, 15)  # Muy alta
])
alerta_gas = np.random.uniform(220, 500, 30)

# --- 10 mixtos (1 mal, otros bien) ---
mixto_temp = np.random.uniform(30, 37, 10)  # Temperatura bien
mixto_pres = np.random.uniform(0.3, 0.7, 10)  # Presión baja
mixto_gas  = np.random.uniform(50, 180, 10)  # Gas normal

# --- Etiquetas ---
normal_labels = np.zeros(70)  # 0 = normal
alerta_labels = np.ones(30)   # 1 = alerta clara
mixto_labels  = np.ones(10)   # 1 = alerta, porque un parámetro está crítico

# --- Unir todo ---
temp = np.concatenate([normal_temp, alerta_temp, mixto_temp])
pres = np.concatenate([normal_pres, alerta_pres, mixto_pres])
gas  = np.concatenate([normal_gas, alerta_gas, mixto_gas])
labels = np.concatenate([normal_labels, alerta_labels, mixto_labels])

# --- Mezclar ---
indices = np.arange(len(labels))
np.random.shuffle(indices)

df = pd.DataFrame({
    'temperatura': temp[indices],
    'presion': pres[indices],
    'mq4_gas': gas[indices],
    'label': labels[indices]
})

df.to_csv('datos_biodigestor.csv', index=False)
print("Archivo 'datos_biodigestor.csv' generado con 110 datos.")
