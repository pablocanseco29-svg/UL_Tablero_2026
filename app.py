import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# -----------------------------------------------------------------------------
# Configuración de la página y Estilo Estelar (CSS Personalizado)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="El Principito y los Secretos de la Mente",
    page_icon="✨",
    layout="wide"
)

# Inyectamos estilos CSS para darle una apariencia de cielo nocturno estelar y moderna
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #f0f2f6;
    }
    .sidebar .stRadio label {
        color: #f0f2f6;
        font-weight: 500;
    }
    .stAlert {
        background-color: #1a2238;
        color: #ffffff;
        border: 1px solid #3b82f6;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Panel de Control (Sidebar)
# -----------------------------------------------------------------------------
st.sidebar.title("🪐 Planeta B612")
st.sidebar.markdown("### Navegación Estelar")

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
# Contenido Principal con Storytelling y Widgets Interactivos
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
            color=alt.Color('Constelación', scale=alt.Scale(range=['#ffd700', '#00d2ff']))
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
            color=alt.Color('Tipo', scale=alt.Scale(range=['#ff4b4b', '#ffd700']))
        ).properties(height=280)
        st.altair_chart(chart_rosas, use_container_width=True)

elif opcion == "3. Continuidad (El camino del desierto)":
    st.title("🛤️ 3. Ley de la Continuidad: Las huellas en la arena")
    st.write("### 📖 El cuento en las dunas")
    st.write("El Principito recorre el desierto siguiendo líneas fluidas y huellas luminosas que guían la mirada de forma natural sin interrupciones abruptas hacia el horizonte.")
    
    st.markdown("---")
    col1,
