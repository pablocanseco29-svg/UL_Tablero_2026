import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="Magia Visual: Leyes de la Gestalt",
    page_icon="🎨",
    layout="wide"
)

# -----------------------------------------------------------------------------
# Panel de Control (Sidebar) - Las 7 Actividades / Principios de la Gestalt
# -----------------------------------------------------------------------------
st.sidebar.title("🧠 Menú Mágico")
st.sidebar.markdown("Elige un superpoder de la mente:")

opcion_seleccionada = st.sidebar.radio(
    "Leyes de la Gestalt:",
    [
        "1. Proximidad (Amigos cercanos)",
        "2. Semejanza (¡Del mismo equipo!)",
        "3. Continuidad (Siguiendo el caminito)",
        "4. Cierre (Completando el dibujo)",
        "5. Figura y Fondo (El héroe y el paisaje)",
        "6. Simetría (Todo en orden y equilibrio)",
        "7. Destino Común (Moviéndose juntos)"
    ]
)

# -----------------------------------------------------------------------------
# Contenido Principal adaptado para niños de 10 años
# -----------------------------------------------------------------------------
if opcion_seleccionada == "1. Proximidad (Amigos cercanos)":
    st.title("🤝 Ley de la Proximidad")
    st.write("### ¡Imagina que estás en el recreo!")
    st.write("Los niños que están parados muy juntitos en el patio, automáticamente pensamos que son **amigos del mismo grupo**, aunque no los conozcamos a todos.")
    st.info("💡 **En diseño:** Los elementos que están cerca unos de otros se perciben como si estuvieran relacionados. Por eso los botones de un menú están juntitos.")

elif opcion_seleccionada == "2. Semejanza (¡Del mismo equipo!)":
    st.title("👕 Ley de la Semejanza")
    st.write("### ¡Un partido de fútbol en la escuela!")
    st.write("Si ves a 20 personas en una cancha y 10 tienen camiseta roja y 10 tienen camiseta azul, tu cerebro dice al instante: *'¡Ellos son un equipo y ellos son el otro!'*.")
    st.info("💡 **En diseño:** Las cosas que tienen el mismo color, forma o tamaño parecen tener la misma función.")

elif opcion_seleccionada == "3. Continuidad (Siguiendo el caminito)":
    st.title("🛤️ Ley de la Continuidad")
    st.write("### Siguiendo las huellas")
    st.write("A nuestro cerebro le encanta seguir líneas, curvas o caminitos. Si ves una fila de hormigas o una hilera de puntos, tus ojos la siguen automáticamente como si fuera un tobogán.")
    st.info("💡 **En diseño:** Ayuda a guiar la mirada de las personas de una información a otra sin que se pierdan.")

elif opcion_seleccionada == "4. Cierre (Completando el dibujo)":
    st.title("🧩 Ley del Cierre")
    st.write("### ¡Magia mental!")
    st.write("¿Alguna vez has jugado a unir los puntos? Aunque falte un pedacito de una línea, tu cerebro es tan inteligente que **completa el dibujo por ti** sin que se note el espacio vacío.")
    st.info("💡 **En diseño:** No necesitamos dibujar todo perfecto; el cerebro humano adora terminar las formas incompletas por sí solo.")

elif opcion_seleccionada == "5. Figura y Fondo (El héroe y el paisaje)":
    st.title("🦸‍♂️ Ley de Figura y Fondo")
    st.write("### El superhéroe en la película")
    st.write("Cuando ves una película, te fijas en el superhéroe (la **figura**) y el paisaje de fondo se vuelve borroso o pasa desapercibido (el **fondo**). No podemos mirar ambas cosas con la misma atención al mismo tiempo.")
    st.info("💡 **En diseño:** Destacamos lo más importante haciendo que el resto quede más tranquilo al fondo.")

elif opcion_seleccionada == "6. Simetría (Todo en orden y equilibrio)":
    st.title("⚖️ Ley de la Simetría")
    st.write("### Como una mariposa")
    st.write("Las cosas que son simétricas (iguales de ambos lados, como una mariposa o tu cara frente al espejo) nos dan una sensación de **paz, orden y belleza** inmediata.")
    st.info("💡 **En diseño:** Las páginas web ordenadas y simétricas se sienten más profesionales y agradables de leer.")

elif opcion_seleccionada == "7. Destino Común (Moviéndose juntos)":
    st.title("🦅 Bandada de pájaros")
    st.write("### ¡Todos para uno!")
    st.write("Si ves una bandada de pájaros volando hacia la misma dirección, o un grupo de personas caminando juntas hacia la salida del colegio, tu cerebro asume que **van hacia el mismo objetivo**.")
    st.info("💡 **En diseño:** Los elementos que se mueven o cambian al mismo tiempo parecen estar conectados.")
