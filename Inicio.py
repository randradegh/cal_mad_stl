# Incluímos las bibliotecas necesarias
from utils import *
from os import ST_WRITE

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 50px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #08088A;
    }
</style>
""", unsafe_allow_html=True)
st.image("images/head_01.png")
t1, t2 = st.columns((1,5), gap="medium") 
#t1.image('images/fq_logo_01.png', width = 50)
t1.image('images/UNAM-universidad-1.png', width = 100)
t2.write("# :green[Maestría en Alta Dirección] - :blue[FQ / UNAM]")
st.header("Proyecto Datos MAD")

#
# Lectura de datos
#
df = pd.read_csv("data/cal_mad_01.csv", sep=',')


#
# Intro
#

"""
El análisis de datos en las calificaciones de un programa de maestría en alta dirección puede proporcionar valiosas perspectivas e **insights** que 
ayuden a mejorar la calidad y efectividad del programa. Aquí hay algunas razones clave para realizar análisis de datos en este contexto:

1. Identificar fortalezas y áreas de mejora: Al analizar las calificaciones de los estudiantes en diferentes cursos y asignaturas, se pueden identificar patrones y 
tendencias. Esto permite a los responsables del programa identificar las áreas en las que los estudiantes están obteniendo buenos resultados y aprovechar esas fortalezas. 
Al mismo tiempo, también pueden identificar las áreas donde los estudiantes pueden enfrentar dificultades y tomar medidas para mejorar la enseñanza o el contenido del programa.

2. Personalización y mejora de la experiencia educativa: El análisis de datos puede ayudar a comprender las preferencias y necesidades individuales de los estudiantes. 
Al examinar las calificaciones y el desempeño de los estudiantes, se pueden identificar patrones que revelen cómo diferentes enfoques de enseñanza o modalidades 
de aprendizaje pueden influir en su rendimiento. Estos **insights** pueden usarse para personalizar la experiencia educativa, 
ofreciendo materiales de estudio adicionales, tutorías específicas o adaptando la metodología de enseñanza para maximizar el aprendizaje y la participación de los estudiantes.

Esta es la primera versión de un proyecto que tiene como objetivo ofrecer de manera sintética algunos datos y gráficos que permitan conocer mejor el desempeño general de
la *Maestría en Alta Dirección* de la Facultad de Química de la UNAM.
"""



"""
___
## Datos Originales

"""


with st.expander("Ver tabla de datos originales"):
    st.markdown("### Tabla con todos los datos recibidos para el análisis y visualización")
    """
    En esta tabla se muestran todas las columnas y todos los renglones del *dataset* extraído de la hoja de cálculo
    entregada para el presente proyecto. 

    Incluye a los dos semestres lectivos desde el 2016 y hasta el 2023-1.
    """
    df["Generación"] = df["Generación"].astype("category")
    st.write(df)

#
# Cantidad de desertores y graduados. Se obtienen del dataset sin limpiar
#

qty_desertores = len(df[df.Avance == 'Desertó'])
qty_graduados = len(df[df.Graduado == 'Si'])
qty_alumnos_registrados = len(df)

#
# Limpiamos datos
#
"""
___
### Limpieza de los datos
Es común que los datos de los cuales se parte no 
tengan la calidad adecuada para proceder a su análisis, así que deben 
realizarse algunas operaciones sobre ellos para mejorar su calidad.
Entre estas operaciones se encuentran:
- Homogeneizar el tipo de datos para cada columna específica.
- Convertir a valores nulos aquellos valores que no deban incluirse en las estadísticas.
- Corregir los valores mal capturados: falta de acentos, errores de captura, variedad de nombres.
- Conversión de tipos de datos.
- Otros.
"""

#
# Eliminación de los registros de los alumnos que desertaron
##
df.drop(df[df['Avance'] == 'Desertó'].index, inplace=True)

# Eliminamos las columnas no necesarias para el análisis de calificaciones
# df_cal contendrá solamente las calificaciones y las generaciones
df_cal=df.drop(['No.', 'Nombre', 'Avance', 'Graduado', 'SIMAD', 'ADA', 'Fecha de Nacimiento', 'Carrera', 'Escuela', 'IES', 'Otro grado', 'Escuela otro', 'IES otro', 'Edad al ingresar'], axis=1)
# st.write(df_cal)
for column in df_cal:
    df_cal[column] = df_cal[column].replace('NI',np.nan)
    df_cal[column] = df_cal[column].replace('NP',np.nan)
    df_cal[column] = df_cal[column].astype("float64")
#df = df.drop(df[df.score < 50].index)
st.write(df_cal)
st.markdown("#### Datos limpios")
"""
- Se reemplazaron los valores de 'NI' y 'NP' por valores nulos, de tal manera que 
no sean tomados en cuenta para los cálculos estadísticos necesarios para el análisis.
- Se eliminaron los registros de los alumnos que hayan desertado.

Solamente se muestran los datos cuantitativos.

##### **_Dataframe_** con los datos limpios
"""

df_num=df_cal.drop(['Generación'], axis=1)
st.write(df_num)

###
# Algunos valores básicos
###

"""
___
## Algunos datos generales
"""
# Cantidad de alumnos
cant_alumnos_total = len(df.index)

# Cantidad de generaciones
qty_gen = len(df.Generación.unique())

# Promedio general de calificaciones
cal_promedio_gral = df_cal.Promedio.mean().round(2)

# Porcentaje de desertores
porcien_desertores= (qty_desertores * 100) / qty_alumnos_registrados

#
# Indicadores
#
font_color_text = '#7FB3D5'
font_color_number = '#61210B'
BGCOLOR = "#2E64FE"
col01, col02, col03, col04, col05 = st.columns(5)
fig_ind = go.Figure()

with col01:
    ref = 5
    fig_ind.add_trace(go.Indicator(
        mode = "number",
        number = {'prefix': "",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
        value = qty_alumnos_registrados,
        title = {'text': 'Alumnos<br><b>Registrados</b>', 'font.size': 25, 'font.color':font_color_text},
        domain = {'row': 0, 'column': 0}))
    
with col02:
    ref = 5
    fig_ind.add_trace(go.Indicator(
        mode = "number",
        number = {'prefix': "",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
        value = cant_alumnos_total,
        title = {'text': 'Alumnos<br><b>Analizados</b>', 'font.size': 25, 'font.color':font_color_text},
        domain = {'row': 0, 'column': 1}))

with col03:
    ref = 5
    fig_ind.add_trace(go.Indicator(
        mode = "number",
        number = {'prefix': "",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
        value = qty_gen,
        title = {'text': '<b>Generaciones</b>', 'font.size': 25, 'font.color':font_color_text},
        domain = {'row': 0, 'column': 2}))
    
with col04:
    ref = 5
    fig_ind.add_trace(go.Indicator(
        mode = "number",
        number = {'prefix': "",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
        value = 12,
        title = {'text': '<b>Asignaturas</b>', 'font.size': 25, 'font.color':font_color_text},
        domain = {'row': 0, 'column': 3}))
    
    
fig_ind.update_layout(
    paper_bgcolor = BGCOLOR, 
    width=1200,
    height = 220,
    margin=dict(l=20, r=20, t=40, b=0),
    grid = {'rows': 1, 'columns': 4, 'pattern': "independent"},
)

fig_ind

font_color_text = 'white'
font_color_number = '#002b7a'
BGCOLOR = "#FAAC58"
col11, col12, col13, col14 = st.columns(4)
fig_ind2 = go.Figure()

with col11:
    ref = 6
    fig_ind2.add_trace(go.Indicator(
        mode = "number",
        number = {'prefix': "",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
        value = qty_graduados,
        title = {'text': '<b>Graduados</b>', 'font.size': 25, 'font.color':font_color_text},
        domain = {'row': 0, 'column': 0}))
    
with col12:
    ref = 6
    fig_ind2.add_trace(go.Indicator(
        mode = "number",
        number = {'prefix': "",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
        value = qty_desertores,
        title = {'text': '<b>Desertores</b>', 'font.size': 25, 'font.color':font_color_text},
        domain = {'row': 0, 'column': 1}))
    
with col13:
    ref = 5
    fig_ind2.add_trace(go.Indicator(
        mode = "number",
        number = {'prefix': "",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
        value = cal_promedio_gral,
        title = {'text': '<b>Promedio</b><br>General', 'font.size': 25, 'font.color':font_color_text},
        domain = {'row': 0, 'column': 2}))

with col14:
    ref = 5
    fig_ind2.add_trace(go.Indicator(
        mode = "number",
        number = {'suffix': "%",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
        value = porcien_desertores,
        title = {'text': '<b>Porcentaje de</b><br>Desertores', 'font.size': 25, 'font.color':font_color_text},
        domain = {'row': 0, 'column': 3}))


fig_ind2.update_layout(
    paper_bgcolor = BGCOLOR, 
    width=1200,
    height = 220,
    margin=dict(l=20, r=20, t=40, b=0),
    grid = {'rows': 1, 'columns': 4, 'pattern': "independent"},
)

fig_ind2

"""
___
### Función *describe()* de *Python*
"""

st.markdown("""
Haremos un somero análisis estadístico del *dataset* con la función _describe()_ de Python. 

La función _describe()_ se utiliza para calcular algunos datos estadísticos como percentiles, media y desviacion 
estándar de los valores numéricos de nuestros datos.
""")
desc = df_num.describe()
st.dataframe(desc)

"""
Más adelante revisaremos con detalle la distribución de calificaciones para cada asignatura.
"""
