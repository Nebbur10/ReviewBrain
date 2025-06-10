import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.components.header import render_header
from src.components.footer import render_footer

st.set_page_config(page_title="Legal", layout="wide")
render_header()

st.markdown("""
<div style='min-height: 70vh'>
    <h1>⚖️ Aviso Legal y Políticas</h1>
    <h3>Política de Privacidad</h3>
    <p>En ReviewBrain nos tomamos muy en serio la protección de tus datos personales. Esta Política de Privacidad explica cómo recopilamos, utilizamos y protegemos la información que nos proporcionas a través de nuestro sitio web [www.reviewbrain.com] (en adelante, “el Sitio”).
    <h4>1. Responsable del tratamiento</h4>
    <p>Nombre del responsable: Rubén Carrasco Marcos</p>
    <p>Nombre comercial: ReviewBrain</p>
    <p>Correo electrónico de contacto: contacto@reviewbrain.com</p>
    <h4>2. Datos personales que recopilamos</h4>
    <p>Cuando interactúas con nuestro sitio, podemos recopilar los siguientes datos personales:</p>
    <p>Nombre y apellidos (si los introduces en formularios)</p>
    <p>Dirección de correo electrónico</p>
    <p>Número de teléfono (si lo proporcionas)</p>
    <p>Dirección IP</p>
    <p>Datos técnicos de navegación y comportamiento (mediante cookies y herramientas de análisis)</p>
    <h4>3. Finalidades del tratamiento</h4>
    <p>Los datos personales que recopilamos se utilizan para:</p>
    <p>Atender tus solicitudes y responder consultas.</p>
    <p>Gestionar los servicios ofrecidos por ReviewBrain.</p>
    <p>Enviar comunicaciones informativas o comerciales, siempre que nos hayas dado tu consentimiento.</p>
    <p>Analizar el uso del sitio web para mejorar la experiencia del usuario.</p>
    <h4>4. Base legal del tratamiento</h4>
    <p>El tratamiento de tus datos se basa en:</p>
    <p>Tu consentimiento explícito (formularios, cookies, etc.).</p>
    <p>La ejecución de un contrato (cuando contratas o utilizas nuestros servicios).</p>
    <p>El interés legítimo de ReviewBrain en mejorar sus servicios y ofrecer una experiencia segura y eficiente.</p>
    <h4>5. Conservación de los datos</h4>
    <p>Tus datos serán conservados únicamente durante el tiempo necesario para cumplir con las finalidades descritas, o mientras exista una obligación legal que lo justifique. Una vez finalizado ese plazo, se eliminarán de forma segura.</p>
    <h4>6. Destinatarios de los datos</h4>
    <p>No compartimos tus datos con terceros, salvo cuando sea estrictamente necesario para prestarte nuestros servicios (por ejemplo, proveedores de hosting o analítica) o en cumplimiento de obligaciones legales. En estos casos, garantizamos que dichos terceros cumplen con el Reglamento General de Protección de Datos (RGPD).</p>
    <h4>7. Tus derechos</h4>
    <p>Puedes ejercer en cualquier momento los siguientes derechos:</p>
    <p>Acceder a tus datos personales.</p>
    <p>Rectificar datos incorrectos o incompletos.</p>
    <p>Solicitar la supresión de tus datos (derecho al olvido).</p>
    <p>Oponerte o limitar el tratamiento de tus datos.</p>
    <p>Solicitar la portabilidad de tus datos.</p>
    <p>Para ello, escríbenos a contacto@reviewbrain.com, adjuntando una copia de tu documento de identidad.</p>
    <h4>8. Seguridad</h4>
    <p>ReviewBrain adopta todas las medidas de seguridad técnicas y organizativas necesarias para proteger tus datos personales frente a pérdida, acceso no autorizado, uso indebido o divulgación.</p>
    <h4>9. Cookies</h4>
    <p>Utilizamos cookies propias y de terceros para personalizar la experiencia de usuario y analizar el uso del sitio. Puedes consultar todos los detalles en nuestra [Política de Cookies].</p>
    <h4>10. Cambios en la Política</h4>
    <p>Esta Política de Privacidad puede actualizarse ocasionalmente. Publicaremos las modificaciones en esta misma página e indicaremos la fecha de la última actualización.</p>
    <h3>Política de Cookies</h3>
    <p>En <strong>ReviewBrain</strong>, utilizamos cookies para mejorar tu experiencia de usuario, analizar el uso del sitio web y ofrecerte contenidos personalizados. Al navegar por nuestro sitio <em>www.reviewbrain.com</em>, aceptas el uso de cookies conforme a esta política.</p>
    <h4>1. ¿Qué son las cookies?</h4>
    <p>Las cookies son pequeños archivos de texto que se almacenan en tu dispositivo (ordenador, móvil, tablet…) cuando visitas una página web. Permiten que el sitio recuerde tus preferencias, hábitos de navegación y otra información útil para ofrecerte una experiencia más personalizada.</p>
    <h4>2. Tipos de cookies que usamos</h4>
    <p>Cookies técnicas (necesarias): Permiten el funcionamiento básico del sitio web y no requieren consentimiento.</p>
    <p>Cookies de análisis: Recogen datos estadísticos sobre el uso de la web.</p>
    <p>Cookies de personalización: Permiten recordar tus preferencias (idioma, diseño…).</p>
    <p>Cookies de terceros: Usamos herramientas externas como Google Analytics para obtener métricas de tráfico y comportamiento.</p>
    <h4>3. ¿Cómo puedes gestionar tus cookies?</h4>
    <p>Al entrar en el sitio por primera vez, te mostraremos un aviso para que puedas aceptar, rechazar o configurar tus preferencias. También puedes cambiar la configuración desde tu navegador:</p>
    <p><a href="https://support.google.com/chrome/answer/95647?hl=es" target="_blank">Google Chrome</a></p>
    <p><a href="https://support.mozilla.org/es/kb/habilitar-y-deshabilitar-cookies" target="_blank">Mozilla Firefox</a></p>
    <p><a href="https://support.microsoft.com/es-es/help/4027947" target="_blank">Microsoft Edge</a></p>
    <p>Ten en cuenta que la desactivación de algunas cookies puede afectar a la funcionalidad del sitio web.</p>
    <h4>4. Cambios en esta Política</h4>
    <p>Podemos actualizar esta política ocasionalmente. La fecha de última actualización aparecerá siempre al inicio del documento.</p>
    <h3>Aviso Legal</h3>
    <p>Titular del sitio web: Rubén Carrasco Marcos</p>
    <p>Nombre comercial:</strong> ReviewBrain</p>
    <p>Correo electrónico: <a href="mailto:contacto@reviewbrain.com">contacto@reviewbrain.com</a></p>
    <p>Sitio web: www.reviewbrain.com</p>
    <h4>1. Objeto</h4>
    <p>El presente Aviso Legal regula el acceso, navegación y uso del sitio web www.reviewbrain.com, así como las responsabilidades derivadas de la utilización de sus contenidos. El simple acceso al sitio implica la aceptación de este aviso sin reservas.</p>
    <h4>2. Propiedad intelectual e industrial</h4>
    <p>Todos los contenidos del sitio (textos, imágenes, logotipos, código fuente, diseño, etc.) son propiedad de Rubén Carrasco Marcos o de terceros autorizados, y están protegidos por la legislación de propiedad intelectual. Queda prohibida su reproducción, distribución o modificación sin autorización expresa.</p>
    <h4>3. Responsabilidad</h4>
    <p>ReviewBrain no se hace responsable del mal uso del contenido del sitio ni de los daños que puedan derivarse del acceso o uso del mismo. Tampoco garantiza la ausencia de virus u otros elementos que puedan producir alteraciones en el sistema informático del usuario.</p>
    <h4>4. Enlaces</h4>
    <p>Este sitio puede incluir enlaces a páginas externas sobre las que ReviewBrain no tiene control. No nos responsabilizamos del contenido ni de las prácticas de privacidad de dichas webs.</p>
    <h4>5. Legislación aplicable</h4>
    <p>Este sitio se rige por la legislación española y europea vigente. Cualquier conflicto relacionado con el uso de esta web se someterá a los tribunales competentes de la ciudad de residencia del titular, salvo que la normativa disponga otra cosa.</p>
</div>
""", unsafe_allow_html=True)

render_footer()
