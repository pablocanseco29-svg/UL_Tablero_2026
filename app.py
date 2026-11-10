import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# -----------------------------------------------------------------------------
# Configuración de la página y Estilo Lunar (CSS Personalizado)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="El Principito y los Secretos de la Mente",
    page_icon="🌕",
    layout="wide"
)

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1b1f24 0%, #0d1117 100%);
        color: #e2e8f0;
    }
    .sidebar .stRadio label {
        color: #e2e8f0;
        font-weight: 500;
    }
    .stAlert {
        background-color: #262d37;
        color: #ffffff;
        border: 1px solid #64748b;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Panel de Control (Sidebar)
# -----------------------------------------------------------------------------
st.sidebar.title("🌕 Asteroide B612")
st.sidebar.markdown("### Panel de Navegación Lunar")

opcion = st.sidebar.radio(
    "Elige un principio visual:",
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
    st.write("Cuando el Principito observa el cielo nocturno de su asteroide, las estrellas que están cerca unas de otras forman constelaciones brillantes ante sus ojos. El cerebro las agrupa de inmediato.")
    st.markdown("---")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("#### 🎛️ Control interactivo de cercanía")
        distancia = st.slider("Ajusta la separación visual entre estrellas:", 1.0, 10.0, 2.0, 0.5)
        st.info(f"💡 Con una separación de **{distancia}**, tu mente decide si forman un grupo estelar o están aisladas.")
    with col2:
        st.markdown("#### 📊 Constelación en tiempo real")
        chart_data = pd.DataFrame({
            'x': [1, 1.5 + (distancia*0.1), 5, 5.5 + (distancia*0.1)],
            'y': [1, 1.2, 5, 5.3],
            'Constelación': ['Grupo Alfa', 'Grupo Alfa', 'Grupo Beta', 'Grupo Beta']
        })
        c = alt.Chart(chart_data).mark_circle(size=300).encode(
            x='x', y='y', 
            color=alt.Color('Constelación', scale=alt.Scale(range=['#facc15', '#38bdf8']))
        ).properties(height=280)
        st.altair_chart(c, use_container_width=True)

elif opcion == "2. Semejanza (El jardín de rosas)":
    st.title("🌹 2. Ley de la Semejanza: Las 5,000 rosas")
    st.write("### 📖 El cuento en el jardín")
    st.write("Ante miles de rosas idénticas en la Tierra, el Principito nota que el cerebro agrupa automáticamente aquellas que comparten el mismo color vibrante y la misma forma como un solo equipo.")
    st.markdown("---")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("#### 🎛️ Selector de similitud de color")
        color_filtro = st.selectbox("Elige qué grupo destacar en el jardín:", ["Todas las rosas", "Solo Rojas Encendidas", "Solo Doradas Mágicas"])
        st.success(f"Filtro aplicado: **{color_filtro}**. Tu mente separa por color de inmediato.")
    with col2:
        st.markdown("#### 📊 Análisis visual de flores")
        data_rosas = pd.DataFrame({
            'Flor': [f'Rosa {i}' for i in range(1, 10)],
            'Intensidad': [12, 18, 12, 15, 45, 45, 12, 18, 45],
            'Tipo': ['Roja', 'Roja', 'Roja', 'Roja', 'Especial', 'Especial', 'Roja', 'Roja', 'Especial']
        })
        chart_rosas = alt.Chart(data_rosas).mark_bar(cornerRadius=8).encode(
            x='Flor', y='Intensidad',
            color=alt.Color('Tipo', scale=alt.Scale(range=['#f43f5e', '#facc15']))
        ).properties(height=280)
        st.altair_chart(chart_rosas, use_container_width=True)

elif opcion == "3. Continuidad (El camino del desierto)":
    st.title("🛤️ 3. Ley de la Continuidad: Las huellas en la arena")
    st.write("### 📖 El cuento en las dunas")
    st.write("El Principito recorre el desierto siguiendo líneas fluidas y huellas luminosas que guían la mirada de forma natural sin interrupciones abruptas hacia el horizonte.")
    st.markdown("---")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("#### 🎛️ Control de fluidez")
        suavidad = st.slider("Intensidad de la curva del camino:", 1, 10, 5)
        st.info("💡 La línea continua guía los ojos con una trayectoria fluida y sin tropiezos.")
    with col2:
        st.markdown("#### 📊 Trayectoria en las dunas")
        x = np.linspace(0, 10, 100)
        y = np.sin(x) * suavidad
        df_line = pd.DataFrame({'Distancia': x, 'Altura': y})
        chart_line = alt.Chart(df_line).mark_line(strokeWidth=4, color='#38bdf8').encode(x='Distancia', y='Altura').properties(height=250)
        st.altair_chart(chart_line, use_container_width=True)

elif opcion == "4. Cierre (La boa y el elefante)":
    st.title("🐘 4. Ley del Cierre: El sombrero o la boa")
    st.write("### 📖 El cuento del dibujo oculto")
    st.write("Los adultos ven un sombrero porque faltan líneas, pero el cerebro de un niño aplica la Ley del Cierre completando la silueta mágica del elefante dentro de la serpiente.")
    st.markdown("---")
    completar = st.checkbox("🪄 Activar la imaginación infantil (Cerrar la figura mentalmente)")
    if completar:
        st.success("🐘 **¡Magia estelar!** Tu cerebro ha completado los trazos incompletos: ¡Es un elefante descansando dentro de una boa!")
    else:
        st.warning("🎩 Se percibe un objeto incompleto (parece un simple sombrero). ¡Falta cerrar el contorno mental!")

elif opcion == "5. Figura y Fondo (La puesta de sol)":
    st.title("🌅 5. Ley de Figura y Fondo: El atardecer")
    st.write("### 📖 El cuento del atardecer")
    st.write("El sol brillante de oro es la **figura** principal que atrapa toda la atención, mientras que el cielo del pequeño planeta actúa como el **fondo** difuminado.")
    st.markdown("---")
    opacidad_fondo = st.slider("Atenuación del fondo lunar:", 0.05, 1.0, 0.3)
    chart_data = pd.DataFrame({
        'Paso': [f'Momento {i}' for i in range(1, 6)] * 2,
        'Brillo': [15, 30, 25, 45, 40, 70, 85, 80, 95, 100],
        'Capa': ['Fondo Lunar (Secundario)']*5 + ['Sol Radiante (Figura Principal)']*5
    })
    chart_fondo = alt.Chart(chart_data).mark_line(strokeWidth=4).encode(
        x='Paso', y='Brillo',
        color=alt.Color('Capa', scale=alt.Scale(range=['#64748b', '#facc15']))
    ).properties(height=280)
    st.altair_chart(chart_fondo, use_container_width=True)
    st.info(f"Nivel de contraste del fondo: {opacidad_fondo}. Al atenuar el fondo, el sol (figura) destaca con fuerza.")

elif opcion == "6. Simetría (Los volcanes ordenados)":
    st.title("🌋 6. Ley de la Simetría: Los volcanes")
    st.write("### 📖 El cuento de los tres volcanes")
    st.write("El orden simétrico de los volcanes del Principito transmite equilibrio, estabilidad y paz visual inmediata al limpiar su planeta cada mañana.")
    st.markdown("---")
    simetria_nivel = st.selectbox("Estado de orden del asteroide:", ["Perfectamente simétrico y equilibrado", "Caótico y desordenado"])
    if simetria_nivel == "Perfectamente simétrico y equilibrado":
        st.success("⚖️ **Armonía visual:** El planeta se siente ordenado, limpio y sumamente agradable a la vista.")
    else:
        st.error("🌪️ **Ruido visual:** El desorden genera tensión y desequilibrio en quien observa.")

elif opcion == "7. Destino Común (Los pájaros migrantes)":
    st.title("🦅 7. Ley de Destino Común: El viaje migratorio")
    st.write("### 📖 El cuento del vuelo")
    st.write("Los pájaros silvestres que vuelan en la misma dirección y al mismo tiempo parecen formar parte de un único viaje coordinado hacia las estrellas.")
    st.markdown("---")
    direccion = st.radio("Destino de la bandada estelar:", ["Hacia el Asteroide B612", "Hacia la Tierra", "En direcciones dispersas y rotas"])
    if direccion != "En direcciones dispersas y rotas":
        st.success(f"🦅 Al moverse juntos hacia **{direccion}**, el cerebro asume instantáneamente que comparten un propósito común.")
    else:
        st.warning("⚠️ Sin un destino común, los elementos se perciben desconectados y sin rumbo.")

elif opcion == "🧩 Mini-Quiz Estelar":
    st.title("🧩 Mini-Quiz Interactivo de la Gestalt")
    st.write("Pon a prueba tu aprendizaje con este widget de evaluación lunar:")
    respuesta = st.radio("¿Qué principio visual explica que el sol radiante destaque de inmediato sobre el cielo oscuro?", ["Ley de Proximidad", "Ley de Figura y Fondo", "Ley del Cierre"])
    if st.button("✨ Evaluar respuesta lunar"):
        if respuesta == "Ley de Figura y Fondo":
            st.success("🎉 ¡Excelente respuesta! Comprendiste cómo separar la figura principal del fondo.")
        else:
            st.error("❌ ¡Casi! Vuelve a revisar la sección de Figura y Fondo.")
