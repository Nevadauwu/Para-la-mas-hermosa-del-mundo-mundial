import streamlit as st
import random

#Configuracion inicial de la pagina
st.set_page_config(
    page_title="Para la persona con los cachetitos mas scuichis del mundo mundial<33",
    page_icon="❤️",
    layout="centered"
)

#Estilo visual
st.markdown("""
    <style> 
    /* Fondo con degradado romántico */
    .stApp {
        background: linear-gradient(135deg, #ffa9a9 0%, #fecfef 50%, #feada6 100%);
    }

    /* Estilo de los títulos */
    h1, h2, h3 {
        color: #b8004f !important;
        font-family: 'Segoe UI', sans-serif;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
    }

    /* Estilo del texto normal */
    p, span, div {
        color: #b8004f !important;
        font-size: 1.05rem;
    }

    /* Botones bonitos y redondeados */
    .stButton > button {
        background-color: #ff4b4b !important;
        color: white !important;
        border-radius: 25px !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.15) !important;
        padding: 10px 24px !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        background-color: #e60039 !important;
    }
    </style>
""", unsafe_allow_html=True)


#Titulo y bienvenida
st.title("Bienvenida a nuestro secretito de amor:3")
st.subheader("Con muchisimmo amor hice esta pagina enteramente para ti, nosotros❤️❤️❤️")

st.divider()

#Mensaje principal
st.header("✨Nunca olvides que te amo no importa donde estes ni el tiempo que pase✨")
st.write("Siempre te llevo en mi alma a todos lados, eres la mejor personita del mundo, mi mundo")

#Interaccion 1: Botón con animacion de globos
st.markdown("### 🎁 Una sorpresa para ti")
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
    "Juntos me sale lo warrior, sabes que por ti mato.",
    "No hay nada mejor en el mundo que despertar acurrucados dandonos calor.",
    "Eres el publico favorito de mi neurona rapera:) ",
    "Mis ojos reviven al verte deslumbrar en este mundo podrido",
    
]
razon_elegida = "Presiona el botón para ver una razón 💖"
if st.button("Generar una razón aleatoria"):
    razon_elegida = random.choice(razones)

st.info(f"💖 **Razón:** {razon_elegida}")


#Razoones por las que deberias hablarme :C (24/09/26)
st.divider()
st.markdown("Por qué deberias comunicarte con este flaco que te ama tanto")
razones2 = [
    "Sin ti mi corazon derrama sangre transmutada en agua.",
    "Osito ya se cansó de ser aplastado, necesita tu relevo :(.",
    "Spoki muere de tristeza como yo esperando saber de tu bienestar.",
    "te amo.",
    "te kero.",
    "te kero y te amo mucho.",
    "Mis dedos sufren sin sentir sus slimes favoritos.",
    "Sin ti spoki se pone bien caliya.",

]

razon_elegida2 = "Nelycita pechocha keo te necesita y aqui hay varias razones :c"
if st.button("por que keito te necesita igual que su corazoncito?"):
    razon_elegida2 = random.choice(razones2)

st.info(f" ***Razón***  {razon_elegida2}")

#Interaccion 3: Medidor de amor
st.divider()
st.markdown("### 💖 Medidor de amor")
nivel = st.slider("¿Cuánto te amo hoy?", min_value=0, max_value=100000000, value=1000000)

if nivel < 100000000:
    st.warning("Creo te patina el coquito lindo :C, Subele a mil millones!")
else:
    st.success("¡!💖10000000%!¡ Te amo muuuuuuuuuuuuuuuuuuuucho mas que todas las vaquitas del mundo diciendo muuuuu juntas;3 💖")
    