import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

import streamlit as st
from src.components.header import render_header
from src.components.footer import render_footer

st.set_page_config(page_title="Inicio", layout="wide")

render_header()

st.markdown("""
<div style='min-height: 10vh'>
<br>
    <p>Explora las opciones desde el menú lateral izquierdo:</p>
    <ul>
        <li>📊 Análisis de clústeres</li>
        <li>💡 Servicios inteligentes</li>
        <li>📬 Contacto con la empresa</li>
        <li>📜 Información legal</li>
    </ul>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div style='min-height: 30vh'>
    <h4>🛠️ Servicios que ofrecemos</h4>
    <h6>🔍 Análisis de Opiniones</h6>
    <p>Procesamos y categorizamos automáticamente opiniones de clientes.</p>
    <h6>📊 Clustering temático</h6>
    <p>Detectamos temas clave usando algoritmos de agrupamiento.</p>
    <h6>📈 Análisis de sentimientos</h6>
    <p>Identificamos si los clientes opinan positivamente o negativamente.</p>
    <h6>☁️ Visualización interactiva</h6>
    <p>Dashboard completo con nubes de palabras, gráficas y filtros avanzados.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='min-height: 10vh'>
    <h4>📬 Contacta con nosotros</h4>
    <p>Si deseas más información o contratar nuestros servicios, déjanos tus datos y te llamaremos:</p>
    <ul>
        <li>📧 Email: contacto@reviewbrain.com</li>
        <li>📞 Teléfono: +34 912 345 678</li>
        <li>📍 Dirección: Calle Ficticia 123, Madrid</li>
    </ul>
</div>
""", unsafe_allow_html=True)

render_footer()
