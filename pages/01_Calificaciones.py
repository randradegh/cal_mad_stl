# Incluímos las bibliotecas necesarias
from utils import *
from os import ST_WRITE
# Debe ser el primer comando
st.set_page_config(
    layout="wide",
    page_title="Análisis de Calificaciones. MAD/FQ/UNAM",
    page_icon="🧊",     
    initial_sidebar_state="auto"
)

#
# Encabezado
#
encabezado()

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
div[data-baseweb="select"] > div {
    background-color:#CED8F6;
                color:#0B0B61
}
</style>""", unsafe_allow_html=True)


st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #08088A;
    }
</style>

""", unsafe_allow_html=True)



#
# Lectura de datos
#
df = read_data()
#st.write(df)

#
# Limpieza de datos
#
df_cleaned = clean_data(df)

"""
## Indicadores de Desempeño

### Promedios Totales por Asignatura
- Cada imagen muestra el promedio de calificaciones para cada asignatura de todas las generaciones. 
- **Para el cálculo no se incluyeron los alumnos que han desertado.**
###
"""

#
# Extraemos los nombre de las asignaturas en una lista
#
asigs = df.columns[5:17].tolist()

#
# Primer bloque
#
cols = st.columns(4, gap='small')
ncol = 0
for x in asigs[0:4]:
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
cols = st.columns(4, gap='small')
ncol = 0
for x in asigs[4:8]:
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
# Tercer bloque
#
cols = st.columns(4, gap='small')
ncol = 0
for x in asigs[8:12]:
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
# Análisis de promedio general de calificaciones por asignatura y generación
#
# Recuperación de las generaciones
#
df_cleaned["Generación"] = df_cleaned["Generación"].astype("category")

"""
---
### Análisis del promedio general de calificaciones por asignatura y generación

Para tener un análisis más detallado de las calificaciones, a continuación se presentan los histogramas del promedio de las calificaciones para cada asignatura.

Se puede seleccionar la generación a analizar.
###
"""
# Ordenar y obtener los valores únicos de la columna 'Generación'
generaciones = sorted(df_cleaned['Generación'].unique())

#st.write(generaciones)
# Convertir los valores a cadena sin separador de miles
generaciones = [int(g) for g in generaciones]


cols1,cols2 = st.columns([1,6])

with cols1:
    # Crear el widget select en Streamlit
    generacion_seleccionada = st.selectbox('**:orange[Seleccione una generación]**', generaciones)

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
    
fig = px.bar( df_gsg, x='asignatura', y='calificaciones', color='calificaciones', 
             title='Calificaciones promedio de la Generación ' + str(generacion_seleccionada),
             #text='calificaciones',
             text_auto=True,
             color_continuous_scale=['red', 'white', 'green'])

fig.update_layout(
    #margin=dict(l=10, r=10, t=10, b=10),
    #paper_bgcolor='#5882FA',
    width = 800,
    height = 500
)

fig.update_traces(textposition="outside",
                  textfont_size = 14
                  )
fig


st.warning("### ¿Poner *insights*?")

#
# Heatmap de calificaciones
#
# Asignaturas 
asignaturas = (df_cleaned.columns.to_numpy())
# st.write(asignaturas)
# st.write(df_cleaned)
df_gg=df_cleaned.groupby(['Generación'])[asignaturas].mean()

# Convertimos el index 'Generación' a columna.
df_gg.reset_index(inplace=True)

df_gg["Generación"] = df_gg['Generación'].astype("category")

# st.markdown('Agrupada')
# st.write(df_gg)
# st.write(df_gg['Generación'])

#
# Mapa de calor
#
gen = df_gg.values.round(1)

#st.write(gen)
trace = go.Heatmap(
   x = asignaturas,
   y = df_gg['Generación'],
   z = gen,
   type = 'heatmap',
   colorscale = ['white', '#31B404'],
   zmin=5,
   zmax=10,
   text=gen,
   #title={"text":"Title"},
   texttemplate="%{text}",
   textfont={"size": 10, "color":'white'}
)




trace.colorbar.title = "Calificación"

fig = go.Figure(data = trace)
fig.update_layout(autosize=False, width=600, height=600, title={'text':'Mapa de calor de calificaciones'})
#fig['layout'].update(plot_bgcolor='#2E64FE')
st.plotly_chart(fig, use_container_width=True)

#
# Promedio general por generación
#

fig = px.bar(
   y=df_gg['Promedio'], 
   x=df_gg['Generación'], 
   title='Calificación Total Promedio por Generación',
   color=df_gg['Promedio'],
   text=df_gg['Promedio'].round(2),
   labels = dict(x = "Generación",y = "Promedio Total")
)
fig.update_layout(yaxis_range=[6,10])

st.plotly_chart(fig, use_container_width=True)
