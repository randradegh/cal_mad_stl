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

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

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

qty_desertores = len(df[df.Avance == 'Desertó'])
qty_graduados = len(df[df.Graduado == 'Si'])
qty_alumnos_registrados = len(df)

#
# Limpiamos datos
#


#
# Eliminación de los registros de los alumnos que desertaron
##
df_cleaned = clean_data(df)
#st.write(df_cleaned)


df_num=df_cleaned.drop(['Generación'], axis=1)
#st.write(df_num)

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
cal_promedio_gral = df_cleaned.Promedio.mean().round(2)

# Porcentaje de desertores
porcien_desertores= (qty_desertores * 100) / qty_alumnos_registrados

#
# Indicadores
#
font_color_text = '#7FB3D5'
font_color_number = '#61210B'
BGCOLOR = "#2E64FE"


#col01, col02, col03, col04, col05 = st.columns(5)

#cols1,cols2 = st.columns([1,6])

c1, c2 = st.columns(2)
c1.metric("Temperature", "70 °F", "1.2 °F")
c2.metric("Humidity", "86%", "4%")


fig = go.Figure()


fig.add_trace(go.Indicator(
value = 200,
delta = {'reference': 160},
gauge = {
    'axis': {'visible': False}},
domain = {'row': 0, 'column': 0}))

fig.add_trace(go.Indicator(
value = 120,
gauge = {
    'shape': "bullet",
    'axis' : {'visible': False}},
    domain = {'row': 0, 'column': 1}))

fig.update_layout(
    grid = {'rows': 1, 'columns': 2, 'pattern': "independent"},
    template = {'data' : {'indicator': [{
        'title': {'text': "Speed"},
        'mode' : "number+delta+gauge",
        'delta' : {'reference': 90}}]
                         }})

fig



# with coli11:
#     ref = 5
#     fig_ind_01.add_trace(go.Indicator(
#         mode = "number",
#         number = {'prefix': "",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
#         value = qty_alumnos_registrados,
#         title = {'text': 'Alumnos<br><b>Registrados</b>', 'font.size': 25, 'font.color':font_color_text},
#         domain = {'row': 0, 'column': 0}))





#with coli12:
    # #ref = 5
    # fig_ind_01.add_trace(go.Indicator(
    #     mode = "number",
    #     number = {'prefix': "",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
    #     value = qty_alumnos_registrados,
    #     title = {'text': 'Alumnos<br><b>Registrados</b>', 'font.size': 25, 'font.color':font_color_text},
    #     domain = {'row': 0, 'column': 1}))
    #st.write("# Hola mundo")

# fig_ind_01.update_layout(
#     paper_bgcolor = BGCOLOR, 
#     width=550,
#     height = 220,
#     margin=dict(l=20, r=20, t=40, b=0),
#     grid = {'rows': 1, 'columns': 1, 'pattern': "independent"},
# )

#fig_ind_01


# with col02:
#     ref = 5
#     fig_ind.add_trace(go.Indicator(
#         mode = "number",
#         number = {'prefix': "",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
#         value = cant_alumnos_total,
#         title = {'text': 'Alumnos<br><b>Analizados</b>', 'font.size': 25, 'font.color':font_color_text},
#         domain = {'row': 0, 'column': 1}))

# with col03:
#     ref = 5
#     fig_ind.add_trace(go.Indicator(
#         mode = "number",
#         number = {'prefix': "",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
#         value = qty_gen,
#         title = {'text': '<b>Generaciones</b>', 'font.size': 25, 'font.color':font_color_text},
#         domain = {'row': 0, 'column': 2}))
    
# with col04:
#     ref = 5
#     fig_ind.add_trace(go.Indicator(
#         mode = "number",
#         number = {'prefix': "",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
#         value = 12,
#         title = {'text': '<b>Asignaturas</b>', 'font.size': 25, 'font.color':font_color_text},
#         domain = {'row': 0, 'column': 3}))
    
    
# fig_ind.update_layout(
#     paper_bgcolor = BGCOLOR, 
#     width=1200,
#     height = 220,
#     margin=dict(l=20, r=20, t=40, b=0),
#     grid = {'rows': 1, 'columns': 4, 'pattern': "independent"},
# )

# fig_ind