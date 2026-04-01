import streamlit as st
import os

# Configuración
st.set_page_config(page_title="Idea de Investigación", layout="wide")

# -----------------------
# IMAGEN INICIAL
# -----------------------
st.markdown("""
<div style="display:flex; justify-content:center;">
    <img src="https://images.unsplash.com/photo-1507874457470-272b3c8d8ee2"
         style="width:100%; max-height:750px; object-fit:cover; border-radius:10px;">
</div>
""", unsafe_allow_html=True)

# -----------------------
# TÍTULO
# -----------------------
st.markdown(
    "<h1 style='font-size:40px; text-align:center; margin-bottom:30px;'>¿Qué hace exitoso un lineup? Un análisis de datos sobre festivales de música</h1>",
    unsafe_allow_html=True
)

# -----------------------
# CONTENIDO
# -----------------------

st.markdown("<h2 style='font-size:26px;'>Área</h2>", unsafe_allow_html=True)
st.markdown("<p style='font-size:18px;'>Economía y Negocios.</p>", unsafe_allow_html=True)

st.markdown("<h2 style='font-size:26px;'>Idea</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='font-size:18px;'>
Analizar cómo la composición de los lineups de festivales de música influye en la decisión de compra de entradas, considerando variables como cantidad de artistas, presencia de headliners, popularidad y diversidad de géneros.
</p>
""", unsafe_allow_html=True)

st.markdown("<h2 style='font-size:26px;'>Fundamento o Motivación</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='font-size:18px;'>
La organización de festivales musicales implica decisiones estratégicas de alto costo, especialmente en la selección de artistas. Sin embargo, estas decisiones suelen basarse en criterios subjetivos. El uso de Ciencia de Datos permite analizar información proveniente de plataformas digitales y datos históricos para identificar patrones que expliquen el comportamiento del público.
</p>
""", unsafe_allow_html=True)

st.markdown("<h2 style='font-size:26px;'>Inserción de Ingenieros en el ámbito Laboral</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='font-size:18px;'>
Este tema se vincula con la formación de ingenieros en Ciencia de Datos capaces de aplicar técnicas analíticas en industrias creativas. Además, refleja una oportunidad laboral emergente donde profesionales pueden aportar valor mediante modelos predictivos y análisis de datos en el sector del entretenimiento.
</p>
""", unsafe_allow_html=True)

st.markdown("<h2 style='font-size:26px;'>Descripción del Problema</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='font-size:18px;'>
Existe incertidumbre respecto a qué características de un lineup generan mayor interés en el público. No está claro si priorizar artistas altamente populares, aumentar la cantidad total de artistas o diversificar géneros es más efectivo para maximizar la venta de entradas.
</p>
""", unsafe_allow_html=True)

# -----------------------
# IMÁGENES DE LINEUPS
# -----------------------

st.markdown("<h2 style='font-size:32px;'>Ejemplos de Lineups</h2>", unsafe_allow_html=True)

image_folder = "images"

if os.path.exists(image_folder):
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpeg")]

    cols = st.columns(3)

    for i, img in enumerate(images):
        img_path = os.path.join(image_folder, img)
        with cols[i % 3]:
            st.image(img_path, use_column_width=True)
            st.caption(img.replace(".jpeg", ""))
else:
    st.warning("Carpeta 'images' no encontrada.")

# -----------------------
# PALABRAS CLAVE
# -----------------------

st.markdown("---")
st.markdown("<h2 style='font-size:32px;'>Palabras clave</h2>", unsafe_allow_html=True)

# Lista manual
st.markdown("<h3 style='font-size:26px;'>1) Lista manual inicial</h3>", unsafe_allow_html=True)
st.markdown("""
<ul style='font-size:20px;'>
<li>music festivals</li>
<li>lineup</li>
<li>ticket sales</li>
<li>consumer behavior</li>
<li>artist popularity</li>
<li>genre diversity</li>
<li>music industry</li>
</ul>
""", unsafe_allow_html=True)

# Expansión IA
st.markdown("<h3 style='font-size:26px;'>2) Expansión con IA</h3>", unsafe_allow_html=True)
st.markdown("""
<ul style='font-size:20px;'>
<li>lineup composition</li>
<li>ticket sales prediction</li>
<li>purchase intention</li>
<li>audience engagement</li>
<li>artist ranking</li>
<li>streaming metrics</li>
<li>genre segmentation</li>
<li>event analytics</li>
<li>demand forecasting</li>
<li>entertainment industry analytics</li>
<li>machine learning</li>
<li>predictive modeling</li>
</ul>
""", unsafe_allow_html=True)