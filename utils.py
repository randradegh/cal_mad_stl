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

