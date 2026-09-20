import streamlit as st
import random

#Configuracion inicial de la pagina
st.set_page_config(
    page_title="Para la persona con los cachetitos mas scuichis del mundo mundial<33",
    page_icon="❤️",
    layout="centered"
)

#Titulo y bienvenida
st.title("Bienvenida a nuestro secretito de amor:3")
st.subheader("Con muchisimmo amor hice esta pagina enteramente para ti, nosotros❤️❤️❤️")

st.divider()

#Mensaje principal
st.header("✨Nunca olvides que te amo no importa donde estes ni el tiempo que pase✨")
st.write("Siempre te llevo en mi alma a todos lados, eres la mejor personita del mundo, mi mundo")

#Interaccion 1: Botón con animacion de globos
st.markdown("###🎁 Una sorpresa para ti")
if st.button("Puchale aki para recibir un besote en tus cachetitos hermosos"):
    st.balloons()
    st.success("Muaak! Te mando un besote en tus cachetitos hermosos ❤️")
#Interaccion 2: Razones por las que te amo
st.divider()
st.markdown("¿Por qué este lokote te ama tanto? Aquí van algunas razones:")
razones = [
    "Haces brillar mi alma con solo ver tu sonrisa.",
    "Me pones mas contento que baisa de weed.",
    "Ningun slime se comparan a esos cachetitos tan divinos que tienes.",
    "Escucharte cantar mata todos los demonios de mi coko maniakon.",
    "Me haces sentir mas fuerte que tanke de cri.",
    "Juntos me sale lo warrior, sabes que por ti mato."
]

razon_elegida = "Presiona el botón para ver una razón 💖"

if st.button("Generar una razón aleatoria"):
    razon_elegida = random.choice(razones)

st.info(f"💖 **Razón:** {razon_elegida}")

#Interaccion 3: Medidor de amor
st.divider()
st.markdown("###💖 Medidor de amor  ")
nivel = st.slider("¿Cuánto te amo hoy?", min_value=0, max_value=100000000, value=1000000)

if nivel < 100000000:
     st.warning("Creo te patina el coquito lindo :C, Subele a mil millones!")
else:
    st.success("¡!💖10000000%!¡ Te amo muuuuuuuuuuuuuuuuuuuucho mas que todas las vaquitas del mundo diciendo muuuuu juntas;3 💖")
    