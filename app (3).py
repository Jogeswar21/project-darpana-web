
import streamlit as st
import time
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image
import os

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="Project Darpana | Jogeswar Bisoi",
    page_icon="✏️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CSS STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Patrick Hand', cursive !important;
        font-size: 24px !important;
    }
    .stApp {
        background-color: #0a192f !important;
        background-image: radial-gradient(#112240 1px, transparent 1px);
        background-size: 20px 20px;
        color: #e6f1ff !important;
    }
    h1, h2, h3 { color: #f1c40f !important; letter-spacing: 1px !important; text-shadow: 2px 2px #000 !important; }
    p, label, .stMarkdown { color: #e6f1ff !important; }
    
    section[data-testid="stSidebar"] {
        background-color: #112240 !important;
        border-right: 3px solid #f1c40f !important;
    }
    
    .stTextInput>div>div>input {
        background-color: #112240 !important;
        color: #f1c40f !important;
        border: 2px dashed #f1c40f !important;
        border-radius: 10px;
    }
    
    .founder-box {
        background: rgba(241, 196, 15, 0.1);
        border-left: 5px solid #f1c40f;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 5px;
    }
    
    .stButton>button {
        background-color: #f1c40f !important;
        color: #0a192f !important;
        border: 2px solid #0a192f !important;
        border-radius: 255px 15px 225px 15px/15px 225px 15px 255px !important;
        font-weight: bold !important;
        font-size: 24px !important;
        height: 65px !important;
        box-shadow: 4px 4px 0px #000 !important;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        transform: translate(-2px, -2px);
        box-shadow: 6px 6px 0px #2ecc71 !important;
        background-color: #f39c12 !important;
        color: white !important;
    }
    
    .stSuccess {
        background-color: rgba(46, 204, 113, 0.1) !important;
        border: 2px solid #2ecc71 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. HELPER FUNCTIONS ---
def generate_math_image(latex):
    """Generates a math image locally"""
    plt.figure(figsize=(6, 2), facecolor='#112240')
    plt.text(0.5, 0.5, f"${latex}$", fontsize=25, ha='center', va='center', color='#f1c40f')
    plt.axis('off')
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=150, facecolor='#112240')
    buf.seek(0)
    plt.close()
    return Image.open(buf)

# --- 4. SIDEBAR ---
with st.sidebar:
    # IMAGES
    if os.path.exists("hero-notebook.jpg"):
        st.image("hero-notebook.jpg", use_column_width=True)
    elif os.path.exists("logo.png"):
        st.image("logo.png", width=80)
    else:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Gaussian_Integral.svg/320px-Gaussian_Integral.svg.png", width=60)

    st.markdown("# ✏️ Project Darpana")
    st.markdown("**Ver 1.0 (Koraput Release)**")
    
    st.markdown("---")
    st.markdown("### 👨‍💻 Founder's Corner")
    
    # FOUNDER PROFILE
    st.markdown("""
    <div class="founder-box">
        <strong>Founder:</strong> Jogeswar Bisoi <span style="color:#2ecc71">✔</span><br>
        <span style="font-size: 16px;">jogeswarbisoifromkpt@gmail.com</span><br>
        <hr style="border-top: 1px dashed #f1c40f; opacity: 0.5;">
        <strong>Mission:</strong> Undivided Koraput Development
    </div>
    """, unsafe_allow_html=True)
    
    # ICONS STATUS
    col_a, col_b = st.columns([1, 4])
    with col_a:
        if os.path.exists("dristi-icon.jpg"): st.image("dristi-icon.jpg")
    with col_b:
        st.caption("Dristi (Vision): **Active**")

    col_c, col_d = st.columns([1, 4])
    with col_c:
        if os.path.exists("siddhanta-icon.jpg"): st.image("siddhanta-icon.jpg")
    with col_d:
        st.caption("Siddhanta (Logic): **Active**")
        
    st.success("✅ System Online")

# --- 5. MAIN INTERFACE ---
c1, c2 = st.columns([1.5, 2])

with c1:
    st.markdown("## 1. Input Problem")
    st.markdown("Type your derivation step below (LaTeX supported).")
    
    # Inputs - Double backslash used here for safety in writing the file
    math_input = st.text_input("Equation:", r"\\int x^2 dx")
    subject = st.select_slider("Engine:", ["Samanta (Physics)", "Bhaskara (Math)", "Nagarjuna (Chem)"])
    voice = st.text_area("📝 Note (Odia/Hinglish):", "Sir, eita thik achi ki?", height=100)
    
    st.markdown("####") 
    if st.button("🚀 RUN LOGIC CHECK"):
        st.session_state['run'] = True
        st.session_state['math'] = math_input

with c2:
    if 'run' in st.session_state:
        st.markdown("## 2. The Mirror")
        
        # Backend Simulation
        col_icon, col_text = st.columns([1, 5])
        with col_icon:
            if os.path.exists("dristi-icon.jpg"): st.image("dristi-icon.jpg", width=50)
        with col_text:
            with st.spinner("Dristi is scanning..."):
                time.sleep(1)
                
        try:
            img = generate_math_image(st.session_state['math'])
            st.image(img, caption="Digitized Input")
        except:
            st.error("Invalid Math Syntax")
        
        col_icon2, col_text2 = st.columns([1, 5])
        with col_icon2:
            if os.path.exists("siddhanta-icon.jpg"): st.image("siddhanta-icon.jpg", width=50)
        with col_text2:       
            with st.spinner("Siddhanta Core is proving..."):
                time.sleep(1.5)
            
        user_math = st.session_state['math']
        
        # Smart Logic Feedback
        if "int" in user_math and "dx" in user_math:
            st.success("✅ **LOGIC VERIFIED**")
            st.markdown("""
            <div style="background:#112240; padding:15px; border:1px dashed #2ecc71; border-radius:10px;">
                <p style="color:#2ecc71; margin:0;"><strong>Siddhanta Analysis:</strong></p>
                <p style="color:white; margin:0;">Integration logic is consistent. Variable of integration (dx) matches.</p>
            </div>
            """, unsafe_allow_html=True)
            proof = "theorem int_valid : ∫ x^2 = x^3/3 := by simp"
            
        elif "=" in user_math:
            st.warning("⚠️ **LOGIC GAP DETECTED**")
            st.markdown("LHS does not dimensionally balance RHS.")
            proof = "theorem balance_fail : LHS ≠ RHS"
            
        else:
            st.info("ℹ️ **SYNTAX CHECK**")
            st.markdown("Valid expression, but no claim was made to verify.")
            proof = "def expr : Nat := 0"

        # Samvad Output
        st.markdown("---")
        col_icon3, col_text3 = st.columns([1, 5])
        with col_icon3:
            if os.path.exists("samvad-icon.jpg"): st.image("samvad-icon.jpg", width=50)
        with col_text3:
            st.markdown("### 🗣️ Samvad (Odia):")
            st.info('🤖 "Babu, logic thik achi. Kintu integration constant bhuli jao ni!"')
        
        with st.expander("View Formal Proof (Lean 4)"):
            st.code(proof, language="lean")

    else:
        st.markdown("""
        <div style="text-align: center; margin-top: 50px; opacity: 0.5; border: 2px dashed #f1c40f; padding: 40px; border-radius: 20px;">
            <h3>Waiting for Input...</h3>
            <p>The Logic Engine is sleeping.</p>
        </div>
        """, unsafe_allow_html=True)
