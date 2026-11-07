import random
import streamlit as st

st.set_page_config(
    page_title="A Little Guess of Luck 🐰",
    page_icon="🐰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');
:root { --lavender:#eee5ff; --purple:#8f65bd; --deep:#563b78; --pink:#f6dce9; }
.stApp {
    background: radial-gradient(ellipse at top left, #f8e8f5 0%, transparent 45%),
                linear-gradient(135deg, #f4edff 0%, #fff3f7 52%, #eee7ff 100%);
    color: var(--deep);
    font-family: 'Nunito', sans-serif;
}
.block-container { max-width: 1100px; padding-top: 2rem; }
h1, h2, h3, p, label, .stMarkdown { color: var(--deep); font-family: 'Nunito', sans-serif; }
.hero { text-align:center; padding: 1.5rem 1rem .6rem; }
.hero h1 { font-size: clamp(2.2rem, 5vw, 3.8rem); font-weight: 800; margin-bottom: .2rem; }
.hero p { font-size: 1.15rem; color: #80649e; }
.bunny { font-size: 5.5rem; text-align:center; filter: drop-shadow(0 8px 10px #d8c1e8); }
.panel {
    background: rgba(255,255,255,.76); border: 2px solid #e3d1f4;
    border-radius: 28px; padding: 1.6rem; box-shadow: 0 8px 24px rgba(126,85,160,.10);
}
div[data-testid="stNumberInput"] input {
    background: #fffaff; border: 2px solid #d7bde9; border-radius: 16px;
    color: #563b78; font-weight: 700;
}
.stButton button {
    border: 0; border-radius: 18px; padding: .65rem 1.2rem;
    background: linear-gradient(135deg,#b18ad8,#8c62b8); color: white;
    font-weight: 800; box-shadow: 0 5px 0 #76509e; transition: transform .15s;
}
.stButton button:hover { color:white; transform: translateY(-2px); }
div[data-testid="stMetric"] {
    background:#fff8ff; border:1px solid #e8d7f5; padding: .8rem; border-radius: 18px;
}
div[data-testid="stAlert"] { border-radius: 18px; }
footer { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.history = []
    st.session_state.message = "I've picked a number between 1 and 100. Can you find it? ✨"
    st.session_state.won = False

st.markdown('<div class="hero"><h1>💗 A Little Guess of Luck 💗</h1><p>A tiny cozy game from my coding journey</p></div>', unsafe_allow_html=True)

left, center, right = st.columns([1, 2, 1], gap="large")
with left:
    st.markdown('<div class="bunny">🐰</div>', unsafe_allow_html=True)
    st.markdown('<div class="panel"><h3>🌷 How to play</h3><p>Pick a number from 1 to 100.</p><p>I\'ll give you sweet little hints after each guess.</p><p>Keep going until you find it!</p></div>', unsafe_allow_html=True)

with center:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.subheader("🌙 Your guessing nook")
    st.write(st.session_state.message)
    guess = st.number_input("Your guess", min_value=1, max_value=100, step=1, value=50, disabled=st.session_state.won, key="guess_input")
    submit_col, reset_col = st.columns(2)
    with submit_col:
        submitted = st.button("Make a guess ✨", use_container_width=True, disabled=st.session_state.won)
    with reset_col:
        restart = st.button("New round 💜", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if submitted:
        st.session_state.attempts += 1
        difference = abs(st.session_state.secret - int(guess))
        if guess == st.session_state.secret:
            st.session_state.won = True
            st.session_state.message = f"🎉 You found it! The secret number was {st.session_state.secret}. You did it in {st.session_state.attempts} guesses!"
            st.balloons()
        elif guess < st.session_state.secret:
            warmth = "You're so close! 💖" if difference <= 5 else ("Getting warmer! 🌸" if difference <= 15 else "A little chilly—try higher! ☁️")
            st.session_state.message = f"⬆️ A little higher! {warmth}"
        else:
            warmth = "You're so close! 💖" if difference <= 5 else ("Getting warmer! 🌸" if difference <= 15 else "A little chilly—try lower! ☁️")
            st.session_state.message = f"⬇️ A little lower! {warmth}"
        st.session_state.history.append(int(guess))
        st.rerun()

    if restart:
        st.session_state.secret = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.history = []
        st.session_state.message = "A fresh number is ready! Can you find it? ✨"
        st.session_state.won = False
        st.rerun()

with right:
    st.markdown('<div class="panel"><h3>🎀 Game stats</h3>', unsafe_allow_html=True)
    st.metric("Guesses made", st.session_state.attempts)
    st.metric("Numbers tried", len(set(st.session_state.history)))
    st.write("**Your guess trail**")
    if st.session_state.history:
        st.write(" · ".join(map(str, st.session_state.history)))
    else:
        st.write("Your little trail will appear here 💌")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center;color:#9b80b5;margin-top:2rem'>Made with a little nostalgia & lots of 💜</p>", unsafe_allow_html=True)
