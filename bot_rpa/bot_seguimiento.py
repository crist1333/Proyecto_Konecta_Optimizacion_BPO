import os
import pandas as pd
from datetime import datetime

# Rutas absolutas en /data
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(project_root, "data", "seguimiento_clientes_raw.xlsx")
output_path = os.path.join(project_root, "data", "seguimiento_clientes_actualizado.xlsx")

# Cargar datos
df = pd.read_excel(input_path)

# Simulación de envío de mensajes
for index, row in df.iterrows():
    nombre = row["Nombre"]
    contacto = row.get("Contacto", "Sin contacto")
    caso = row["Número de caso"]
    estado = row["Estado"]

    mensaje = f"""
🔔 KONNECTA ATENCIÓN AL CLIENTE

Hola {nombre}, gracias por comunicarte con nosotros.

📝 Hemos registrado tu caso:
• Número de caso: #{caso}
• Estado: {estado}

📅 Tiempo estimado de respuesta: 24 horas

Si deseas consultar el estado en cualquier momento, responde con la palabra: ESTADO
"""
    print(f"📤 Mensaje enviado a: {contacto}\n{mensaje}")

# Actualizar archivo con timestamp
df["Última actualización"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
df.to_excel(output_path, index=False)

print(f"✅ Archivo actualizado guardado como '{output_path}'")
