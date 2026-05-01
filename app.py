import random
import streamlit as st

st.set_page_config(page_title="Palabras Mágicas", page_icon="🌈", layout="centered")

WORDS = [
    {"target": "mamá", "options": ["mamá", "memo", "mima", "mimo"]},
    {"target": "memo", "options": ["mema", "mama", "memo", "mimi"]},
    {"target": "mima", "options": ["mimo", "mima", "mamá", "meme"]},
    {"target": "pato", "options": ["pato", "peta", "pata", "pito"]},
    {"target": "luna", "options": ["lina", "luna", "lana", "lona"]},
]

if "round_index" not in st.session_state:
    st.session_state.round_index = 0
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "feedback_type" not in st.session_state:
    st.session_state.feedback_type = ""
if "order" not in st.session_state:
    st.session_state.order = random.sample(range(4), 4)


def reset_options():
    st.session_state.order = random.sample(range(4), 4)


def next_round():
    st.session_state.round_index = (st.session_state.round_index + 1) % len(WORDS)
    st.session_state.feedback = ""
    st.session_state.feedback_type = ""
    reset_options()


def choose_word(choice: str, target: str):
    if choice == target:
        st.session_state.feedback = f"🎉 ¡Muy bien! Esa era la palabra '{target}'. ¡Excelente trabajo!"
        st.session_state.feedback_type = "success"
    else:
        st.session_state.feedback = (
            f"❌ No, esa palabra significa '{choice}'. Intenta nuevamente y busca la palabra '{target}'."
        )
        st.session_state.feedback_type = "error"


st.markdown(
    """
    <style>
        .main {background: linear-gradient(160deg, #fff2d7, #ffe0f0);}
        h1, h2, h3, p, div, button {font-family: 'Comic Sans MS', 'Nunito', sans-serif !important;}
        .title {text-align: center; color: #8c52ff; font-size: 2.4rem; margin-bottom: 0;}
        .subtitle {text-align: center; font-size: 1.3rem; margin-top: 0;}
        .target {text-align: center; font-size: 3rem; color: #8c52ff; font-weight: 800; margin: 0.4rem 0 1rem;}
        .instruction {text-align: center; font-size: 1.1rem; margin-bottom: 0.4rem;}
        .stars {text-align: center; font-size: 1.6rem; margin-top: 0.8rem;}
        .feedback {font-size: 1.15rem; font-weight: 700; text-align: center; min-height: 3rem; padding: 0.4rem;}
        .success {color: #1ba94c;}
        .error {color: #e74c3c;}
        .stButton > button {width: 100%; border-radius: 14px; font-size: 1.2rem; padding: 0.6rem;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<p class='title'>🌈 Palabras Mágicas</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>¡Aprendamos jugando!</p>", unsafe_allow_html=True)

round_data = WORDS[st.session_state.round_index]
st.markdown("<p class='instruction'>Toca la palabra correcta</p>", unsafe_allow_html=True)
st.markdown(f"<p class='target'>{round_data['target']}</p>", unsafe_allow_html=True)

cols = st.columns(2)
for idx, option_idx in enumerate(st.session_state.order):
    word = round_data["options"][option_idx]
    with cols[idx % 2]:
        st.button(
            word,
            key=f"opt_{idx}_{st.session_state.round_index}",
            on_click=choose_word,
            args=(word, round_data["target"]),
        )

if st.session_state.feedback:
    css_class = "success" if st.session_state.feedback_type == "success" else "error"
    st.markdown(f"<p class='feedback {css_class}'>{st.session_state.feedback}</p>", unsafe_allow_html=True)
else:
    st.markdown("<p class='feedback'>&nbsp;</p>", unsafe_allow_html=True)

st.button("Siguiente palabra", on_click=next_round)
st.markdown("<p class='stars'>⭐ ✨ ⭐ ✨ ⭐</p>", unsafe_allow_html=True)
