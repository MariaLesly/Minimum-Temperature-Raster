# 🌡️ Minimum-Temperature-Raster

Este repositorio contiene un análisis geoespacial sobre las temperaturas mínimas en el Perú, utilizando raster data. El propósito es evaluar la distribución espacial de las temperaturas mínimas y generar visualizaciones interactivas.

## 📁 Estructura del repositorio

```
Minimum-Temperature-Raster/
├── .devcontainer/            # Configuración para entornos de desarrollo
├── .ipynb_checkpoints/       # Archivos temporales de Jupyter Notebook
├── data/                     # Datos: ráster Tmin  y shapefile de distritos
├── outputs/                  # Resultados generados
├── streamlit/                # Aplicación interactiva con Streamlit
├── 3.1.ipynb                 # Notebook con análisis preliminar
├── Tmin_Peru_Analisis.ipynb  # Notebook principal de análisis
├── req_notebook.txt          # Requisitos para ejecutar Jupyter Notebook
└── requirements.txt          # Dependencias para el deploy del Streamlit
```

## 🧪 Requisitos

Para ejecutar este proyecto, necesitas tener instaladas las siguientes dependencias:

- Python 3.8+
- Bibliotecas listadas en `req_notebook.txt` y `requirements.txt`, según corresponda.



## 🚀 Uso

1. **Análisis en Jupyter Notebook**: Abre el archivo `Tmin_Peru_Analisis.ipynb` para explorar el análisis de las temperaturas mínimas en Perú.
2. **Aplicación Streamlit**: Navega al directorio `streamlit/` y ejecuta la aplicación con:

   ```conda prompt
   streamlit run streamlit_app.py
   ```

## 🗂️ Datos

Los datos utilizados en este proyecto se encuentran en el directorio `data/`.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).

