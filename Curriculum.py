import streamlit as st
import pandas as pd
import time

st.set_page_config(layout="wide")

col1, col2 = st.columns([0.2,1.2])

with col1:
    # Agregamos mi imagen
    # Extreaemos la imagen de la carpeta Documents
    st.image("C:/Users/gusta/Documents/ImagenCV.jpeg", width=200)

with col2:
    # Agregamos mi nombre
    st.title("Gustavo Rodríguez Ayala")
    col3, col4, col5, col6, col7 = st.columns([0.03,0.15,0.03, 0.03, 0.3])

    with col3:
        st.image("C:/Users/gusta/Downloads/actuario.png", width=50)
        
    with col4:
        st.subheader("Estudiante de Actuaría")

    with col5:
        st.image("C:/Users/gusta/Downloads/Escudo-facultad-ciencias-unam-escalable.svg.png", width=53)
    with col6:
        st.image("C:/Users/gusta/Downloads/Escudo-UNAM-escalable.svg.png", width=49)
    with col7:
        st.subheader("Universidad Nacional Autónoma de México")
    
    col8, col9, col10, col11, col12, col13 = st.columns([0.03,0.15,0.03, 0.2, 0.03, 0.1])
    with col8:
        st.image("C:/Users/gusta/Downloads/llamada-telefonica.png", width=30)
    with col9:
        st.write("5533134149")
    with col10:
        st.image("C:/Users/gusta/Downloads/correo.png", width=40)
    with col11:
        st.markdown("[gusrodriguezayala@gmail.com](mailto:gusrodriguezayala@gmail.com)",unsafe_allow_html=True)
    with col12:
        st.image("C:/Users/gusta/Downloads/linkedin.png", width=35)
    with col13:
        st.write("[Gustavo Rodríguez Ayala](https://www.linkedin.com/in/gustavo-rodríguez-ayala-08714025b/)")

col14, col15 = st.columns(2)
with col14:
    st.header("Experiencia")
    st.write("Becario de Análisis de Datos en Stellantis")
    st.write("Septiembre 2024 - Presente")  
    exp1 = st.expander("Actividades")
    exp2 = st.expander("Conocimientos")
    with exp1:
        st.write(""
        "- Elaboración de reportes para monitorio de competencia en el mercado, analizando datos. \n "
        "- Migracion completa de dashboards desde Qlik Sense a Power Bi. \n "
        "- Apoyo en revision de costos y precios de vehiculos. \n"
        "- Apoyo en comparación de escenarios de presupuest vs escenarios reales. \n"
        "- Experiencia en resolver problemas a través de modelos matemáticos y la estadística (Regresiones lineales, modelos lineales generalizados) en R. \n"
        "- Conocimiento de métodos de Machine Learning como clustering, bootstraping, componentes principales. \n"
        "- Manejo de Excel, hojas de cálculo, funciones básicas, macros básico, gráficas y tablas dinámicas. \n"
        "- Conocimiento de programación orientada a objetos y estructuras de datos en Python, tales como DataFrames. \n"
        "- Análisis e interpretación de información a través de Python. \n"
        "- Cursos realizados en la aplicación DataCamp enfocados a Python.")
    with exp2:
        st.write(""
        "- Experiencia en resolver problemas a través de modelos matemáticos y la estadística (Regresiones lineales, regresiones lineales múltiples, modelos lineales generalizados) en R. \n"
        "- Conocimiento de métodos de Machine Learning como clustering (k-means, jerarquias), bootstraping, componentes principales, análisis factorial exploratorio. \n"
        "- Manejo de Excel, hojas de cálculo, funciones básicas, macros básico, gráficas y tablas dinámicas. \n"
        "- Conocimiento de programación orientada a objetos y estructuras de datos en Python, tales como DataFrames. \n"
        "- Análisis e interpretación de información a través de Python. \n"
        "- Cursos realizados en la aplicación DataCamp enfocados a Python. \n"
        "- Conocimiento de la herramienta Power BI para la creación de dashboards. \n"
        "- Conocimiento del lenguaje R enfocado en estadística y datos. \n")

    st.header("Proyectos")
    st.write("Proyecto financiero")
    exp3 = st.expander("Descripción")
    with exp3:
        st.write("Llevé a cabo un proyecto en donde se utiliza el modelo de Black-Litterman para obtener portafolios de inversión óptimos a través de views del mercado financiero. (Con Python-Streamlit y GitHub).")



