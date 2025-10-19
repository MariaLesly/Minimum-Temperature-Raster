import os
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# -------------------------------------------
# CONFIGURACIÓN DE LA APP
# -------------------------------------------
st.set_page_config(
    page_title="Accesibilidad a Hospitales en el Perú",
    layout="wide"
)

# TÍTULO PRINCIPAL
st.title("Temperaturas mínimas y riesgo de heladas en el Perú")
st.caption("Análisis raster de temperaturas a nivel distrital y propuestas de política pública")

# Directorio base del proyecto (2 niveles arriba de este script)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# -------------------------------------------
# FUNCIÓN PARA MOSTRAR FIGURAS PNG
# -------------------------------------------
def show_img(filename, height=600):
    """Carga y muestra una figura PNG desde /outputs/."""
    img_path = os.path.join(BASE_DIR, "outputs", filename)
    try:
        if not os.path.exists(img_path):
            st.error(f"No se encontró el archivo: {img_path}")
            return
        st.image(img_path, caption=filename, use_container_width=True)
    except Exception as e:
        st.error(f"Error mostrando el mapa {filename}: {e}")

# -------------------------------------------
# PESTAÑAS
# -------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
     "Descripción de los datos",
    "Estadísticas zonales y tablas",
    "Gráficos",
    "Propuestas de política pública"
])

# TAB 1 - DESCRIPCIÓN DE DATOS
with tab1:
    st.header("Descripción de los Datos")
    st.markdown("""
    Esta sección presentan los datos empleados para el análisis de temperaturas en el Perú.  
    Se utilizan tres tipos principales de datos:
    
    1. **TBC**: TBC 
    2. **TBC**: TBC
    3. **TBC**: TBC

    """)

st.header("📂 Carga del Raster")

uploaded = st.file_uploader("Sube un raster de temperatura (.tif)", type=["tif"])

if uploaded is None:
    st.info("Usando el raster de ejemplo incluido en la app.")
    raster_path = os.path.join(BASE_DIR, "data", "tmin_raster.tif")
else:
    raster_path = uploaded

# Mostrar vista previa o imagen ilustrativa
preview_path = os.path.join(BASE_DIR, "figures", "raster_preview.png")
if os.path.exists(preview_path):
    st.image(preview_path, caption="Vista previa del raster base")
else:
    st.warning("No se encontró la vista previa del raster.")


# TAB 2 - Estadísticas zonales
with tab2:
    st.header("Estadísticas zonales")

    st.markdown("""
    [TBC: Se presentan estadísticas (at least: mean, min, max, std, p10, p90) + one custom metric.]
    """)

    st.markdown("""
    [TBC: Se presentan las tablas descargables en formato CSV]
    """)

# TAB 3 - Gráficos
with tab3:
    st.header("Gráfico de distribución")

    show_img("TBC")
    st.markdown("""
   [TBC: Aquí se presenta el gráfico de distribución]
    """)

    st.subheader("Ranking")
    show_img("TBC")
    st.markdown("""
    [TBC: Aquí se presenta el gráfico de ranking]
    """)

    st.subheader("Mapa estático")
    st.markdown("""
     [TBC: Aquí se presenta el mapa estático]
    """)

# TAB 4 - Propuestas de política pública
with tab4:
    st.header("Propuestas de política pública ante el friaje en zonas altoandinas y olas de frío en la Amazonía")

    st.subheader("Red de monitoreo de salud climática")
    st.markdown("""
    - **Objetivo específico:** Disminución de enfermedades respiratorias mediante la detección temprana y respuesta rápida a brotes vinculados a bajas temperaturas.
    - **Población / territorio objetivo:** Niños menores de 5 años y adultos mayores en distritos de Puno, Cusco, Ayacucho y Huancavelica.
    - **Intervención:** Instalación de una red digital de vigilancia:
            - Centros de salud equipados con sensores de temperatura ambiental y alertas automáticas de riesgo.
            - Uso de mensajería móvil para notificar a promotores y familias sobre medidas preventivas cuando la temperatura baja a umbrales críticos (<9.5°C)
    - **Costo estimado:** Inversión en sensores, software y capacitación ascendente a S/1,920,000 (S/20,000 por cada uno de los 64 hospitales en funcionamiento en los 4 departamentos seleccionados).
    - **KPI:** −10% en hospitalizaciones por infecciones respiratorias en zonas monitoreadas.
    """)

    st.subheader("Protección de ganado frente a helados")
    st.markdown("""
    - **Objetivo específico:** Reducir la mortalidad del ganado por hipotermia durante heladas.
    - **Población / territorio objetivo:** Distritos altoandinos ganaderos con temperaturas menores menores a 9.5°C en Puno, Cusco, Ayacucho y Huancavelica.
    - **Intervención:** Construcción de 1,000 módulos de resguardo ganadero (cobertizos térmicos con aislamiento y pisos secos).
    - **Costo estimado:** Inversión en construcción de módulos ascendente a S/3,500,000 (S/3,500 por módulo)
    - **KPI:** -10% en la mortalidad de alpacas, ovinos y vacunos durante heladas.
    """)

    st.subheader("Horario escolar flexible en distritos vulnerables al de friaje")
    st.markdown("""
    - **Objetivo específico:** Reducir el ausentismo y los casos de infecciones respiratorias agudas (IRA) en estudiantes de educación básica durante los meses de menor temperatura.
    - **Población / territorio objetivo:** Estudiantes de instituciones educativas públicas en distritos con temperaturas mínimas promedio menores a 9.5 °C, principalmente en Puno, Cusco, Ayacucho y Huancavelica.
    - **Intervención:** Implementar un horario escolar flexible y escalonado durante la temporada de friaje (mayo–agosto), que contemple:
            - Retrasar el inicio de clases entre 90 y 120  minutos en zonas de heladas intensas (de 8:00 a 8:30 a.m. o más tarde).
            - Coordinar con las UGEL y DRE para ajustar calendarios sin reducir horas lectivas anuales.
    - **Costo estimado:** S/10,000 de gastos de coordinación y difusión por cada una de las 47 UGEL en los departamentos priorizados.
    - **KPI:** −10% en la tasa de inasistencia escolar de los distritos priorizados en los meses de junio–agosto (vs. promedio 3 años previos).
    """)


