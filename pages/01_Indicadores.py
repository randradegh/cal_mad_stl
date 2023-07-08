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
st.write(df)

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
            domain={'row': 0, 'column':  0},
            title={'text': x}
        ))
        fig.update_layout(
        paper_bgcolor="#2E2EFE",
        height=250,  
        width = 250
        )

        fig

# Supongamos que tienes un DataFrame llamado 'df' con una columna 'Generación'
df_cleaned["Generación"] = df_cleaned["Generación"].astype("category")

# Ordenar y obtener los valores únicos de la columna 'Generación'
generaciones = sorted(df_cleaned['Generación'].unique())

#st.write(generaciones)
# Convertir los valores a cadena sin separador de miles
generaciones = [int(g) for g in generaciones]


# Crear el widget select en Streamlit
generacion_seleccionada = st.selectbox('Selecciona una generación', generaciones)

#st.write('Sel: ' + str(generacion_seleccionada))

#
# Gráfico de la generación seleccionada
#

asignaturas = (df_cleaned.columns.to_numpy())

# Filtramos para la generación seleccionada
#
df_gs = df_cleaned[(df_cleaned['Generación']==generacion_seleccionada)]
#st.write(df_gs)

df_gs=df_gs.drop(['Generación', 'Promedio'], axis=1)


df_gsg=df_gs.mean()
df_gsg=df_gsg.to_frame()

df_gsg.reset_index(inplace=True)
df_gsg.rename({'index':'asignatura', 0:'calificaciones'}, axis=1, inplace=True)
#st.write(df_gsg)
    
fig = px.bar( df_gsg, x='asignatura', y='calificaciones', color='calificaciones', 
             title='Calificaciones promedio de la Generación ' + str(generacion_seleccionada),
             color_continuous_scale=['red', 'blue'])
fig