from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Configuración del navegador (Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Página de ejemplo
url = "https://quotes.toscrape.com/"
driver.get(url)
time.sleep(2)

quotes_data = []
quotes = driver.find_elements(By.CLASS_NAME, "quote")

for quote in quotes:
    text = quote.find_element(By.CLASS_NAME, "text").text
    author = quote.find_element(By.CLASS_NAME, "author").text
    quotes_data.append({"Texto": text, "Autor": author})

driver.quit()

# Guardar datos
df = pd.DataFrame(quotes_data)
df.to_excel("resultados_selenium.xlsx", index=False)
print("✅ Datos guardados en 'resultados_selenium.xlsx'")
