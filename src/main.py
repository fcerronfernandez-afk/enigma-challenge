# PATHS ORIGINALES DE DATOS
loans_path = 'data/loans.csv'
branches_path = 'data/branches.csv'

# PATH LIMPIO
loans_clean_path = 'data/loans_clean.csv'

import pandas as pd
import sqlite3
import os

# --- 1. PROCESO DE LIMPIEZA DE DATOS ---

print("Iniciando proceso de carga y limpieza de datos...")

if not os.path.exists('data'):
    print("Error: El directorio 'data' no existe. Asegúrate de tener 'data/loans.csv' y 'data/branches.csv'.")
    exit()

try:
    loans = pd.read_csv(loans_path)
    branches = pd.read_csv(branches_path)
    print("Archivos de datos cargados exitosamente.")
except FileNotFoundError as e:
    print(f"Error de carga de archivo: {e}. Asegúrate de que los archivos estén en la ruta correcta.")
    exit()


loans['issue_date'] = pd.to_datetime(loans['issue_date'], errors='coerce')

loans['total_payable'] = loans['amount'] + (loans['amount'] * loans['interest_rate'])

loans_clean = loans[loans['amount'] > 0].copy()

os.makedirs("data", exist_ok=True)
loans_clean.to_csv(loans_clean_path, index=False)
print(f"Datos limpios guardados en '{loans_clean_path}'.")

print("\nPrimeros 5 registros del DataFrame limpio (loans_clean):")
print(loans_clean.head())


# --- 2. CONSULTAS SQL ---

print("\nEjecutando consultas SQL...")

loans_clean = pd.read_csv(loans_clean_path)
branches = pd.read_csv(branches_path)

conn = sqlite3.connect(':memory:')
loans_clean.to_sql('loans_clean', conn, index=False, if_exists='replace')
branches.to_sql('branches', conn, index=False, if_exists='replace')

sql_code = """
SELECT
  b.zone,
  SUM(l.amount) AS total_amount
FROM loans_clean l
JOIN branches b ON l.branch_id = b.branch_id
GROUP BY b.zone
ORDER BY total_amount DESC;
"""
result = pd.read_sql_query(sql_code, conn)

print("\nResultados de la consulta SQL por zona (total_amount):")
print(result)
