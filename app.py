import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="UL Tablero 2026",
    page_icon="📊",
    layout="wide"
)

# -----------------------------------------------------------------------------
# Panel de Control (Sidebar)
# -----------------------------------------------------------------------------
st.sidebar.title("Panel de Control")
st.sidebar.markdown("Selecciona una actividad para visualizar:")

# Definición de las 7 actividades
actividades = [
    "Actividad 1: Resumen General",
    "Actividad 2: Análisis de Datos",
    "Actividad 3: Visualización de Métricas",
    "Actividad 4: Reportes Exportables",
    "Actividad 5: Gestión de Usuarios",
    "Actividad 6: Configuración",
    "Actividad 7: Ayuda y Soporte"
]

opcion_seleccionada = st.sidebar.radio("Navegación", actividades)

# -----------------------------------------------------------------------------
# Contenido Principal (Placeholders)
# -----------------------------------------------------------------------------
st.title(opcion_seleccionada)

if opcion_seleccionada == "Actividad 1: Resumen General":
    st.header("Placeholder - Actividad 1")
    st.info("Aquí irá el contenido principal del resumen general.")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Métrica A")
        st.write("[Placeholder para gráfico o datos]")
    with col2:
        st.subheader("Métrica B")
        st.write("[Placeholder para gráfico o datos]")

elif opcion_seleccionada == "Actividad 2: Análisis de Datos":
    st.header("Placeholder - Actividad 2")
    st.write("Filtros y tablas de datos se ubicarán en esta sección.")
    st.dataframe({"Columna 1": [1, 2, 3], "Columna 2": ["A", "B", "C"]})

elif opcion_seleccionada == "Actividad 3: Visualización de Métricas":
    st.header("Placeholder - Actividad 3")
    st.warning("Sección de gráficos y visualización avanzada.")

elif opcion_seleccionada == "Actividad 4: Reportes Exportables":
    st.header("Placeholder - Actividad 4")
    st.write("Módulo para descarga de reportes.")
    st.button("Descargar Reporte (Ejemplo)")

elif opcion_seleccionada == "Actividad 5: Gestión de Usuarios":
    st.header("Placeholder - Actividad 5")
    st.write("Panel de administración de usuarios y permisos.")

elif opcion_seleccionada == "Actividad 6: Configuración":
    st.header("Placeholder - Actividad 6")
    st.write("Ajustes y parámetros de la aplicación.")

elif opcion_seleccionada == "Actividad 7: Ayuda y Soporte":
    st.header("Placeholder - Actividad 7")
    st.write("Documentación y canales de soporte.")
