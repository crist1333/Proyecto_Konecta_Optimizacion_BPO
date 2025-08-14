import pandas as pd
from datetime import datetime

# Cargar datos de clientes
df = pd.read_excel("seguimiento_clientes.xlsx")

# Simulación de envío de mensajes
for index, row in df.iterrows():
    nombre = row["Nombre"]
    contacto = row["Contacto"]
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

# Actualizar archivo con fecha de seguimiento
df["Última actualización"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
df.to_excel("seguimiento_clientes_actualizado.xlsx", index=False)
print("✅ Archivo actualizado guardado como 'seguimiento_clientes_actualizado.xlsx'")
