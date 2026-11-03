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
# Contenido Principal
# -----------------------------------------------------------------------------
if opcion == "1. Proximidad (Las estrellas)":
    st.title("⭐ 1. Ley de la Proximidad")
    st.write("### Las estrellas en el cielo de B612")
    st.write("Cuando miras el cielo nocturno, las estrellitas que están cerquita unas de otras las agrupamos con la mirada y decimos: *'¡Mira, ahí hay una constelación!'*.")
    st.info("💡 **En diseño:** Los elementos cercanos se sienten como una sola familia (como los botones de un menú).")
    # Espacio para imagen visual (puedes cambiar el link si encuentras otra)
    st.image("https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=600", caption="Las estrellas se agrupan por cercanía", width=500)

elif opcion == "2. Semejanza (El jardín de rosas)":
    st.title("🌹 2. Ley de la Semejanza")
    st.write("### El jardín de las 5,000 rosas")
    st.write("Cuando el Principito visitó el jardín terrestre, vio miles de flores rojas. Aunque eran muchas, su cerebro supo al instante que **todas pertenecían a la misma especie** porque tenían el mismo color y forma.")
    st.info("💡 **En diseño:** Lo que se ve igual (color, forma, tamaño), nuestro cerebro cree que sirve para lo mismo.")
    st.image("https://images.unsplash.com/photo-1558882224-dda166733046?w=600", caption="Las cosas semejantes se agrupan mentalmente", width=500)

elif opcion == "3. Continuidad (El camino del desierto)":
    st.title("🛤️ 3. Ley de la Continuidad")
    st.write("### Siguiendo las huellas en la arena")
    st.write("A nuestro cerebro le encanta seguir líneas y direcciones. Si ves una línea curva o huellas en el desierto, tus ojos viajan por ella automáticamente como si fuera un tobogán.")
    st.info("💡 **En diseño:** Sirve para guiar los ojos de quien lee de un punto a otro sin que se pierda.")

elif opcion == "4. Cierre (La boa y el elefante)":
    st.title("🐘 4. Ley del Cierre")
    st.write("### ¿Sombrero o elefante?")
    st.write("¿Te acuerdas del famoso dibujo del libro? Aunque al principio los adultos veían un sombrero, el dibujo tenía líneas incompletas. Nuestro cerebro completa los espacios vacíos para entender la figura.")
    st.info("💡 **En diseño:** No necesitamos dibujar todo perfecto; el cerebro humano adora terminar las formas por sí solo.")

elif opcion == "5. Figura y Fondo (La puesta de sol)":
    st.title("🌅 5. Ley de Figura y Fondo")
    st.write("### Disfrutando la puesta de sol")
    st.write("En el pequeño planeta del Principito, él podía ver atardeceres moviendo su silla. El sol brillante es la **figura** (lo importante) y el cielo del planeta es el **fondo** (lo que acompaña).")
    st.info("💡 **En diseño:** Destacamos lo importante haciendo que el resto pase a un segundo plano.")

elif opcion == "6. Simetría (Los volcanes ordenados)":
    st.title("🌋 6. Ley de la Simetría")
    st.write("### Los volcanes del Principito")
    st.write("El Principito tenía tres volcanes (dos activos y uno apagado). Las cosas simétricas, equilibradas y ordenadas nos transmiten una sensación inmediata de paz y belleza.")
    st.info("💡 **En diseño:** Una página web ordenada y simétrica se siente mucho más confiable.")

elif opcion == "7. Destino Común (Los pájaros migrantes)":
    st.title("🦅 7. Ley de Destino Común")
    st.write("### El viaje gracias a los pájaros silvestres")
    st.write("El Principito pudo viajar de planeta en planeta aprovechando una migración de pájaros silvestres. Si ves un grupo de cosas moviéndose hacia el mismo lado, tu cerebro asume que van al mismo destino.")
    st.info("💡 **En diseño:** Los elementos que se mueven o cambian juntos parecen estar conectados.")

elif opcion == "🧩 Mini-Quiz Estelar (¡A jugar!)":
    st.title("🧩 Mini-Quiz: Pon a prueba tu mente")
    st.write("¡Es hora de demostrar lo que aprendiste sobre cómo funciona nuestro cerebro!")
    
    # Esto es un WIDGET interactivo de Streamlit (una pregunta tipo test)
    pregunta_1 = st.radio(
        "1. Si ves un grupo de amigos muy juntos en el recreo, ¿qué ley de la Gestalt aplicas sin darte cuenta?",
        ["Ley del Cierre", "Ley de la Proximidad", "Ley de la Simetría"]
    )
    
    if st.button("Comprobar Respuesta 1"):
        if pregunta_1 == "Ley de la Proximidad":
            st.success("🎉 ¡Correcto! Por estar cerquita, asumimos que están juntos.")
        else:
            st.error("❌ ¡Casi! La respuesta correcta es la Ley de la Proximidad.")

    st.markdown("---")
    
    pregunta_2 = st.radio(
        "2. ¿Por qué el cerebro entiende un dibujo al que le falta una línea (como la boa y el elefante)?",
        ["Porque aplica la Ley del Cierre", "Porque las líneas vuelan", "Porque no importa el dibujo"]
    )
    
    if st.button("Comprobar Respuesta 2"):
        if pregunta_2 == "Porque aplica la Ley del Cierre":
            st.success("🌟 ¡Excelente! Tu cerebro es un mago completando formas.")
        else:
            st.error("❌ ¡Inténtalo de nuevo! Es la Ley del Cierre.")
