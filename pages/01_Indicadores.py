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
t1.image('images/UNAM-universidad-1.png', width = 100)
t2.write("# :green[Maestría en Alta Dirección] - :blue[FQ / UNAM]")
st.header("Proyecto Datos MAD")

#
# Lectura de datos
#
df = read_data()

#
# Limpieza de datos
#
df_cleaned = clean_data(df)

"""
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
    media = pd.to_numeric(df_cleaned[x]).mean().round(2)
    
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
    media = pd.to_numeric(df_cleaned[x]).mean().round(2)
    
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

