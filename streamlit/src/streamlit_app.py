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

    st.subheader("Distribución")
    show_map("mapa_proximidad_Lima.html")
    st.markdown("""
   [TBC: Aquí se presenta el gráfico de distribución]
    """)

    st.subheader("Ranking")
    show_map("mapa_proximidad_Loreto.html")
    st.markdown("""
    [TBC: Aquí se presenta el gráfico de ranking]
    """)

    st.subheader("Mapa estático")
    st.markdown("""
     [TBC: Aquí se presenta el mapa estático]
    """)

# TAB 3 - Propuestas de política pública
with tab4:
    st.header("Propuestas de política pública ante el friaje en zonas altoandinas y olas de frío en la Amazonía")

    st.subheader("Propuesta de política 1")
    st.markdown("""
   [TBC: Aquí se desarrollará la propuesta de política 1]
    """)

    st.subheader("Propuesta de política 2")
    st.markdown("""
  [TBC: Aquí se desarrollará la propuesta de política 2]
    """)

    st.subheader("Propuesta de política 3")
    st.markdown("""
  [TBC: Aquí se desarrollará la propuesta de política 3]
    """)



