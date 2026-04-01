import streamlit as st
import os

# Configuración
st.set_page_config(page_title="Idea de Investigación", layout="wide")

# -----------------------
# LOGO SUPERIOR DERECHO
# -----------------------
st.markdown("""
<div style="position:fixed; top:10px; right:20px; text-align:right; z-index:1000;">
    <img src="https://www.uandes.cl/wp-content/uploads/2025/11/UTEM.png" width="80">
</div>
""", unsafe_allow_html=True)

# -----------------------
# SIDEBAR
# -----------------------
st.sidebar.title("Navegación")

seccion = st.sidebar.radio(
    "Ir a:",
    [
        "Inicio",
        "Idea",
        "Fundamento",
        "Problema",
        "Lineups",
        "Palabras clave"
    ]
)

# Nombre abajo en sidebar
st.sidebar.markdown("---")
st.sidebar.markdown(
    "<p style='position:fixed; bottom:10px; left:20px; font-size:14px;'>Christian Pérez Flores</p>",
    unsafe_allow_html=True
)

# -----------------------
# IMAGEN + TÍTULO
# -----------------------
st.markdown("""
<div style="display:flex; justify-content:center;">
    <img src="https://images.unsplash.com/photo-1507874457470-272b3c8d8ee2"
         style="width:100%; max-height:500px; object-fit:cover; border-radius:10px;">
</div>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 style='font-size:40px; text-align:center; margin-bottom:30px;'>¿Qué hace exitoso un lineup? Un análisis de datos sobre festivales de música</h1>",
    unsafe_allow_html=True
)

# -----------------------
# FUNCION CAJAS
# -----------------------
def caja(titulo, contenido):
    st.markdown(f"""
    <div style='padding:20px; border-radius:10px; border:1px solid #ddd; margin-bottom:20px;'>
        <h3>{titulo}</h3>
        <p style='font-size:18px;'>{contenido}</p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------
# SECCIONES
# -----------------------

if seccion == "Inicio":

    col1, col2 = st.columns([3,1])

    with col1:
        caja("Área",
             "OCDE: Ciencias Sociales (Economía y Negocios) / ODS 9: Industria, Innovación e Infraestructura")

    with col2:
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/3/31/Sustainable_Development_Goal-es-09.jpg",
            use_column_width=True
        )

elif seccion == "Idea":
    caja("Idea",
         "Analizar cómo la composición de los lineups de festivales de música influye en la decisión de compra de entradas, considerando variables como cantidad de artistas, presencia de headliners, popularidad y diversidad de géneros.")

elif seccion == "Fundamento":
    caja("Fundamento o Motivación",
         "La organización de festivales musicales implica decisiones estratégicas de alto costo. Sin embargo, estas decisiones suelen basarse en criterios subjetivos. La Ciencia de Datos permite analizar información de plataformas digitales para identificar patrones en el comportamiento del público.")

    caja("Inserción de Ingenieros en el ámbito Laboral",
         "Este tema se vincula con la formación de ingenieros en Ciencia de Datos capaces de aplicar modelos en industrias creativas, aportando valor mediante análisis predictivo.")

elif seccion == "Problema":
    caja("Descripción del Problema",
         "Existe incertidumbre sobre qué características de un lineup generan mayor interés. No está claro si priorizar popularidad, cantidad o diversidad maximiza la venta de entradas.")

elif seccion == "Lineups":

    st.subheader("Ejemplos de Lineups")

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

elif seccion == "Palabras clave":

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Lista manual")
        st.markdown("""
        - music festivals  
        - lineup  
        - ticket sales  
        - consumer behavior  
        - artist popularity  
        - genre diversity  
        - music industry  
        """)

    with col2:
        st.markdown("### Expansión IA")
        st.markdown("""
        - lineup composition  
        - ticket demand modeling  
        - purchase intention  
        - audience behavior analysis  
        - artist popularity metrics  
        - genre diversification  
        - event attendance prediction  
        - demand forecasting  
        - cultural consumption  
        - entertainment economics  
        - recommender systems  
        - predictive analytics  
        """)
