import streamlit as st
import openai

API_KEY = st.secrets["API_KEY"]

st.title("Generador de Plan de Dieta Personalizado")

# Inputs del usuario
peso = st.number_input("Peso (kg):", min_value=0.0)
altura = st.number_input("Altura (cm):", min_value=0.0)
edad = st.number_input("Edad:", min_value=0)
genero = st.selectbox("Género:", ["Masculino", "Femenino", "Otro"])
objetivos_personales = st.text_input("Objetivos Personales:")
restricciones_alimentarias = st.text_input("Restricciones Alimentarias:")
actividad_fisica = st.selectbox(
    "Nivel de Actividad Física:",
    ["Sedentario", "Ligeramente Activo", "Moderadamente Activo", "Muy Activo", "Extra Activo"],
)

# Botón para generar el plan de dieta
if st.button("Generar Plan de Dieta"):
    # Clave de API de OpenAI
    openai.api_key = API_KEY

    # Construir el prompt
    prompt = f"""
    Genera un plan de dieta detallado para una persona con las siguientes características:
    Peso: {peso} kg
    Altura: {altura} cm
    Edad: {edad} años
    Género: {genero}
    Objetivos Personales: {objetivos_personales}
    Restricciones Alimentarias: {restricciones_alimentarias}
    Nivel de Actividad Física: {actividad_fisica}

    Incluye detalles como:
    - Desglose de macronutrientes (proteína, carbohidratos, grasas)
    - Ejemplos de planes de comidas para cada día
    - Recetas específicas para algunas comidas
    - Otra información relevante para una dieta saludable y efectiva.
    """

    # Llamar a la API de OpenAI
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.7,
        )

        plan_de_dieta = response.choices[0].message.content.strip()
        st.subheader("Plan de Dieta:")
        st.write(plan_de_dieta)

    except Exception as e:
        st.error(f"Ocurrió un error: {e}")
