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
    [data-testid=stSidebar] {
        background-color: #08088A;
    }
</style>
""", unsafe_allow_html=True)

#
# Lectura de datos
#
df = read_data()

#
# Limpiamos datos
#
df_cleaned = clean_data(df)

#st.markdown("Tabla con datos cuantitativos (sin generaciones)")
df_num=df_cleaned.drop(['Generación'], axis=1)
#st.write(df_num)
# st.write(f"Cantidad de registros: {df_num.shape[0]}")

"""
### Boxplot
El gráfico **_boxplot_**, también conocido como diagrama de caja y bigotes, es una herramienta visual que nos ayuda a entender la distribución de un conjunto de datos y a detectar valores atípicos o extremos en ellos. Este gráfico muestra la mediana (valor que divide el conjunto de datos en dos partes iguales), el rango intercuartílico (la distancia entre el primer y tercer cuartil), y los valores mínimo y máximo que no son considerados valores atípicos.

La estructura del boxplot está compuesta por:

- La caja: Representa el rango intercuartílico y contiene el 50% de los datos. La línea dentro de la caja indica la mediana.

- Los bigotes: Son las líneas que se extienden desde la caja y llegan hasta los valores más extremos que no son considerados valores atípicos. Generalmente, se calculan como 1.5 veces el rango intercuartílico.

- Los valores atípicos: Son los puntos fuera de los bigotes y representan valores que están significativamente alejados del resto de los datos.

El gráfico boxplot muestra de manera clara la estructura básica de la distribución, resaltando la mediana, los cuartiles y los valores atípicos. 
A diferencia de la curva de Gauss, no hace supuestos sobre la forma de la distribución, 
sino que proporciona una imagen más completa de cómo están distribuidos los datos, 
incluyendo información sobre la dispersión y posibles valores atípicos.

---
#### Calificaciones promedio de los alumnos
"""
fig = go.Figure()
for col in df_num:
  fig.add_trace(go.Box(y=df_num[col].values, name=df_num[col].name))
  
fig.update_layout(title='Boxplot de los promedios de las calificaciones por asignatura')
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

"""
---
#### Edad de los alumnos al ingresar a la MAD
"""

fig = px.histogram(df, x=df['Edad al ingresar'], nbins=40, 
                   title="Gráfico de barras de la edad de los alumnos al ingresar", 
                   color=df["Edad al ingresar"])
fig.update_layout(
    font_family="Arial",
    font_color="blue",
    title_font_family="Arial",
    title_font_color="white",
    xaxis_title="Edad",
    yaxis_title="Cantidad",
    legend_title_font_color="white"
)
#fig.update_layout(xaxis={'categoryorder':'total ascending'}) # add only this line

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

"""
---
#### Edad de los alumnos al ingresar a la MAD
"""
fig=px.box(y=df['Edad al ingresar'].values, title='Boxplot de la edad de los alumnos al ingresar')
fig.update_layout(
    font_family="Arial",
    font_color="blue",
    title_font_family="Arial",
    title_font_color="white",
    xaxis_title="Edad",
    yaxis_title="Cantidad",
    legend_title_font_color="white"
)
fig

"""
---
#### Cantidad de alumnos por IES de origen
"""
dfc = df.groupby(['IES'])['IES'].count().reset_index(name='count')
dfc=dfc.nlargest(10, 'count')
#st.write(dfc)
fig = px.bar(dfc, x='IES', y='count', title="Las primeras diez IES por frecuencia", color=dfc["IES"])
fig.update_layout(
    font_family="Arial",
    font_color="blue",
    title_font_family="Arial",
    title_font_color="white",
    xaxis_title="IES",
    yaxis_title="Cantidad",
    showlegend=False,
    #legend_title_font_color="white",
    xaxis={'categoryorder':'total descending'}
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)


#
# Gráfico de sectores
#
"""
---
Cantidad de alumnos por IES de origen
"""
dfc = df.groupby(['IES'])['IES'].count().reset_index(name='count')
dfc=dfc.nlargest(10, 'count')


fig = px.pie(dfc, values='count', names='IES', title='Las primeras diez IES por frecuencia')
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

