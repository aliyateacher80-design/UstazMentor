import streamlit as st
import pandas as pd
from datetime import datetime

# Беттің баптаулары
st.set_page_config(
    page_title="USTAZAI - Функционалдық сауаттылық платформасы",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 🌟 СУРЕТТЕГІДЕЙ ЗАМАНАУИ ДИЗАЙН ИНТЕРФЕЙСІ ЖӘНЕ СТИЛЬДЕР
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
    .stApp {
        background-color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    /* Жоғарғы фиолетті-көк шапка карточкасы */
    .header-card {
        background: linear-gradient(135deg, #4f46e5 0%, #3b82f6 100%);
        color: white;
        padding: 2rem 2.5rem;
        border-radius: 0 0 24px 24px;
        box-shadow: 0 10px 25px -5px rgba(59, 130, 246, 0.3);
        margin-bottom: 2rem;
    }
    .header-title {
        font-size: 2.2rem !important;
        font-weight: 800;
        margin-bottom: 0.2rem;
        color: #ffffff;
    }
    .header-subtitle {
        font-size: 1rem;
        opacity: 0.9;
        color: #e0e7ff;
    }
    /* Негізгі үлкен ақ карточка контейнері */
    .main-container {
        background: #ffffff;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        border: 1px solid #e2e8f0;
        margin-bottom: 2rem;
    }
    h1, h2, h3, h4 {
        color: #1e293b !important;
        font-weight: 700 !important;
    }
    .context-box {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 1.2rem;
        border-radius: 12px;
        color: #334155;
        font-size: 1.05rem;
        margin-bottom: 1rem;
    }
    .feedback-box {
        background-color: #f0fdf4;
        border-left: 5px solid #22c55e;
        padding: 1.2rem;
        border-radius: 12px;
        color: #166534;
        font-size: 1.05rem;
        margin-top: 1rem;
    }
    .stButton>button {
        border-radius: 10px !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# Session state деректері
if "school_data" not in st.session_state:
    st.session_state.school_data = {
        "5-сынып": [
            {"id": 1, "title": "1. Компьютер және қауіпсіздік", "context": "Кабинеттегі қауіпсіздік ережелері мен дұрыс отыру тәртібі.", "a": "Компьютерді дұрыс қосу тәртібін жазыңыз.", "b": "Қате мен дұрыс отыру жағдайын салыстырыңыз.", "c": "Қауіпсіздік ережесін сақтау бойынша шағын жоспар құрыңыз.", "feedback": "Керемет! Компьютер кабинетіндегі қауіпсіздік ережелерін сақтау денсаулық үшін өте маңызды."},
            {"id": 2, "title": "2. Ақпарат ұғымы", "context": "Өмірдегі ақпарат түрлерін қабылдау мен тарату әдістері.", "a": "Ақпарат көздерін атап көрсетіңіз.", "b": "Ақпаратты қабылдау түрлеріне қарай жіктеңіз.", "c": "Күнделікті өмірдегі ақпараттық қауіпсіздікті дәлелдеңіз.", "feedback": "Жақсы! Ақпаратты қабылдау және өңдеу адам өміріндегі шешім қабылдауға тікелей әсер етеді."}
        ],
        "6-сынып": [
            {"id": 1, "title": "1. Электрондық кестелер", "context": "Мектеп асханасының бір апталық өнім шығынын есептеу.", "a": "Ұяшық адресін дұрыс көрсетіңіз.", "b": "Екі дүкен бағасын формула арқылы салыстырыңыз.", "c": "Тиімді бюджет жоспарын ұсынып, дәлелдеңіз.", "feedback": "Талдауыңыз дұрыс! Электрондық кестелер қаржыны үнемдеуге және есеп айырысуға көмектеседі."}
        ],
        "7-сынып": [
            {"id": 1, "title": "1. Python тіліне кіріспе", "context": "Мектеп жарысының нәтижелерін есептейтін шағын скрипт.", "a": "Айнымалы мәнін дұрыс жазыңыз.", "b": "Шартты оператор жұмысын талдаңыз.", "c": "Берілген есепті шығаратын код құрыңыз.", "feedback": "Өте жақсы! Бағдарламалау логикасы күнделікті өмірдегі алгоритмдерді автоматтандырады."}
        ],
        "8-сынып": [
            {"id": 1, "title": "1. Компьютерлік желілер", "context": "Мектеп кабинеттерін жергілікті желіге қосу.", "a": "Желі жабдықтарын атаңыз.", "b": "Wi-Fi мен сымды интернетті салыстырыңыз.", "c": "Желілік топология жобасын ұсыныңыз.", "feedback": "Керемет! Желі қауіпсіздігі мен жылдамдығы дұрыс конфигурацияға тікелей байланысты."}
        ],
        "9-сынып": [
            {"id": 1, "title": "1. Жасанды интеллект негіздері", "context": "Суреттерді танитын қарапайым нейрожелі.", "a": "Оқыту деректерін таңдау.", "b": "Қателік функциясын (MSE) талдаңыз.", "c": "ЖИ көмегімен мәселені шешу жобасын ұсыныңыз.", "feedback": "Тамаша! Жасанды интеллект модельдері заманауи өмірлік мәселелерді шешуде үлкен рөл атқарады."}
        ]
    }

if "submissions" not in st.session_state:
    st.session_state.submissions = []

if "app_mode" not in st.session_state:
    st.session_state.app_mode = "Мұғалім кабинеті"

# Жоғарғы шапка және режимді ауыстыру батырмалары
col_h1, col_h2 = st.columns([2, 1])
with col_h1:
    st.markdown("""
    <div style="padding: 1rem 0;">
        <span style="font-size: 2rem; font-weight: 800; color: #ffffff;">🎓 USTAZAI</span><br>
        <span style="font-size: 0.95rem; color: #e0e7ff;">Бір тақырып — бір өмірлік жағдаят — үш деңгей — нақты нәтиже!</span>
    </div>
    """, unsafe_allow_html=True)
with col_h2:
    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        if st.button("Оқушы режимі", use_container_width=True):
            st.session_state.app_mode = "Оқушы режимі"
            st.rerun()
    with col_b2:
        if st.button("Мұғалім кабинеті", use_container_width=True, type="primary"):
            st.session_state.app_mode = "Мұғалім кабинеті"
            st.rerun()

st.markdown("<hr style='margin: 0px 0px 20px 0px; border-color: #3b82f6;'>", unsafe_allow_html=True)

# ================= МҰҒАЛІМ КАБИНЕТІ =================
if st.session_state.app_mode == "Мұғалім кабинеті":
    st.markdown("""
    <div class="main-container">
        <h3>👩‍🏫 Мұғалімнің басқару панелі</h3>
    """, unsafe_allow_html=True)
    
    st.markdown("**Сыныпты таңдаңыз:**")
    selected_class = st.radio(
        "Сыныптар:",
        list(st.session_state.school_data.keys()),
        horizontal=True,
        label_visibility="collapsed",
        key="teacher_class_radio"
    )
    
    st.markdown("<hr style='margin: 15px 0px;'>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        st.markdown(f"**📚 {selected_class} тақырыптары:**")
        topics = st.session_state.school_data[selected_class]
        topic_titles = [t["title"] for t in topics]
        selected_topic_title = st.selectbox("Тақырыпты таңдаңыз:", topic_titles, label_visibility="collapsed")
        
        current_topic = next(t for t in topics if t["title"] == selected_topic_title)
        
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("➕ Өз тапсырмаңды жасау"):
            with st.form("custom_form"):
                c_title = st.text_input("Тақырып атауы:")
                c_context = st.text_area("Өмірлік жағдаят (Контекст):")
                c_a = st.text_input("А деңгейі сұрағы:")
                c_b = st.text_input("В деңгейі сұрағы:")
                c_c = st.text_input("С деңгейі сұрағы:")
                c_feedback = st.text_input("Автоматты кері байланыс мәтіні:")
                
                submitted = st.form_submit_button("Тақырыпты қосу")
                if submitted and c_title and c_context:
                    new_id = len(st.session_state.school_data[selected_class]) + 1
                    new_t = {
                        "id": new_id,
                        "title": f"{new_id}. {c_title}",
                        "context": c_context,
                        "a": c_a or "Базалық сұрақ.",
                        "b": c_b or "Талдау сұрағы.",
                        "c": c_c or "Мәселені шешу.",
                        "feedback": c_feedback or "Жарайсыз!"
                    }
                    st.session_state.school_data[selected_class].append(new_t)
                    st.success("Жаңа тақырып сәтті қосылды!")
                    st.rerun()

    with col2:
        st.markdown(f"#### {current_topic['title']}")
        
        st.markdown(f"""
        <div class="context-box">
            <b>Өмірлік жағдаят:</b> {current_topic['context']}
        </div>
        """, unsafe_allow_html=True)
        
        # Баптаулар контейнері
        opt_col1, opt_col2 = st.columns(2)
        with opt_col1:
            save_mode = st.checkbox("💾 Нәтижені сақтау:", value=True)
        with opt_col2:
            set_timer_mins = st.selectbox("⏱ Таймер уақыты:", [10, 15, 20, 30], index=1, key="set_timer_val")
        
        st.markdown("**🔗 САБАҚ СІЛТЕМЕСІН АВТОМАТТЫ ЖАСАУ**")
        link_col1, link_col2 = st.columns([4, 1])
        with link_col1:
            share_link = f"https://ustazai.streamlit.app/?class={selected_class}&topic={current_topic['id']}&timer={set_timer_mins}"
            st.code(share_link, language="")
        with link_col2:
            st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
            if st.button("📋 Көшіру", use_container_width=True):
                st.toast("Сілтеме буферге көшірілді!")

    st.markdown("<hr style='margin: 25px 0px;'>", unsafe_allow_html=True)
    st.markdown("#### 📊 Оқушылардың нәтижелері")
    
    if st.session_state.submissions:
        df = pd.DataFrame(st.session_state.submissions)
        filtered_df = df[df["Сыныбы"].str.contains(selected_class[0], na=False)]
        
        if not filtered_df.empty:
            st.dataframe(filtered_df, use_container_width=True)
            
            csv = filtered_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Excel-ге жүктеу (CSV)",
                data=csv,
                file_name=f"UstazAI_Netijeler_{selected_class}.csv",
                mime="text/csv",
            )
        else:
            st.info("Бұл сыныпта әзірге нәтижелер жоқ.")
    else:
        st.info("Бұл сыныпта әзірге нәтижелер жоқ немесе сақтау режимі өшірулі.")

    st.markdown("</div>", unsafe_allow_html=True)

# ================= ОҚУШЫ РЕЖИМІ =================
else:
    st.markdown("""
    <div class="main-container">
        <h3>👨‍🎓 Оқушы режимі</h3>
    """, unsafe_allow_html=True)
    
    st_class = st.radio(
        "Оқушы сыныбы:",
        list(st.session_state.school_data.keys()),
        horizontal=True,
        key="student_class_radio"
    )
    
    topics = st.session_state.school_data[st_class]
    st_topic_title = st.selectbox("Тақырыпты таңдаңыз:", [t["title"] for t in topics], key="student_topic_select")
    current_topic = next(t for t in topics if t["title"] == st_topic_title)
    
    st.markdown("<hr style='margin: 15px 0px;'>", unsafe_allow_html=True)
    
    col_name, col_cls = st.columns(2)
    with col_name:
        student_name = st.text_input("Аты-жөніңіз:")
    with col_cls:
        student_class_full = st.text_input("Сынып літерін көрсетіңіз (мысалы: 8 «Ә»):", value="8 «Ә»")
        
    st.markdown(f"""
    <div class="context-box">
        <b>📖 Өмірлік жағдаят:</b> {current_topic['context']}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 📝 Тапсырмалар:")
    ans_a = st.text_input(f"🟢 A деңгейі (2 балл): {current_topic['a']}")
    ans_b = st.text_input(f"🟡 B деңгейі (3 балл): {current_topic['b']}")
    ans_c = st.text_area(f"🔴 C деңгейі (5 балл): {current_topic['c']}")
    
    if st.button("🚀 Жауаптарды жіберу", type="primary"):
        if not student_name.strip():
            st.error("Өтінемін, аты-жөніңізді енгізіңіз!")
        else:
            score = 10
            now_time = datetime.now().strftime("%H:%M:%S")
            
            st.session_state.submissions.append({
                "Оқушы аты-жөні": student_name,
                "Сыныбы": student_class_full,
                "Тақырып": current_topic["title"],
                "Жинаған ұпайы": f"{score} / 10",
                "Уақыты": now_time
            })
            
            st.success(f"Рақмет, {student_name}! Жинаған ұпайыңыз: **{score} / 10 балл**.")
            
            # Оқушыға арналған кері байланыс
            st.markdown(f"""
            <div class="feedback-box">
                <b>💡 Мұғалімнің кері байланысы мен түсініктемесі:</b><br>
                {current_topic['feedback']}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
       
