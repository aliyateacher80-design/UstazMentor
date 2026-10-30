import streamlit as st

st.set_page_config(page_title="StudySync - UstazMentor", page_icon="💻", layout="wide")

# Session state баптаулары
if "classes_list" not in st.session_state:
    st.session_state.classes_list = ["5 «А»", "5 «Ә»"]

if "results_db" not in st.session_state:
    st.session_state.results_db = [
        {"name": "Жайнарбек А.", "grade": "5 «Ә»", "topic": "1. Эргономика дегеніміз не", "score": "10 / 10 ұпай"}
    ]

# StudySync (Dark Glassmorphism UI) CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [data-testid="stAppViewContainer"], .stApp {
    background: #060913 !important;
    background-image: 
        radial-gradient(at 0% 0%, rgba(14, 165, 233, 0.18) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(99, 102, 241, 0.18) 0px, transparent 50%) !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    color: #f1f5f9 !important;
}

[data-testid="stHeader"] { display: none !important; }

/* Сол жақ панель (Sidebar) стилі суреттегідей */
[data-testid="stSidebar"] {
    background-color: #090d16 !important;
    border-right: 1px solid rgba(56, 189, 248, 0.2) !important;
}

/* Карточкалар мен панельдер */
.study-card {
    background: rgba(15, 23, 42, 0.75) !important;
    backdrop-filter: blur(16px);
    border: 1px solid rgba(56, 189, 248, 0.25);
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
    margin-bottom: 20px;
}

h1, h2, h3, h4, p, span, label, [data-testid="stWidgetLabel"] {
    color: #f8fafc !important;
    font-weight: 600 !important;
}

.stTextInput input, .stSelectbox [data-baseweb="select"] > div {
    background-color: rgba(30, 41, 59, 0.8) !important;
    border: 1px solid rgba(56, 189, 248, 0.3) !important;
    border-radius: 12px !important;
    color: #ffffff !important;
}

.stButton > button {
    background: linear-gradient(135deg, #0284c7 0%, #6366f1 100%) !important;
    border: none;
    border-radius: 12px;
    color: white;
    font-weight: 700;
    box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);
}
</style>
""", unsafe_allow_html=True)

# ----------------- БҮЙІРЛІК МӘЗІР (Sidebar - Суреттің сол жақ бөлігі) -----------------
with st.sidebar:
    st.markdown("### 🟦 **StudySync**")
    st.caption("AI-Powered Learning Platform")
    st.divider()
    
    menu_choice = st.radio("Мәзір:", [
        "📊 Dashboard", 
        "📁 AI Document Analysis", 
        "📝 Quiz Generation", 
        "💡 AI Summaries", 
        "📈 Learning Analytics",
        "⚙️ Settings"
    ])
    
    st.divider()
    role = st.radio("Режим:", ["👨‍🎓 Оқушы режимі", "👩‍🏫 Мұғалім кабинеті"])

# ----------------- БАСТЫ БӨЛІМ (Dashboard - Суреттің оң жақ бөлігі) -----------------
if role == "👩‍🏫 Мұғалім кабинеті":
    st.markdown("""
        <div class="study-card">
            <h2>Welcome back, Устаз! 👋</h2>
            <p style="color: #38bdf8 !important;">Бүгін оқушыларға қандай тапсырма жүктегіңіз келеді?</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class="study-card">
                <h4>📂 Upload & Learn</h4>
                <p style="font-size: 13px; color: #94a3b8 !important;">Материалдарды жүктеп, талдау жасаңыз.</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="study-card">
                <h4>🤖 AI Tutor</h4>
                <p style="font-size: 13px; color: #94a3b8 !important;">Сұрақтарға жауап алып, тест құрыңыз.</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="study-card">
                <h4>📊 Analytics</h4>
                <p style="font-size: 13px; color: #94a3b8 !important;">Оқушылардың прогресін бақылаңыз.</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.subheader("⚙️ Сынып және тақырып баптаулары")
    selected_class = st.selectbox("Сыныпты таңдаңыз:", st.session_state.classes_list)
    topic_input = st.text_input("Сабақ тақырыбы:", value="1. Эргономика дегеніміз не")
    
    if st.button("🔗 Оқушы сілтемесін генерациялау"):
        st.success("Сілтеме жасалды: `https://ustaz-mentor.streamlit.app/?topic=1`")

else:
    st.markdown("""
        <div class="study-card">
            <h2>Welcome back, Оқушы! 👋</h2>
            <p style="color: #38bdf8 !important;">Бүгін қандай тақырыпты меңгергіңіз келеді?</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_n, col_c = st.columns([2, 1])
    with col_n:
        s_name = st.text_input("Аты-жөніңіз:")
    with col_c:
        s_grade = st.selectbox("Сыныбыңыз:", st.session_state.classes_list)
        
    st.markdown("---")
    st.markdown("### 📝 Белсенді тапсырмалар")
    
    tab1, tab2 = st.tabs(["🚀 Интерактивті тест", "💻 Прагматикалық тренажер"])
    with tab1:
        st.info("Тақырып: 1. Эргономика дегеніміз не")
        st.radio("Монитор мен көздің арақашықтығы қандай болуы тиіс?", ["А) 20-30 см", "Б) 50-70 см", "В) 1 метр"])
        if st.button("Тестті тапсыру ⚡"):
            st.balloons()
            st.success("Нәтижеңіз сақталды: 10 / 10 ұпай! 🌟")
    with tab2:
        st.slider("Тренажер қадамы:", 0, 10, 0)
