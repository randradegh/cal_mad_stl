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
st.write(f"Cantidad de registros: {df_num.shape[0]}")

fig = go.Figure()
for col in df_num:
  fig.add_trace(go.Box(y=df_num[col].values, name=df_num[col].name))
  
st.plotly_chart(fig, theme="streamlit", use_container_width=True)


fig = px.histogram(df, x=df['Edad al ingresar'], nbins=40, title="Edad al ingresar", color=df["Edad al ingresar"])
fig.update_layout(
    font_family="Arial",
    font_color="blue",
    title_font_family="Arial",
    title_font_color="brown",
    xaxis_title="Edad",
    yaxis_title="Cantidad",
    legend_title_font_color="brown"
)
#fig.update_layout(xaxis={'categoryorder':'total ascending'}) # add only this line

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

fig=px.box(y=df['Edad al ingresar'].values, title='Edad al ingresar')
fig.update_layout(
    font_family="Arial",
    font_color="blue",
    title_font_family="Arial",
    title_font_color="brown",
    xaxis_title="Edad",
    yaxis_title="Cantidad",
    legend_title_font_color="brown"
)
fig


fig = px.bar(df['IES'], title="IES", color=df["IES"])
fig.update_layout(
    font_family="Arial",
    font_color="blue",
    title_font_family="Arial",
    title_font_color="brown",
    xaxis_title="IES",
    yaxis_title="Cantidad",
    legend_title_font_color="brown",
    xaxis={'categoryorder':'total descending'}
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)


#
# Gráfico de sectores
#
dfc = df.groupby(['IES'])['IES'].count().reset_index(name='count')
dfc=dfc.nlargest(10, 'count')


fig = px.pie(dfc, values='count', names='IES', title='Los 10 Primeros IES')
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# #
# # Heatmap de calificaciones
# #
# # Asignaturas 
# asignaturas = (df_cleaned.columns.to_numpy())
# st.write(asignaturas)

#df_gg=df_cleaned.groupby(['Generación'])[asignaturas].mean()
# #st.write(type(df_gg))
#df_gg.reset_index(inplace=True)

#df_gg["Generación"] = df_gg['Generación'].astype("category")

# st.markdown('Agrupada')
#st.write(df_gg)

# #
# # Mapa de calor
# #
# gen = df_gg.values.round(1)

# #st.write(gen)
# trace = go.Heatmap(
#    x = asignaturas,
#    y = df_gg['Generación'],
#    z = gen,
#    type = 'heatmap',
#    colorscale = ['white', '#31B404'],
#    zmin=5,
#    zmax=10,
#    text=gen,
#    #title={"text":"Title"},
#    texttemplate="%{text}",
#    textfont={"size": 10, "color":'white'}
# )




# trace.colorbar.title = "Calificación"

# fig = go.Figure(data = trace)
# fig.update_layout(autosize=False, width=600, height=600, title={'text':'Mapa de calor de calificaciones'})
# #fig['layout'].update(plot_bgcolor='#2E64FE')
# st.plotly_chart(fig, use_container_width=True)

# #
# # Promedio general por generación
# #

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
