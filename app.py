import streamlit as st

# Configuración de la página con temática de El Principito
st.set_page_config(
    page_title="El Principito y los Secretos de la Mente",
    page_icon="🦊",
    layout="wide"
)

# -----------------------------------------------------------------------------
# Panel de Control (Sidebar)
# -----------------------------------------------------------------------------
st.sidebar.title("🪐 Planeta B612")
st.sidebar.markdown("Explora los misterios visuales:")

opcion = st.sidebar.radio(
    "Navegación estelar:",
    [
        "1. Proximidad (Las estrellas)",
        "2. Semejanza (El jardín de rosas)",
        "3. Continuidad (El camino del desierto)",
        "4. Cierre (La boa y el elefante)",
        "5. Figura y Fondo (La puesta de sol)",
        "6. Simetría (Los volcanes ordenados)",
        "7. Destino Común (Los pájaros migrantes)",
        "🧩 Mini-Quiz Estelar (¡A jugar!)"
    ]
)

# -----------------------------------------------------------------------------
# Contenido Principal en formato de Cuento
# -----------------------------------------------------------------------------
if opcion == "1. Proximidad (Las estrellas)":
    st.title("⭐ 1. Ley de la Proximidad: El secreto de las estrellas")
    st.write("### 📖 Érase una vez...")
    st.write("El Principito miraba todas las noches las millones de estrellas de su pequeño planeta. Aunque son luceros separados, cuando el aviador miraba el cielo, su mente unía instintivamente aquellas que estaban más juntitas para formar constelaciones y dibujos imaginarios.")
    st.info("💡 **El secreto visual:** Los elementos que están cerca unos de otros se perciben como un grupo o una familia.")
    st.image("https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=600", caption="Las estrellas cercanas forman constelaciones ante nuestros ojos", width=500)

elif opcion == "2. Semejanza (El jardín de rosas)":
    st.title("🌹 2. Ley de la Semejanza: El gran jardín de la Tierra")
    st.write("### 📖 Érase una vez...")
    st.write("Cuando el Principito llegó a la Tierra y entró a un jardín lleno de cinco mil rosas idénticas, se sintió muy triste porque pensaba que su flor era única en el universo. Sin embargo, su cerebro entendió al instante que todas esas flores formaban un solo equipo visual porque compartían el mismo color rojo y la misma forma.")
    st.info("💡 **El secreto visual:** Las cosas que tienen el mismo color, forma o estilo parecen pertenecer al mismo grupo.")
    st.image("https://images.unsplash.com/photo-1558882224-dda166733046?w=600", caption="Las flores idénticas se agrupan en nuestra mente de inmediato", width=500)

elif opcion == "3. Continuidad (El camino del desierto)":
    st.title("🛤️ 3. Ley de la Continuidad: Las huellas en la arena")
    st.write("### 📖 Érase una vez...")
    st.write("En su caminar por el vasto y silencioso desierto, el Principito buscaba una señal de vida. Sus ojos no veían puntos aislados, sino que seguían de forma natural las líneas de las dunas y las huellas sobre la arena, como si un camino invisible guiara sus pasos hacia el horizonte.")
    st.info("💡 **El secreto visual:** A nuestro cerebro le encanta seguir líneas, curvas y direcciones fluidas sin perderse.")
    st.image("https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=600", caption="El camino de arena guía nuestra mirada sin esfuerzo", width=500)

elif opcion == "4. Cierre (La boa y el elefante)":
    st.title("🐘 4. Ley del Cierre: El misterio del sombrero")
    st.write("### 📖 Érase una vez...")
    st.write("El pequeño príncipe dibujó una serpiente boa que se había tragado a un elefante. Los adultos veían un simple sombrero porque les faltaban líneas por cerrar, pero los niños, con su gran imaginación, completaban los trazos vacíos en su mente para ver al elefante por dentro.")
    st.info("💡 **El secreto visual:** El cerebro humano adora completar figuras incompletas por sí mismo.")
    st.image("https://images.unsplash.com/photo-1557683316-973673baf926?w=600", caption="Completando formas y siluetas mentales", width=500)

elif opcion == "5. Figura y Fondo (La puesta de sol)":
    st.title("🌅 5. Ley de Figura y Fondo: El atardecer en el asteroide")
    st.write("### 📖 Érase una vez...")
    st.write("Para ver una puesta de sol, al Principito le bastaba con mover su silla unos pasos en su diminuto planeta. En ese instante mágico, el sol radiante se convertía en la gran **figura** protagonista, mientras que el cielo oscuro pasaba a ser un tranquilo **fondo** acompañante.")
    st.info("💡 **El secreto visual:** Destacamos lo más importante (figura) separándolo del entorno (fondo).")
    st.image("https://images.unsplash.com/photo-1534447677768-be436bb09401?w=600", caption="El sol brilla como figura principal sobre el cielo de fondo", width=500)

elif opcion == "6. Simetría (Los volcanes ordenados)":
    st.title("🌋 6. Ley de la Simetría: Los tres volcanes del planeta")
    st.write("### 📖 Érase una vez...")
    st.write("En el planeta B612 había tres volcanes: dos activos para calentar el desayuno y uno apagado que servía de taburete. Cuando el Principito los limpiaba todas las mañanas, cuidaba que guardaran un orden tan equilibrado y simétrico que su pequeño mundo se sentía en absoluta paz.")
    st.info("💡 **El secreto visual:** Las formas equilibradas, ordenadas y simétricas transmiten una armonía visual inmediata.")
    st.image("https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=600", caption="El equilibrio y la simetría generan orden visual", width=500)

elif opcion == "7. Destino Común (Los pájaros migrantes)":
    st.title("🦅 7. Ley de Destino Común: El vuelo hacia la libertad")
    st.write("### 📖 Érase una vez...")
    st.write("El día que el Principito tuvo que abandonar su planeta para explorar otros mundos, aprovechó la gran migración de una bandada de pájaros silvestres. Todos los pájaros volaban coordinados hacia el mismo rumbo, demostrando que aquello que se mueve junto, comparte un mismo destino.")
    st.info("💡 **El secreto visual:** Los elementos que se mueven o apuntan en la misma dirección parecen estar conectados.")
    st.image("https://images.unsplash.com/photo-1522858547374-e8d99805b74a?w=600", caption="Elementos con una misma dirección y propósito compartido", width=500)

elif opcion == "🧩 Mini-Quiz Estelar (¡A jugar!)":
    st.title("🧩 Mini-Quiz: Pon a prueba tu mente estelar")
    st.write("¡Es hora de demostrar lo que aprendiste en este viaje por los asteroides!")
    
    pregunta_1 = st.radio(
        "1. Si ves las estrellas del cielo agruparse formando constelaciones por su cercanía, ¿qué ley estamos usando?",
        ["Ley del Cierre", "Ley de la Proximidad", "Ley de la Simetría"]
    )
    
    if st.button("Comprobar Respuesta 1"):
        if pregunta_1 == "Ley de la Proximidad":
            st.success("🎉 ¡Correcto! Las estrellas cercanas se agrupan por proximidad.")
        else:
            st.error("❌ ¡Casi! La respuesta correcta es la Ley de la Proximidad.")

    st.markdown("---")
    
    pregunta_2 = st.radio(
        "2. ¿Por qué el Principito y los niños pueden ver un elefante dentro de la boa aunque falten trazos?",
        ["Porque el cerebro aplica la Ley del Cierre", "Porque las serpientes vuelan", "Por arte de magia estelar"]
    )
    
    if st.button("Comprobar Respuesta 2"):
        if pregunta_2 == "Porque el cerebro aplica la Ley del Cierre":
            st.success("🌟 ¡Excelente! Tu mente completa las formas incompletas.")
        else:
            st.error("❌ ¡Inténtalo de nuevo! Es la Ley del Cierre.")
