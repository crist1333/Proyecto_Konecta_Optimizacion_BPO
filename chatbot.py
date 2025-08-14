def chatbot_respuesta(mensaje):
    mensaje = mensaje.lower()

    if "hola" in mensaje:
        return "¡Hola! Bienvenido al centro de atención Konecta. ¿En qué puedo ayudarte?"
    elif "estado" in mensaje:
        return "Claro, tu caso está en revisión y recibirás respuesta en un máximo de 24 horas."
    elif "gracias" in mensaje:
        return "Con gusto 😊. Estamos aquí para ayudarte."
    else:
        return "No entendí tu solicitud. Por favor escribe 'estado' para consultar tu caso."

# Simulación de chat
print("💬 Chatbot Konecta (escribe 'salir' para terminar)")
while True:
    user_input = input("Tú: ")
    if user_input.lower() == "salir":
        print("👋 Gracias por usar el servicio de atención Konecta.")
        break
    print("Bot:", chatbot_respuesta(user_input))
