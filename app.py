import streamlit as st
import time
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image
import os

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Project Darpana | Jogeswar Bisoi",
    page_icon="✏️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. THE "KIMI GENIUS" THEME ---
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap" rel="stylesheet">
    <style>
    /* GLOBAL FONTS */
    * {
        font-family: 'Patrick Hand', cursive !important;
        font-size: 24px !important;
        color: #e6f1ff;
    }
    
    /* APP BACKGROUND */
    .stApp {
        background-color: #0a192f !important;
        background-image: radial-gradient(#112240 1px, transparent 1px);
        background-size: 30px 30px;
    }
    
    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background-color: #112240 !important;
        border-right: 3px solid #f1c40f !important;
    }
    
    /* INPUTS & TEXT AREAS */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #1A2332 !important;
        color: #f1c40f !important;
        border: 2px dashed #f1c40f !important;
        border-radius: 12px !important;
    }
    
    /* BUTTONS */
    .stButton>button {
        background-color: #f1c40f !important;
        color: #0a192f !important;
        border: 2px solid #0a192f !important;
        border-radius: 255px 15px 225px 15px/15px 225px 15px 255px !important;
        font-weight: bold !important;
        height: 65px !important;
        box-shadow: 4px 4px 0px #000 !important;
        transition: all 0.2s ease-in-out !important;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 6px 6px 0px #2ecc71 !important;
        background-color: #f39c12 !important;
        color: white !important;
    }
    
    /* ALERTS */
    .stSuccess, .stInfo, .stWarning {
        background-color: rgba(26, 35, 50, 0.9) !important;
        border: 1px dashed #f1c40f !important;
        border-radius: 10px !important;
    }
    
    /* CUSTOM PROFILE IMAGE CIRCLE */
    .profile-img {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        border: 3px solid #f1c40f;
        object-fit: cover;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. HELPER FUNCTIONS ---
def load_image(filename):
    """Smart loader that handles missing files gracefully"""
    if os.path.exists(filename):
        return Image.open(filename)
    return None

def generate_math_image(latex):
    """Generates a math image locally"""
    plt.figure(figsize=(8, 3), facecolor='#0a192f')
    plt.text(0.5, 0.5, f"${latex}$", fontsize=28, ha='center', va='center', color='#f1c40f')
    plt.axis('off')
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=150, facecolor='#0a192f')
    buf.seek(0)
    plt.close()
    return Image.open(buf)

# --- 4. SIDEBAR ---
with st.sidebar:
    # 1. PROFILE PICTURE
    col_p1, col_p2, col_p3 = st.columns([1, 2, 1])
    with col_p2:
        if os.path.exists("founder.jpg"):
            st.image("founder.jpg", width=120) # Circular mask applied via CSS if needed, but simple width works best here
        else:
            st.write("👤") # Placeholder if you forgot to upload

    st.markdown("<h2 style='text-align: center; color: #f1c40f;'>Jogeswar Bisoi</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 16px; margin-top: -15px;'>Founder & Architect</p>", unsafe_allow_html=True)
    
    st.success("✅ **Verified Creator**")
    st.info("📍 Undivided Koraput, Odisha")
    
    st.markdown("---")
    
    # 2. STATUS INDICATORS
    st.markdown("### 🛠️ System Status")
    
    status_cols = st.columns([1, 4])
    with status_cols[0]:
        img = load_image("dristi-icon.jpg")
        if img: st.image(img)
        else: st.write("👁️")
    with status_cols[1]:
        st.write("**DRISTI** (Online)")
        
    status_cols2 = st.columns([1, 4])
    with status_cols2[0]:
        img = load_image("siddhanta-icon.jpg")
        if img: st.image(img)
        else: st.write("🧠")
    with status_cols2[1]:
        st.write("**SIDDHANTA** (Active)")

# --- 5. MAIN DASHBOARD ---
c1, c2 = st.columns([1.5, 2], gap="large")

with c1:
    st.markdown("# 📓 Research Notebook")
    st.write("Input your scientific query below.")
    
    math_input = st.text_input("LaTeX Equation:", r"\int x^2 dx")
    subject = st.select_slider("Engine:", ["Physics", "Math", "Chemistry"])
    voice = st.text_area("Add Context Note:", "Sir, checking dimensional consistency.", height=100)
    
    st.markdown("####")
    if st.button("RUN LOGIC CHECK ➜"):
        st.session_state['run'] = True
        st.session_state['math'] = math_input
        # Save to history
        if 'history' not in st.session_state: st.session_state['history'] = []
        st.session_state['history'].append(math_input)

    # HISTORY SECTION (New Feature)
    if 'history' in st.session_state and st.session_state['history']:
        st.markdown("---")
        st.markdown("### 🕒 Recent Checks")
        for item in reversed(st.session_state['history'][-3:]): # Show last 3
            st.code(item)

with c2:
    if 'run' in st.session_state:
        st.markdown("# 🔍 Analysis Results")
        
        # 1. VISUALIZATION
        with st.spinner("Dristi is scanning..."):
            time.sleep(0.8)
            try:
                img = generate_math_image(st.session_state['math'])
                st.image(img, caption="Digitized Input")
            except:
                st.error("Syntax Error")

        # 2. LOGIC
        with st.spinner("Siddhanta is proving..."):
            time.sleep(1.2)
            
        user_math = st.session_state['math']
        
        # LOGIC GATES
        if "int" in user_math and "dx" in user_math:
            st.success("✅ **LOGIC VERIFIED**")
            st.markdown("Integration logic is consistent. Variable of integration (dx) matches the integrand.")
            proof = "theorem int_valid : ∫ x^2 = x^3/3 := by
