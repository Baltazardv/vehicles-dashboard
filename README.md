# 🚗 Dashboard de Análisis de Vehículos Usados

## Descripción del Proyecto
Esta aplicación web interactiva permite explorar y visualizar datos de vehículos usados mediante gráficos interactivos. Desarrollada con Streamlit y Plotly Express, proporciona una interfaz intuitiva para analizar tendencias en el mercado de automóviles usados.

## Funcionalidades
- **Histogramas interactivos**: Visualiza la distribución del odómetro de los vehículos
- **Gráficos de dispersión**: Explora la relación entre precio y kilometraje
- **Filtros por condición**: Analiza datos segmentados por estado del vehículo
- **Vista de datos en bruto**: Examina los datos originales

## Tecnologías Utilizadas
- **Python**: Lenguaje de programación principal
- **Streamlit**: Framework para aplicaciones web
- **Plotly Express**: Biblioteca de visualización interactiva
- **Pandas**: Manipulación y análisis de datos
- **Render**: Plataforma de despliegue

## Estructura del Proyecto
.
├── README.md
├── app.py                 # Aplicación principal
├── vehicles_us.csv        # Dataset de vehículos
├── requirements.txt       # Dependencias
└── notebooks/
└── EDA.ipynb         # Análisis exploratorio

## Cómo Ejecutar Localmente
1. Clonar el repositorio
2. Crear entorno virtual: `python -m venv vehicles_env`
3. Activar entorno: `vehicles_env\Scripts\activate` (Windows) o `source vehicles_env/bin/activate` (Mac/Linux)
4. Instalar dependencias: `pip install -r requirements.txt`
5. Ejecutar aplicación: `streamlit run app.py`

## Enlace a la Aplicación
[[Ver aplicación desplegada][(https://vehicles-dashboard-gfhj.onrender.com/)]
## Autor
Baltazar Dimayuga 
