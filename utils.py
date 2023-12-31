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
import numpy as np 



#
# Funciones
#
def encabezado():
    t1, t2 = st.columns((1,3), gap="medium") 
    t1.image('images/UNAM-universidad-1.png', width = 100)
    #t2.header(":gray[Proyecto Datos]")
    t2.write("# Proyecto Datos")
    t2.write(" ## :green[Maestría en Alta Dirección] - :blue[FQ / UNAM]")
    #t3.image('images/data_analysis.jpeg', width = 160)

#
# Lectura del dataset
#

def read_data():
    #return pd.read_csv("data/cal_mad_01.csv", sep=',')

    df = pd.read_csv("data/cal_mad_sexo_ready.csv", sep=',')
    sex_dict = {'male':'hombre', 'female':'mujer'}
    df = df.replace({'sexo': sex_dict})

    return df

#
# Limpieza de datos
#

def edad_mean(df_base):
    edad_promedio=df_base['Edad al ingresar'].mean().round(1)
    return edad_promedio



def clean_data(df_base):
    # Eliminamos a los desertores
    df_base.drop(df_base[df_base['Avance'] == 'Desertó'].index, inplace=True)

    # Eliminamos las columnas no necesarias para el análisis de calificaciones
    # df_base contendrá solamente las calificaciones y las generaciones
    df_base=df_base.drop(['No.', 'Nombre', 'Avance', 'Graduado', 'SIMAD', 'ADA', 'Fecha de Nacimiento', 'Carrera', 'Escuela', 'IES', 'Otro grado', 'Escuela otro', 'IES otro', 'Edad al ingresar','sexo'], axis=1)
    
    # Convertimos 'NI' y 'NP' a nulos.
    for column in df_base:
        df_base[column] = df_base[column].replace('NI',np.nan)
        df_base[column] = df_base[column].replace('NP',np.nan)
        df_base[column] = df_base[column].astype("float64")
    
    return df_base

# import gender_guesser.detector as gender
# d=gender.Detector()
# >>> print(d.get_gender('Álvarez Pérez David'.split().[-1]))
#   File "<stdin>", line 1
#     print(d.get_gender('Álvarez Pérez David'.split().[-1]))
#                                                      ^
# SyntaxError: invalid syntax
# >>> print(d.get_gender('Álvarez Pérez David'.split()[-1]))
# male
# >>> print(d.get_gender('Alonso Galeana Marco Antonio'.split()[-1]))
# male
# >>> print(d.get_gender('Campa Arvizu Carlos Félix'.split()[-1]))
# male
# >>> print(d.get_gender('Guadarrama Lara Melissa'.split()[-1]))
# female
# >>> print(d.get_gender('Duarte Michel Lilia Angélica'.split()[-1]))
# female


