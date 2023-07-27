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
Cada imagen muestra el promedio de calificaciones para cada asignatura de todas las generaciones. 
"""

st.warning('Para el cálculo NO se incluyeron los alumnos que han desertado.')

"""
##
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


cols1,cols2 = st.columns([2,6])

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


#
# Heatmap de calificaciones
#
# Asignaturas 

"""
---
### ¿Qué es un mapa de calor (*heatmap*)?

Un mapa de calor (heat map, en inglés) es una técnica de visualización de datos que mide la magnitud de un fenómeno en colores en dos dimensiones. 
La variación del color puede ser por tono o intensidad, haciendo obvia la lectura del fenómeno sobre el espacio que se trata.

A continuación se muestra un *heatmap* que permite comparar los **promedios de las calificaciones** para cada asignatura y para cada generación de la MAD.

La intensidad del color es proporcional al promedio de las calificaciones consideradas.

Los valores nulos (*null*) se deben a las asignaturas que no se han calificado para el semestre 2023-2 al momento del desarrollo de esta aplicación.
"""
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


layout = go.Layout(xaxis=go.layout.XAxis(
    title=go.layout.xaxis.Title(
        text='Depth Axis',
    )),
yaxis=go.layout.YAxis(
    title=go.layout.yaxis.Title(
        text='Time Axis',
    )
))

trace.colorbar.title = "Calificación"


fig.update_layout(autosize=False, width=600, height=600, title={'text':'Mapa de calor de calificaciones'})
fig = go.Figure(data = trace, layout=layout)
#fig['layout'].update(plot_bgcolor='#2E64FE')
st.plotly_chart(fig, use_container_width=True)

#
# Promedio general por generación
#

# fig = px.bar(
#    y=df_gg['Promedio'], 
#    x=df_gg['Generación'], 
#    title='Calificación Total Promedio por Generación',
#    color=df_gg['Promedio'],
#    text=df_gg['Promedio'].round(2),
#    labels = dict(x = "Generación",y = "Promedio Total")
# )
# fig.update_layout(yaxis_range=[6,10])

# st.plotly_chart(fig, use_container_width=True)

"""
---
#### Las calificiones por generación
En este apartado mostramos una gráfica de barras que nos permite visualizar los promedios de las calificaciones
de todas las asignaturas para todas las generaciones.
"""
figx = px.bar(
   df_gg,
   x='Generación',
   y='Promedio',
   title='Calificación Total Promedio por Generación',
   color=df_gg['Promedio'],
   text=df_gg['Promedio'].round(2),
   labels = dict(x = "",y = ""),
   hover_name="Generación",
   #hover_data=['Promedio', 'Generación'],
    color_continuous_scale=["#9FF781", "#088A29"]
)
#figx.update_layout(yaxis_range=[6,10])
figx.update(layout_coloraxis_showscale=False)
figx.update_yaxes(visible=False, showticklabels=False)
figx.update_yaxes(visible=False, showticklabels=False)
# Ancho relativo de las barras. 1 es la norma.
figx.update_traces(width=0.5)

# Fuente: https://stackoverflow.com/questions/60158618/plotly-how-to-add-elements-to-hover-data-using-plotly-express-piechart
# import plotly.express as px
# df = px.data.gapminder().query("year == 2007").query("continent == 'Americas'")
# fig = px.pie(df, values='pop', names='country',
#              title='Population of American continent',
#              custom_data=['lifeExp','iso_num'], labels={'lifeExp':'life expectancy','iso_num':'iso num'
#                                                       })
# fig.update_traces(textposition='inside', textinfo='percent+label',\
#                  hovertemplate = "Country:%{label}: <br>Population: %{value} </br>(life expentancy, iso num) : %{customdata}"
# )


st.plotly_chart(figx, use_container_width=True)

# st.write(df_cleaned)

# fig = px.line_polar(df_cleaned, r="frequency", theta="direction", color="strength", line_close=True,
#                     color_discrete_sequence=px.colors.sequential.Plasma_r,
#                     template="plotly_dark",)
# fig.show()