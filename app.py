import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Dashboard de Vehículos", page_icon="🚗", layout="wide")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv('vehicles_us.csv')

car_data = load_data()

# Título principal
st.header('🚗 Dashboard de Análisis de Vehículos Usados')

st.write("""
Esta aplicación permite explorar datos de vehículos usados a través de visualizaciones interactivas.
Utiliza los botones o casillas de verificación para generar los gráficos.
""")

# Mostrar información básica del dataset
st.subheader('📊 Información del Dataset')
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total de Vehículos", len(car_data))
with col2:
    st.metric("Precio Promedio", f"${car_data['price'].mean():,.0f}")
with col3:
    st.metric("Años Disponibles", f"{car_data['model_year'].min():.0f} - {car_data['model_year'].max():.0f}")

# Opción 1: Usando botones
st.subheader('📈 Visualizaciones con Botones')

col1, col2 = st.columns(2)

with col1:
    hist_button = st.button('Construir Histograma del Odómetro')
    if hist_button:
        st.write('**Histograma del Odómetro**')
        fig = px.histogram(car_data, 
                          x="odometer", 
                          title="Distribución del Odómetro",
                          labels={'odometer': 'Odómetro (millas)', 'count': 'Frecuencia'})
        st.plotly_chart(fig, use_container_width=True)

with col2:
    scatter_button = st.button('Construir Gráfico de Dispersión')
    if scatter_button:
        st.write('**Precio vs Odómetro**')
        fig = px.scatter(car_data, 
                        x="odometer", 
                        y="price",
                        title="Relación entre Precio y Odómetro",
                        labels={'odometer': 'Odómetro (millas)', 'price': 'Precio ($)'})
        st.plotly_chart(fig, use_container_width=True)

# Opción 2: Usando checkboxes (más interactivo)
st.subheader('✅ Visualizaciones con Casillas de Verificación')

build_histogram = st.checkbox('Mostrar Histograma del Odómetro')
build_scatter = st.checkbox('Mostrar Gráfico de Dispersión Precio vs Odómetro')

if build_histogram:
    st.write('**Distribución del Odómetro**')
    fig = px.histogram(car_data, 
                      x="odometer",
                      nbins=50,
                      title="Distribución del Odómetro de Vehículos",
                      labels={'odometer': 'Odómetro (millas)', 'count': 'Número de Vehículos'})
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('**Relación entre Precio y Odómetro**')
    fig = px.scatter(car_data, 
                    x="odometer", 
                    y="price",
                    color="condition",
                    title="Precio vs Odómetro por Condición del Vehículo",
                    labels={'odometer': 'Odómetro (millas)', 'price': 'Precio ($)'})
    st.plotly_chart(fig, use_container_width=True)

# Información adicional
if st.checkbox('Mostrar datos en bruto'):
    st.subheader('🔍 Muestra de Datos')
    st.dataframe(car_data.head(100))