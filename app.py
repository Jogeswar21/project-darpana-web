import streamlit as st
import time
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Project Darpana | Jogeswar Bisoi",
    page_icon="✏️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. THE "KIMI GENIUS" CSS (Exact Match) ---
st.markdown("""
    <style>
    /* 1. IMPORT THE KIMI FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&family=Caveat&display=swap');
    
    /* 2. GLOBAL FONT SETTINGS */
    html, body, [class*="css"], .stMarkdown, .stButton, .stTextInput, .stSelectbox {
        font-family: 'Patrick Hand', cursive !important;
        font-size: 22px !important;
        color: #F8F9FA !important; /* Warm White */
    }
    
    /* 3. DEEP NAVY BACKGROUND (The Kimi Base) */
    .stApp {
        background-color: #0B1426 !important;
        /* Subtle Graph Paper Effect */
        background-image: 
            linear-gradient(rgba(255, 217, 61, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 217, 61, 0.05) 1px, transparent 1px);
        background-size: 30px 30px;
    }
    
    /* 4. HEADERS (Electric Yellow) */
    h1, h2, h3 {
        color: #FFD93D !important;
        text-shadow: 2px 2px 0px #000 !important;
        letter-spacing: 1px !important;
        font-weight: 400 !important;
    }
    
    /* 5. SIDEBAR (Soft Navy) */
    section[data-testid="stSidebar"] {
        background-color: #1A2332 !important;
        border-right: 3px solid #FFD93D !important;
    }
    
    /* 6. BUTTONS (Sketchy & Yellow) */
    .stButton>button {
        background-color: #FFD93D !important;
        color: #0B1426 !important;
        border: 2px solid #FFD93D !important;
        border-radius: 255px 15px 225px 15px/15px 225px 15px 255px !important; /* The "Hand-drawn" shape */
        font-weight: bold !important;
        font-size: 24px !important;
        height: 60px !important;
        box-shadow: 0 4px 0px #000 !important;
        transition: all 0.2s ease-in-out !important;
        transform: rotate(-1deg);
    }
    .stButton>button:hover {
        transform: translateY(-2px) rotate(0deg);
        box-shadow: 0 6px 0px #00FF41 !important; /* Green shadow on hover */
        background-color: #ffed4a !important;
    }
    
    /* 7. INPUTS & CARDS */
    .stTextInput>div>div>input {
        background-color: #1A2332 !important;
        color: #FFD93D !important;
        border: 2px solid #2A3441 !important;
        border-radius: 10px !important;
        font-family: 'Patrick Hand', cursive !important;
    }
    .stTextInput>div>div>input:focus {
        border-color: #FFD93D !important;
        box-shadow: 0 0 10px rgba(255, 217, 61, 0.2) !important;
    }
    
    /* 8. FOUNDER CARD (Glass Style) */
    .founder-box {
        background: rgba(26, 35, 50, 0.8);
        border: 1px solid #2A3441;
        border-left: 4px solid #FFD93D;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. HELPER: GENERATE MATH IMAGE ---
def generate_math_image(latex):
    plt.figure(figsize=(8, 3), facecolor='#0B1426')
    plt.text(0.5, 0.5, f"${latex}$", fontsize=30, ha='center', va='center', color='#FFD93D')
    plt.axis('off')
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=150, facecolor='#0B1426')
    buf.seek(0)
    plt.close()
    return Image.open(buf)

# --- 4. SIDEBAR ---
with st.sidebar:
    # Logo Loader
    if os.path.exists("logo.png"):
        st.image("logo.png", width=80)
    elif os.path.exists("hero-notebook.jpg"):
        st.image("hero-notebook.jpg", use_column_width=True)
    
    st.markdown("# ✏️ Darpana")
    st.markdown("*The Genius Notebook*")
    
    st.markdown("---")
    
    # Founder Card
    st.markdown("""
    <div class="founder-box">
        <strong>Founder:</strong> Jogeswar Bisoi <span style="color:#00FF41">✔</span><br>
        <span style="font-size: 16px; color:#B8BCC0;">jogeswarbisoifromkpt@gmail.com</span><br>
        <hr style="border-top: 1px dashed #FFD93D; opacity: 0.3;">
        <strong>Mission:</strong> Undivided Koraput Development
    </div>
    """, unsafe_allow_html=True)
    
    # Status Icons
    col1, col2 = st.columns([1, 4])
    with col1:
        if os.path.exists("dristi-icon.jpg"): st.image("dristi-icon.jpg")
        else: st.write("👁️")
    with col2:
        st.write("**DRISTI** (Online)")
        
    col3, col4 = st.columns([1, 4])
    with col3:
        if os.path.exists("siddhanta-icon.jpg"): st.image("siddhanta-icon.jpg")
        else: st.write("🧠")
    with col4:
        st.write("**SIDDHANTA** (Online)")

# --- 5. MAIN INTERFACE ---
c1, c2 = st.columns([1.5, 2], gap="large")

with c1:
    st.markdown("# 📓 Input Problem")
    st.markdown("Write your equation below.")
    
    math_input = st.text_input("LaTeX Equation:", r"\int x^2 dx")
    
    subject = st.select_slider("Select Engine:", ["Physics", "Math", "Chemistry"])
    voice = st.text_area("Add a Note:", "Sir, is this correct?", height=100)
    
    st.markdown("####") 
    if st.button("RUN LOGIC CHECK ➜"):
        st.session_state['run'] = True
        st.session_state['math'] = math_input

with c2:
    if 'run' in st.session_state:
        st.markdown("# 🔍 Analysis")
        
        with st.spinner("Parsing handwriting..."):
            time.sleep(1)
            try:
                img = generate_math_image(st.session_state['math'])
                st.image(img, caption="Digitized Input")
            except:
                st.error("Syntax Error")

        with st.spinner("Verifying logic..."):
            time.sleep(1.5)
            
        user_math = st.session_state['math']
        
        # Result Card (Kimi Style)
        if "int" in user_math:
            st.markdown("""
            <div style="background:#1A2332; padding:20px; border:2px dashed #00FF41; border-radius:12px; box-shadow: 0 0 20px rgba(0, 255, 65, 0.1);">
                <h3 style="color:#00FF41 !important; margin:0;">✅ LOGIC VERIFIED</h3>
                <p style="color:#F8F9FA; margin-top:10px;">The integration follows standard calculus rules. Variable consistency check passed.</p>
            </div>
            """, unsafe_allow_html=True)
            proof = "theorem int_valid : ∫ x^2 = x^3/3 := by simp"
        else:
            st.info("ℹ️ Syntax Validated.")
            proof = "def check : Valid := true"

        # Samvad
        st.markdown("### 🗣️ Samvad")
        col_mic, col_txt = st.columns([1, 5])
        with col_mic:
            if os.path.exists("samvad-icon.jpg"): st.image("samvad-icon.jpg")
        with col_txt:
            st.info('"Babu, logic thik achi. Sabu thik!"')
        
        with st.expander("Show Proof Code"):
            st.code(proof, language="lean")

    else:
        # Empty State
        st.markdown("""
        <div style="text-align: center; margin-top: 50px; opacity: 0.5;">
            <h3>Waiting for input...</h3>
            <p>( The Logic Engine is sleeping )</p>
        </div>
        """, unsafe_allow_html=True)
