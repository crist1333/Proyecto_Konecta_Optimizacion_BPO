# bot_selenium_casos.py
# Autor: Cristian Aranzazu - Proyecto Konecta RPA
# Descripción: Extrae datos simulados de casos de clientes y los guarda en seguimiento_clientes.xlsx

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os
from datetime import datetime

# ==============================
# 1. Configuración del navegador
# ==============================
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Para que no abra ventana
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

# ==============================
# 2. URL de datos simulados
# ==============================
# Puedes usar un HTML local o una URL de prueba
# Ejemplo: archivo local 'casos_clientes.html' en la misma carpeta
url = "file:///C:/Users/crist/PycharmProjects/Proyecto_Konecta_Optimizacion_BPO/bot_scraper/casos_clientes.html"
driver.get(url)
time.sleep(2)

# ==============================
# 3. Extracción de datos
# ==============================
clientes = []
casos = []
estados = []
fechas = []

rows = driver.find_elements(By.CSS_SELECTOR, "table tr")

for row in rows[1:]:  # Saltar encabezado
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) == 4:
        clientes.append(cols[0].text)
        casos.append(cols[1].text)
        estados.append(cols[2].text)
        fechas.append(cols[3].text)

driver.quit()

# ==============================
# 4. Guardar en Excel para el bot RPA
# ==============================
df = pd.DataFrame({
    "Nombre": clientes,
    "Número de caso": casos,
    "Estado": estados,
    "Tiempo estimado": fechas
})

# Asegurar que la carpeta exista
output_dir = os.path.join(os.getcwd(), "bot_rpa")
os.makedirs(output_dir, exist_ok=True)

# Crear nombre de archivo con timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
excel_filename = f"seguimiento_clientes_{timestamp}.xlsx"
excel_path = os.path.join(output_dir, excel_filename)

# Guardar el DataFrame
df.to_excel(excel_path, index=False)

# Guardar directamente en la carpeta bot_rpa
excel_path = "bot_rpa/seguimiento_clientes.xlsx"
df.to_excel(excel_path, index=False)

print(f"✅ Datos extraídos y guardados en {excel_path}")
