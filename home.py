import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="NovusSolutions", page_icon="⛅")

st.title('Novus Solutions - Inmarepro')
st.header("Centrales de Monitoreo en Tiempo Real con Alarmas y Recomendaciones")

st.write("Ahorros 💰 en costos operativos mediante sistemas de análisis predictivos:")

st.markdown(
  """
  En esta web encontrarás tecnologías de Matrices de Riesgos Industriales para:
  - 🔎 _    Gas Natural y Productos Pretrolíferos
  - 🛒 _    Calefacción Industrial y Energía Solar Térmica
  - ✍️ _     Auditorías y Servicios Energéticos
  - 🔎 _    Mantenimientos Industriales
  - 🛒 _    Sistemas Contraincendios
  - ✍️ _     Climatización
  - 🔎 _    Instalaciones Industriales
  - 🛒 _    Áire Comprimido
  
  EMPIEZA TU 🔎 DIAGNÓSTICO AHORA 🕰
  """
)

st.write("Análisis Espacial de Datos")

#datos

df = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

#mapa
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=df,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))
