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
#st.write(df_cal)
st.markdown("#### Datos limpios")
"""
- Se reemplazaron los valores de 'NI' y 'NP' por valores nulos, de tal manera que 
no sean tomados en cuenta para los cálculos estadísticos necesarios para el análisis.
- Se eliminaron los registros de los alumnos que hayan desertado.

Solamente se muestran los datos cuantitativos.

##### **_Dataframe_** con los datos limpios
"""

df_num=df_cal.drop(['Generación'], axis=1)
#st.write(df_num)

"""
___
## Indicadores de Desempeño

### Promedios Totales por Asignatura
### 

Cada recuadro muestra el promedio de calificaciones para todos los alumnos de todas las generaciones. 

**Para el cálculo no se incluyeron los alumnos que han desertado.**
###
"""

#
# Extraemos los nombre de las asignaturas en una lista
#
asigs = df.columns[5:17].tolist()

#
# Primer bloque
#
cols = st.columns(6, gap='medium')
ncol = 0
for x in asigs[0:6]:
    ncol = ncol + 1
    #
    # Calculamos los promedios de cada asignatura
    #
    media = pd.to_numeric(df_cal[x]).mean().round(2)
    
    with cols[ncol-1]:
        #st.write(f"#### {x}")
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=media,
            gauge=dict(
                axis=dict(range=[None, 10]),
                bar=dict(color="green"),
                steps=[
                    dict(range=[0, 10], color="lightgray")
                ],
            ),
            #domain={"x": [0, 1], "y": [0, 1]},
            domain={'row': 0, 'column':  0},
            title={'text': x}
        ))
        fig.update_layout(
        paper_bgcolor="#2E2EFE",
        height=250,  
        width = 250
        )

        fig

#
# Segundo bloque
#
cols = st.columns(6, gap='medium')
ncol = 0
for x in asigs[6:12]:
    ncol = ncol + 1
    #
    # Calculamos los promedios de cada asignatura
    #
    media = pd.to_numeric(df_cal[x]).mean().round(2)
    
    with cols[ncol-1]:
        #st.write(f"#### {x}")
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=media,
            gauge=dict(
                axis=dict(range=[None, 10]),
                bar=dict(color="green"),
                steps=[
                    dict(range=[0, 10], color="lightgray")
                ],
            ),
            #domain={"x": [0, 1], "y": [0, 1]},
            domain={'row': 0, 'column':  0},
            title={'text': x}
        ))
        fig.update_layout(
        paper_bgcolor="#2E2EFE",
        height=250,  
        width = 250
        )

        fig

