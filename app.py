import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Configuración de la página con temática de El Principito
st.set_page_config(
    page_title="El Principito y los Secretos de la Mente",
    page_icon="🦊",
    layout="wide"
)

# -----------------------------------------------------------------------------
# Panel de Control (Sidebar) con estilo de navegación
# -----------------------------------------------------------------------------
st.sidebar.title("🪐 Planeta B612")
st.sidebar.markdown("Panel de Control Interactivo:")

opcion = st.sidebar.radio(
    "Selecciona un principio:",
    [
        "1. Proximidad (Las estrellas)",
        "2. Semejanza (El jardín de rosas)",
        "3. Continuidad (El camino del desierto)",
        "4. Cierre (La boa y el elefante)",
        "5. Figura y Fondo (La puesta de sol)",
        "6. Simetría (Los volcanes ordenados)",
        "7. Destino Común (Los pájaros migrantes)",
        "🧩 Mini-Quiz Estelar"
    ]
)

# -----------------------------------------------------------------------------
# Contenido Principal
# -----------------------------------------------------------------------------
if opcion == "1. Proximidad (Las estrellas)":
    st.title("⭐ 1. Ley de la Proximidad: El cielo estrellado")
    st.write("### 📖 El cuento en el asteroide")
    st.write("Cuando el Principito observa el cielo nocturno de su asteroide, las estrellas que están cerca unas de otras forman constelaciones ante sus ojos. El cerebro las agrupa de inmediato.")
    
    st.markdown("---")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("#### 🎛️ Control interactivo de cercanía")
        distancia = st.slider("Ajusta la separación visual entre estrellas:", 1.0, 10.0, 2.0, 0.5)
        st.info(f"Con una separación de {distancia}, tu mente decide si forman un grupo o están aisladas.")
    with col2:
        st.markdown("#### 📊 Visualización en tiempo real")
        # Gráfico dinámico de puntos según la proximidad
        chart_data = pd.DataFrame({
            'x': [1, 1.5 + (distancia*0.1), 5, 5.5 + (distancia*0.1)],
            'y': [1, 1.2, 5, 5.3],
            'Grupo': ['Estrellas A', 'Estrellas A', 'Estrellas B', 'Estrellas B']
        })
        c = alt.Chart(chart_data).mark_circle(size=200).encode(x='x', y='y', color='Grupo')
        st.altair_chart(c, use_container_width=True)

elif opcion == "2. Semejanza (El jardín de rosas)":
    st.title("🌹 2. Ley de la Semejanza: Las 5,000 rosas")
    st.write("### 📖 El cuento en el jardín")
    st.write("Ante miles de rosas idénticas en la Tierra, el Principito nota que el cerebro agrupa automáticamente aquellas que comparten el mismo color y forma como un solo equipo.")
    
    st.markdown("---")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("#### 🎛️ Selector de similitud")
        color_filtro = st.selectbox("Elige qué grupo destacar:", ["Todas las rosas", "Solo Rojas", "Solo Amarillas"])
        st.success(f"Filtro aplicado: **{color_filtro}**. Tu mente separa por color de inmediato.")
    with col2:
        st.markdown("#### 📊 Panel de flores")
        data_rosas = pd.DataFrame({
            'Flor': [f'Rosa {i}' for i in range(1, 10)],
            'Valor': [10, 15, 10, 12, 40, 40, 10, 15, 40],
            'Tipo': ['Roja', 'Roja', 'Roja', 'Roja', 'Especial', 'Especial', 'Roja', 'Roja', 'Especial']
        })
        chart_rosas = alt.Chart(data_rosas).mark_bar().encode(x='Flor', y='Valor', color='Tipo')
        st.altair_chart(chart_rosas, use_container_width=True)

elif opcion == "3. Continuidad (El camino del desierto)":
    st.title("🛤️ 3. Ley de la Continuidad: Las huellas en la arena")
    st.write("### 📖 El cuento en las dunas")
    st.write("El Principito recorre el desierto siguiendo líneas fluidas y huellas que guían la mirada de forma natural sin interrupciones abruptas.")
    
    st.markdown("---")
    suavidad = st.slider("Intensidad de la curva del camino:", 1, 10, 5)
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * suavidad
    df_line = pd.DataFrame({'Distancia': x, 'Altura de la duna': y})
    st.line_chart(df_line, x='Distancia', y='Altura de la duna')
    st.info("💡 La línea continua guía los ojos de izquierda a derecha de forma fluida.")

elif opcion == "4. Cierre (La boa y el elefante)":
    st.title("🐘 4. Ley del Cierre: El sombrero o la boa")
    st.write("### 📖 El cuento del dibujo oculto")
    st.write("Los adultos ven un sombrero porque faltan líneas, pero el cerebro de un niño aplica la Ley del Cierre completando la silueta del elefante dentro de la serpiente.")
    
    st.markdown("---")
    completar = st.checkbox("Activar la imaginación infantil (Cerrar la figura)")
    if completar:
        st.success("🐘 ¡Magia! Tu cerebro ha cerrado los trazos incompletos: ¡Es un elefante dentro de una boa!")
    else:
        st.warning("🎩 Se ve un objeto incompleto (parece un sombrero). ¡Falta cerrar el contorno!")

elif opcion == "5. Figura y Fondo (La puesta de sol)":
    st.title("🌅 5. Ley de Figura y Fondo: El atardecer")
    st.write("### 📖 El cuento del atardecer")
    st.write("El sol brillante es la **figura** principal que atrapa la mirada, mientras que el cielo del pequeño planeta actúa como el **fondo** difuminado.")
    
    st.markdown("---")
    opacidad_fondo = st.slider("¿Qué tanto destaca el fondo sobre el sol?", 0.05, 1.0, 0.3)
    
    # Gráfico interactivo estilo minería/paisaje de la referencia
    chart_data = pd.DataFrame({
        'Paso': [f'S{i}' for i in range(1, 6)] * 3,
        'Valor': [20, 35, 30, 50, 45, 10, 20, 15, 25, 30, 60, 55, 50, 65, 70],
        'Elemento': ['Fondo Lejano']*5 + ['Fondo Nublado']*5 + ['Sol (Figura Principal)']*5
    })
    c_fondo = alt.Chart(chart_data).mark_line().encode(
        x='Paso', y='Valor', color=alt.Color('Elemento', scale=alt.Scale(range=['gray', 'lightblue', 'gold']))
    ).properties(height=300)
    st.altair_chart(c_fondo, use_container_width=True)
    st.info(f"Nivel de atención al fondo: {opacidad_fondo}. Cuando el fondo se atenúa, el sol (figura) resalta al instante.")

elif opcion == "6. Simetría (Los volcanes ordenados)":
    st.title("🌋 6. Ley de la Simetría: Los volcanes")
    st.write("### 📖 El cuento de los tres volcanes")
    st.write("El orden simétrico de los volcanes del Principito transmite equilibrio, estabilidad y paz visual inmediata al limpiar su planeta.")
    
    st.markdown("---")
    simetria_nivel = st.selectbox("Estado de orden del planeta:", ["Perfectamente simétrico y ordenado", "Caótico y desordenado"])
    if simetria_nivel == "Perfectamente simétrico y ordenado":
        st.success("⚖️ El planeta se siente equilibrado, limpio y agradable a la vista.")
    else:
        st.error("🌪️ El desorden genera ruido visual y tensión en quien observa.")

elif opcion == "7. Destino Común (Los pájaros migrantes)":
    st.title("🦅 7. Ley de Destino Común: El viaje migratorio")
    st.write("### 📖 El cuento del vuelo")
    st.write("Los pájaros que vuelan en la misma dirección y al mismo tiempo parecen formar parte de un único viaje coordinado hacia otro planeta.")
    
    st.markdown("---")
    direccion = st.radio("Dirección de la bandada:", ["Hacia el Asteroide B612", "Hacia la Tierra", "En direcciones dispersas"])
    if direccion != "En direcciones dispersas":
        st.success(f"🦅 Al moverse juntos **{direccion}**, el cerebro asume que comparten el mismo propósito.")
    else:
        st.warning("⚠️ Sin dirección común, parecen elementos desconectados.")

elif opcion == "🧩 Mini-Quiz Estelar":
    st.title("🧩 Mini-Quiz Interactivo de la Gestalt")
    st.write("Pon a prueba tu aprendizaje con este widget de evaluación:")
    
    respuesta = st.radio("¿Qué ley explica que el sol destaque sobre el cielo oscuro?", ["Ley de Proximidad", "Ley de Figura y Fondo", "Ley del Cierre"])
    if st.button("Evaluar respuesta"):
        if respuesta == "Ley de Figura y Fondo":
            st.success("🎉 ¡Correcto! Separas la figura principal del fondo.")
        else:
            st.error("❌ Inténtalo de nuevo.")
