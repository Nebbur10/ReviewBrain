import streamlit as st

def render_footer():
    st.markdown("""
        <style>
        .footer {
            width: 100%;
            background-color: #1f2937;
            padding: 20px 10px 20px 40px;
            color: white;
            font-size: 14px;
        }
        .footer .column {
            float: left;
            width: 23%;
            margin-right: 2%;
        }
        .footer .column:last-child {
            margin-right: 0;
        }
        .footer:after {
            content: "";
            display: table;
            clear: both;
        }
        .footer h4 {
            margin-top: 0;
            font-size: 16px;
        }
        input {
            width: 90%;
            padding: 6px;
            margin-top: 6px;
            border-radius: 4px;
            border: none;
        }
        a.footer-link {
            color: white;
            text-decoration: none;
        }
        a.footer-link:hover {
            text-decoration: underline;
        }
        iframe {
            border: 0;
        }
        </style>

        <div class="footer">
            <div class="column">
                <h4>📍 Dirección</h4>
                <p>Calle Ficticia 123<br>Madrid, España</p>
                <iframe src="https://maps.google.com/maps?q=madrid&t=&z=13&ie=UTF8&iwloc=&output=embed"
                        width="100%" height="100" allowfullscreen></iframe>
            </div>
            <div class="column">
                <h4>📬 Contacto</h4>
                <form>
                    <label>Email:</label><br>
                    <input type="email" placeholder="tucorreo@empresa.com"><br><br>
                    <label>Teléfono:</label><br>
                    <input type="tel" placeholder="+34 000 000 000"><br><br>
                </form>
            </div>
            <div class="column">
                <h4>🌐 Navegación</h4>
                <p><a class="footer-link" href="/Inicio" target="_self">🏠 Inicio</a></p>
                <p><a class="footer-link" href="/Analisis" target="_self">📊 Análisis</a></p>
            </div>
            <div class="column">
                <h4>⚖️ Legal</h4>
                <p><a class="footer-link" href="/Legal#politica-de-privacidad" target="_self">Política de privacidad</a></p>
                <p><a class="footer-link" href="/Legal#politica-de-cookies" target="_self">Política de cookies</a></p>
                <p><a class="footer-link" href="/Legal#aviso-legal" target="_self">Aviso legal</a></p>
            </div>
        </div>
    """, unsafe_allow_html=True)
