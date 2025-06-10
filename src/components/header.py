import streamlit as st

def render_header():
    st.markdown("""
        <div style="background-color:#1f2937;padding:10px 20px;border-radius:5px">
            <h1 style="color:white;font-size:24px;margin:0">🏠 Bienvenido a ReviewBrain</h1>
        </div>
    """, unsafe_allow_html=True)
    st.logo("images/logo_empresa.png", size="large")
