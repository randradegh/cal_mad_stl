##
# Utilerias del proyecto de calificaciones de la MAD.
##

# Incluímos las bibliotecas necesarias
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import pydeck as pdk
from PIL import Image
#from scipy import stats
import numpy as np 

# Debe ser el primer comando
st.set_page_config(
     page_title="Análisis de Calificaciones. MAD/FQ/UNAM",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="auto"
 )

#
# Funciones
#

#
# Lectura del dataset
#

def read_data():
    return pd.read_csv("data/cal_mad_01.csv", sep=',')

#
# Limpieza de datos
#

def clean_data(df_base):
    # Eliminamos a los desertores
    df_base.drop(df_base[df_base['Avance'] == 'Desertó'].index, inplace=True)

    # Eliminamos las columnas no necesarias para el análisis de calificaciones
    # df_base contendrá solamente las calificaciones y las generaciones
    df_base=df_base.drop(['No.', 'Nombre', 'Avance', 'Graduado', 'SIMAD', 'ADA', 'Fecha de Nacimiento', 'Carrera', 'Escuela', 'IES', 'Otro grado', 'Escuela otro', 'IES otro', 'Edad al ingresar'], axis=1)
    
    # Convertimos 'NI' y 'NP' a nulos.
    for column in df_base:
        df_base[column] = df_base[column].replace('NI',np.nan)
        df_base[column] = df_base[column].replace('NP',np.nan)
        df_base[column] = df_base[column].astype("float64")
    
    return df_base

