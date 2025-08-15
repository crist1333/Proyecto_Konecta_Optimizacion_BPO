# 📞 Optimización de Procesos en Contact Center – Simulación BPO (Konecta)

## 📌 Descripción
Este proyecto simula la optimización de un proceso de atención al cliente en un **BPO / Contact Center**, aplicando:
- **Automatización robótica de procesos (RPA)**
- **Web scraping con Selenium**
- **Mini chatbot** para atención al cliente
- **Documentación visual** (Blueprints, Flujos, Wireframes)

Diseñado para mostrar habilidades alineadas con los **requerimientos de la vacante en Konecta**, incluyendo análisis de procesos, diseño centrado en el usuario y uso de tecnología para mejorar eficiencia y experiencia.

---

## 🎯 Objetivos
- Optimizar la atención al cliente reduciendo tiempos manuales.
- Centralizar información en Excel para integración con otros sistemas.
- Demostrar competencias en **transformación digital** y **automatización en BPO**.
- Aplicar **Design Thinking**, **Customer Journey Maps** y **Service Blueprints**.

---

## 🧭 Fases del Proyecto
1. **Mapeo del proceso actual**
   - Diagramas del flujo real del servicio.
   - Identificación de cuellos de botella.
2. **Investigación del usuario**
   - Creación de arquetipos.
   - Customer Journey Maps.
3. **Detección de mejoras**
   - Priorización de oportunidades.
4. **Desarrollo técnico**
   - Bots RPA y Selenium.
   - Chatbot para consultas.
5. **Prototipado visual**
   - Wireframes y Blueprints.
6. **Presentación**
   - Métricas y visualizaciones.

---

## 🔄 Flujo de Interacción (Ejemplo)

**Caso 1 – María consulta estado de caso**

[Cliente llama al Contact Center] (🟨 Cliente)
↓
[Agente revisa CRM] (🟦 Agente)
↓
[Bot RPA consulta base de datos] (🟪 Bot)
↓
[Agente confirma estado] (🟦 Agente)
↓
[Bot envía correo de confirmación] (🟪 Bot)


**Wireframe – Chatbot Caso María**

┌────────────────────────────┐
│ Chatbot Konecta │
├────────────────────────────┤
│ Hola, María, ¿quieres │
│ consultar el estado de tu │
│ caso? (Sí / No) │
├────────────────────────────┤
│ Bot: Caso #45678, en │
│ revisión por área financiera│
│ Tiempo estimado: 24h │
├────────────────────────────┤
│ [Botón: Consultar otro caso]│
└────────────────────────────┘


---

## 🤖 Bots Incluidos
- **Bot RPA** (`bot_seguimiento.py`): Automatiza seguimiento y actualiza Excel.
- **Bot Selenium** (`bot_selenium.py`, `bot_selenium_casos.py`): Extrae datos desde HTML simulado.
- **Chatbot** (`chatbot.py`): Responde a clientes con datos actualizados.

---

## 📂 Estructura del Proyecto

Proyecto_Konecta_Optimizacion_BPO/
│
├── bot_rpa/ # Automatización RPA
│ └── bot_seguimiento.py
├── bot_scraper/ # Web scraping Selenium
│ ├── bot_selenium.py
│ ├── bot_selenium_casos.py
├── chatbot/ # Chatbot
│ └── chatbot.py
├── data/ # Archivos Excel y HTML
├── docs/img/ # Diagramas y capturas
├── README.md
├── requirements.txt
└── .gitignore



---

## 📊 Herramientas utilizadas
- **Python 3.12**
- **Pandas / OpenPyXL**
- **Selenium**
- **Miro / Draw.io / Figma**
- **Google Slides / PowerPoint**

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

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar un bot (ejemplo RPA)
cd bot_rpa
python bot_seguimiento.py

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

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar un bot (ejemplo RPA)
cd bot_rpa
python bot_seguimiento.py


