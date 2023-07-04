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


t1, t2 = st.columns((1,5), gap="medium") 
#t1.image('images/fq_logo_01.png', width = 50)
t1.image('images/UNAM-universidad-1.png', width = 100)
t2.write("# :green[Maestría en Alta Dirección] - :blue[FQ / UNAM]")
st.header("Proyecto Datos MAD")

#
# Lectura de datos
#
df = pd.read_csv("data/cal_mad_01.csv", sep=',')

# Eliminamos las columnas no necesarias para el análisis de calificaciones
# df_cal contendrá solamente las calificaciones y las generaciones
df_cal=df.drop(['No.', 'Nombre', 'Avance', 'Graduado', 'SIMAD', 'ADA', 'Fecha de Nacimiento', 'Carrera', 'Escuela', 'IES', 'Otro grado', 'Escuela otro', 'IES otro', 'Edad al ingresar'], axis=1)
#st.write(df_cal)

#
# Limpiamos datos
#
for column in df_cal:
    df_cal[column] = df_cal[column].replace('NI',np.nan)
    df_cal[column] = df_cal[column].replace('NP',np.nan)
    df_cal[column] = df_cal[column].astype("float64")


#st.markdown("Tabla con datos cuantitativos (sin generaciones)")
df_num=df_cal.drop(['Generación'], axis=1)
#st.write(df_num)
st.write(f"Cantidad de registros: {df_num.shape[0]}")


fig = go.Figure()

for col in df_num:
  fig.add_trace(go.Box(y=df[col].values, name=df[col].name))
  
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

df['Fecha de Nacimiento'] = df['Fecha de Nacimiento'].astype('datetime64[ns]')
df['Year'] = df['Fecha de Nacimiento'].dt.strftime('%Y')

fig = px.bar(df, x=df['Year'], title="Año de Nacimiento", color=df["Year"])
fig.update_layout(
    font_family="Arial",
    font_color="blue",
    title_font_family="Arial",
    title_font_color="brown",
    xaxis_title="Año de Nacimiento",
    yaxis_title="Cantidad",
    legend_title_font_color="brown"
)
#fig.update_layout(xaxis={'categoryorder':'total ascending'}) # add only this line

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

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

#
# Heatmap de calificaciones
#
# Asignaturas 
asignaturas = (df_cal.columns.to_numpy())
st.write(asignaturas)
df_gg=df_cal.groupby(['Generación'])[asignaturas].mean()
#st.write(type(df_gg))
df_gg["Generación"] = df_gg['Generación'].astype("category")

st.markdown('Agrupada')
st.write(df_gg)

gen = df_gg.values.round(1)


st.write(gen)
trace = go.Heatmap(
   x = asignaturas,
   y = df_gg['Generación'],
   z = gen,
   type = 'heatmap',
   colorscale = 'plasma',
   zmin=5,
   zmax=10,
   text=gen,
   texttemplate="%{text}",
   textfont={"size": 10, "color":'maroon'}
)
data = [trace]

fig = go.Figure(data = data)
st.plotly_chart(fig, use_container_width=True)

#
# Promedio generañ por generación
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
