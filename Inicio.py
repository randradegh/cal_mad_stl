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
st.image("images/head_02.png")
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


st.markdown("""
<style>
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: white;
   font-size: 10px;
}
</style>
""", unsafe_allow_html=True)

#
# Lectura de datos
#
df = read_data()

tab1, tab2, tab3, tab4 = st.tabs(["MAD y sus Datos", "¿Qué es el Análisis de Datos? ", "Los Datos", "Revelaciones"])

with tab1:
    """
    ### MAD y sus Datos
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
    la **Maestría en Alta Dirección** de la Facultad de Química de la UNAM.
    """

with tab2:

    """
    ### ¿Qué es el análisis de datos?

    El análisis de datos es el proceso de exploración, transformación y examen de datos para identificar tendencias y patrones que revelen *insights* importantes y aumenten 
    la eficiencia para respaldar la toma de decisiones. Una estrategia moderna de análisis de datos les permite a los sistemas y a las organizaciones trabajar a partir 
    de análisis automatizados en tiempo real, lo que garantiza resultados inmediatos y de gran impacto.

    #### El proceso de análisis de datos
    El proceso de análisis de datos se basa en varios pasos y fases. Es posible que las conclusiones de fases posteriores requieran volver a trabajar en una fase anterior, 
    lo que implica un proceso más cíclico que lineal. Lo más importante es que el éxito de los procesos de análisis de datos depende de la capacidad de repetición y automatización de cada uno de estos pasos.
    """
with tab3:
    """
    ___
    ## Origen de los datos

    Los datos fueron proporcionados en una hoja de cálculo con el formato *xlsx*.

    El archivo original contiene la información que comprende desde el inicio de la maestría y hasta el semestre 2023-1.

    Las columnas que contiene el archivo base son:

    > Nombre, Generación, 100%, Graduado, DHyPC, MCyF, ERSyL, EEyME, DTH, SO o DO, VPI, SIG, DE, DCS, DF, C, SIMAD, Promedio, ADA, Observaciones, Fecha de Nacimiento, Edad al ingresar, Carrera, Escuela, IES, Otro grado, Escuela otro e IES otro.

    #### Limpieza de los datos

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
    df_cleaned = clean_data(df)
    st.write(df_cleaned)


    """
    ___
    #### Datos limpios
    - Se reemplazaron los valores de 'NI' y 'NP' por valores nulos, de tal manera que 
    no sean tomados en cuenta para los cálculos estadísticos necesarios para el análisis.
    - Se eliminaron los registros de los alumnos que hayan desertado.

    Solamente se muestran los datos cuantitativos.

    ##### **_Dataframe_** con los datos limpios
    """

    df_num=df_cleaned.drop(['Generación'], axis=1)
    st.write(df_num)

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

with tab4:
    """
    ## Revelaciones (*insights*)
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
    # font_color_text = '#7FB3D5'
    # font_color_number = '#61210B'
    # BGCOLOR = "#2E64FE"
    # col01, col02, col03, col04, col05 = st.columns(5)
    # fig_ind = go.Figure()

    # with col01:
    #     ref = 5
    #     fig_ind.add_trace(go.Indicator(
    #         mode = "number",
    #         number = {'prefix': "",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
    #         value = qty_alumnos_registrados,
    #         title = {'text': 'Alumnos<br><b>Registrados</b>', 'font.size': 25, 'font.color':font_color_text},
    #         domain = {'row': 0, 'column': 0}))
        
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

    # font_color_text = 'white'
    # font_color_number = '#002b7a'
    # BGCOLOR = "#FAAC58"
    # col11, col12, col13, col14 = st.columns(4)
    # fig_ind2 = go.Figure()

    # with col11:
    #     ref = 6
    #     fig_ind2.add_trace(go.Indicator(
    #         mode = "number",
    #         number = {'prefix': "",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
    #         value = qty_graduados,
    #         title = {'text': '<b>Graduados</b>', 'font.size': 25, 'font.color':font_color_text},
    #         domain = {'row': 0, 'column': 0}))
        
    # with col12:
    #     ref = 6
    #     fig_ind2.add_trace(go.Indicator(
    #         mode = "number",
    #         number = {'prefix': "",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
    #         value = qty_desertores,
    #         title = {'text': '<b>Desertores</b>', 'font.size': 25, 'font.color':font_color_text},
    #         domain = {'row': 0, 'column': 1}))
        
    # with col13:
    #     ref = 5
    #     fig_ind2.add_trace(go.Indicator(
    #         mode = "number",
    #         number = {'prefix': "",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
    #         value = cal_promedio_gral,
    #         title = {'text': '<b>Promedio</b><br>General', 'font.size': 25, 'font.color':font_color_text},
    #         domain = {'row': 0, 'column': 2}))

    # with col14:
    #     ref = 5
    #     fig_ind2.add_trace(go.Indicator(
    #         mode = "number",
    #         number = {'suffix': "%",'font.size' : 60, 'font.color': font_color_number, 'valueformat':','},
    #         value = porcien_desertores,
    #         title = {'text': '<b>Porcentaje de</b><br>Desertores', 'font.size': 25, 'font.color':font_color_text},
    #         domain = {'row': 0, 'column': 3}))


    # fig_ind2.update_layout(
    #     paper_bgcolor = BGCOLOR, 
    #     width=1200,
    #     height = 220,
    #     margin=dict(l=20, r=20, t=40, b=0),
    #     grid = {'rows': 1, 'columns': 4, 'pattern': "independent"},
    # )

    # fig_ind2

    #c1, c2, c3, c4 = st.columns(4)
    c1, c2, c3, c4= st.columns(4)
    c1.metric("Alumnos Registrados", qty_alumnos_registrados)
    c2.metric("Alumnos Analizados", cant_alumnos_total)
    c3.metric("Generaciones", qty_gen)
    c4.metric("Asignaturas", 12)

    c11, c12, c13, c14= st.columns(4)
    c11.metric("Cantidad de Graduados", qty_graduados)
    c12.metric("Desertores", qty_desertores)
    c13.metric("Promedio General", cal_promedio_gral)
    c14.metric("Porcentaje de Desertores", str(porcien_desertores) + '%')
    


    # fig = go.Figure()


    # fig.add_trace(go.Indicator(
    # value = 200,
    # delta = {'reference': 160},
    # gauge = {
    #     'axis': {'visible': False}},
    # domain = {'row': 0, 'column': 0}))

    # fig.add_trace(go.Indicator(
    # value = 120,
    # gauge = {
    #     'shape': "bullet",
    #     'axis' : {'visible': False}},
    #     domain = {'row': 0, 'column': 1}))
        

    # fig.update_layout(
    #     grid = {'rows': 1, 'columns': 2, 'pattern': "independent"},
    #     template = {'data' : {'indicator': [{
    #         'title': {'text': "Speed"},
    #         'mode' : "number+delta+gauge",
    #         'delta' : {'reference': 90}}]
    #                         }})

    # fig