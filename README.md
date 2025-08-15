# Optimización de Procesos en Contact Center – Simulación BPO para Konecta

## 📌 Descripción
Proyecto diseñado para simular la optimización de un proceso de atención al cliente en un BPO, aplicando análisis de procesos, métricas y tecnología.

Incluye:
- **Bots de automatización** (RPA y Selenium).
- **Mini chatbot** de atención al cliente.
- Documentación visual (Blueprints, Flujos de Interacción, Wireframes).

---

## 🎯 Objetivo
Aplicar herramientas y metodologías para mejorar la experiencia del cliente y la eficiencia operativa, alineado con los objetivos de Konecta.

---

## 🧭 Fases del Proyecto
1. **Mapeo del proceso actual** – Diagramas y análisis de cuellos de botella.
2. **Investigación de usuario** – Arquetipos y Customer Journey Maps.
3. **Propuesta de mejora** – Diseño con Design Thinking.
4. **Desarrollo técnico** – Bots y prototipos digitales.
5. **Prototipado visual** – Wireframes y Service Blueprints
6. **Presentación final** – Documentación y métricas.

## flujo de interacción

## Estructura básica:

Cada paso es un rectángulo o elipse.

Las flechas indican el orden del proceso.

Colores diferentes para:

Cliente (amarillo)

Agente (azul)

Back office (verde)

Tecnología/Bot (morado)

1️⃣ Caso María – Consulta de estado del caso
[Cliente llama al Contact Center] → 
[Agente revisa datos en CRM] → 
[Bot RPA consulta base de datos] → 
[Agente confirma estado del caso] → 
[Bot envía correo de confirmación]


Tips de diseño:

Rectángulos amarillos para el cliente.

Rectángulos azules para el agente.

Rectángulo morado para el bot.

Flechas horizontales o verticales.

2️⃣ Caso Luis – Queja por tiempos de esp
Wireframes – Bocetos de la interfaz


## Los wireframes son simples (blanco y negro o colores neutros) que muestran la estructura de una pantalla, no su diseño final.

Caso María – Consulta de estado de caso (Bot Web o WhatsApp)
┌────────────────────────────┐
│ Chatbot Konecta             │
├────────────────────────────┤
│ Hola, María, ¿quieres       │
│ consultar el estado de tu   │
│ caso? (Sí / No)              │
├────────────────────────────┤
│ Bot: Caso #45678, en        │
│ revisión por área financiera│
│ Tiempo estimado: 24h        │
├────────────────────────────┤
│ [Botón: Consultar otro caso]│
└────────────────────────────┘
---

## 🤖 Bots Incluidos
- **RPA Bot** (`bot_seguimiento.py`): automatiza seguimiento a clientes.
- **Selenium Bot** (`bot_selenium.py`): extrae datos de páginas web.
- **Chatbot** (`chatbot.py`): atiende consultas frecuentes.
- # 🛠 Proyecto de Automatización RPA + Web Scraping para Contact Center

Este proyecto simula la automatización de la gestión de casos en un **BPO / Contact Center**, alineado con las responsabilidades de la vacante en Konecta.

Combina:
- **Bot Selenium** para extraer datos de casos de clientes desde una fuente HTML simulada.
- **Bot RPA en Python** para enviar notificaciones automáticas y actualizar el seguimiento de clientes en Excel.

---

## 📌 Objetivos
- Optimizar procesos de atención al cliente.
- Reducir tiempos manuales de consulta y respuesta.
- Centralizar información en un archivo Excel que puede ser usado por otros sistemas.
- Demostrar habilidades en **automatización robótica de procesos (RPA)** y **procesos BPO**.

---

## 📂 Estructura del proyecto


---

## 📊 Herramientas utilizadas
- Python 3.12
- Pandas / OpenPyXL
- Selenium
- Miro / Draw.io / Figma
- Google Slides / PowerPoint

---

## 📸 Ejemplos visuales
![Blueprint María](docs/img/blueprint_maria.png)
![Flujo María](docs/img/flujo_interaccion_maria.png)
![Bot RPA Output](docs/img/bot_rpa_output.png)
![Wireframe Prototipo](docs/img/wireframe_prototipo.png)

---

## 🚀 Instalación
```bash
# Clonar el repositorio
git clone https://github.com/tu_usuario/Proyecto_Konecta_Optimizacion_BPO.git
cd Proyecto_Konecta_Optimizacion_BPO

# Instalar dependencias de un bot (ejemplo RPA)
cd bot_rpa
pip install -r requirements.txt
