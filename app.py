import streamlit as st
import pandas as pd
from datetime import datetime

# Беттің баптаулары
st.set_page_config(
    page_title="UstazMentor - Цифрлық платформа",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 🌟 КАСОМДЫҚ КӨК СТИЛЬДЕР ЖӘНЕ ТАЙМЕР ДИЗАЙНЫ
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
    .stApp {
        background-color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    .header-card {
        background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
        color: white;
        padding: 2.2rem;
        border-radius: 20px;
        box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.3);
        margin-bottom: 1.5rem;
        text-align: center;
    }
    .header-title {
        font-size: 2.5rem !important;
        font-weight: 800;
        margin-bottom: 0.5rem;
        color: #ffffff;
    }
    .header-subtitle {
        font-size: 1.1rem;
        opacity: 0.95;
        color: #e0e7ff;
    }
    /* Көк түсті тақырыптар мен жазулар */
    h1, h2, h3, h4, .blue-text {
        color: #1e40af !important;
        font-weight: 700 !important;
    }
    .context-box {
        background-color: #eff6ff;
        border-left: 5px solid #2563eb;
        padding: 1.2rem;
        border-radius: 12px;
        color: #1e3a8a;
        font-size: 1.05rem;
        margin-bottom: 1rem;
    }
    .timer-box {
        background: #dbeafe;
        color: #1e40af;
        padding: 0.8rem 1.2rem;
        border-radius: 10px;
        font-weight: bold;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 1rem;
        border: 1px solid #bfdbfe;
    }
    .stButton>button {
        border-radius: 12px !important;
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

# Хедер баннері
st.markdown("""
<div class="header-card">
    <div class="header-title">🎓 UstazMentor</div>
    <div class="header-subtitle">Информатика мұғалімдеріне арналған функционалдық сауаттылық платформасы</div>
</div>
""", unsafe_allow_html=True)

# Негізгі вкладкалар
tab_teacher, tab_student = st.tabs(["👩‍🏫 Мұғалім кабинеті", "👨‍🎓 Оқушы режимі"])

# --- 👩‍🏫 МҰҒАЛІМ КАБИНЕТІ ---
with tab_teacher:
    st.markdown("### 👩‍🏫 Мұғалімнің басқару панелі")
    
    st.markdown("**📌 Сыныпты таңдаңыз:**")
    selected_class = st.radio(
        "Сыныптар:",
        list(st.session_state.school_data.keys()),
        horizontal=True,
        label_visibility="collapsed",
        key="teacher_class_radio"
    )
    
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"**📚 {selected_class} тақырыптары:**")
        topics = st.session_state.school_data[selected_class]
        topic_titles = [t["title"] for t in topics]
        selected_topic_title = st.selectbox("Тақырыпты таңдаңыз:", topic_titles)
        
        current_topic = next(t for t in topics if t["title"] == selected_topic_title)
        
        st.markdown("---")
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
        st.markdown(f"### 📖 {current_topic['title']}")
        
        st.markdown(f"""
        <div class="context-box">
            <b>🌐 Өмірлік жағдаят (Контекст):</b><br>{current_topic['context']}
        </div>
        """, unsafe_allow_html=True)
        
        save_mode = st.checkbox("💾 Сабақ нәтижелерін базада сақтау", value=True)
        
        st.markdown("**🔗 Оқушыларға арналған сабақ сілтемесі:**")
        st.code(f"https://ustaz-mentor.streamlit.app/?class={selected_class}&topic={current_topic['id']}")

    st.divider()
    st.markdown("### 📊 Оқушылардың нәтижелері мен есеп беру")
    
    if st.session_state.submissions:
        df = pd.DataFrame(st.session_state.submissions)
        filtered_df = df[df["Сыныбы"].str.contains(selected_class[0], na=False)]
        
        if not filtered_df.empty:
            st.dataframe(filtered_df, use_container_width=True)
            
            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                csv = filtered_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Excel (CSV) форматында жүктеу",
                    data=csv,
                    file_name=f"UstazMentor_Netijeler_{selected_class}.csv",
                    mime="text/csv",
                    use_container_width=True
                )
            with col_btn2:
                # Буферге көшіру үшін мәтіндік формат жасау
                tsv_data = filtered_df.to_csv(sep='\t', index=False)
                st.download_button(
                    label="📋 Деректерді буферге көшіру (TSV формат)",
                    data=tsv_data,
                    file_name=f"Copy_Data_{selected_class}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
        else:
            st.info("Бұл сыныпта әзірге нәтижелер жоқ.")
    else:
        st.info("Әзірге ешқандай нәтиже тіркелмеді.")

# --- 👨‍🎓 ОҚУШЫ РЕЖИМІ ---
with tab_student:
    st.markdown("### 👨‍🎓 Оқушы режимі")
    
    col_t1, col_t2 = st.columns([3, 1])
    with col_t1:
        st.markdown("**📌 Сыныбыңызды таңдаңыз:**")
        st_class = st.radio(
            "Оқушы сыныбы:",
            list(st.session_state.school_data.keys()),
            horizontal=True,
            key="student_class_radio",
            label_visibility="collapsed"
        )
    with col_t2:
        # ⏱ ТАЙМЕР БАПТАУЫ (15-20 минут)
        timer_mins = st.selectbox("⏱ Таймер уақыты:", [15, 20, 10, 5], index=0)
        st.markdown(f'<div class="timer-box">⏳ Тапсырма уақыты: {timer_mins} минут</div>', unsafe_allow_html=True)

    topics = st.session_state.school_data[st_class]
    st_topic_title = st.selectbox("Тақырыпты таңдаңыз:", [t["title"] for t in topics], key="student_topic_select")
    current_topic = next(t for t in topics if t["title"] == st_topic_title)
    
    st.markdown("---")
    col_name, col_cls = st.columns(2)
    with col_name:
        student_name = st.text_input("Аты-жөніңіз:")
    with col_cls:
        student_class_full = st.text_input("Сынып литерін көрсетіңіз (мысалы: 5 «Ә»):", value="5 «Ә»")
        
    st.markdown(f"""
    <div class="context-box">
        <b>📖 Өмірлік жағдаят:</b> {current_topic['context']}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📝 Тапсырмалар:")
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
                "Ұпай": f"{score} / 10",
                "Уақыты": now_time
            })
            
            st.success(f"Рақмет, {student_name}! Жинаған ұпайыңыз: **{score} / 10 балл**.")
            st.info(f"**💡 Кері байланыс пен түсініктеме:**\n\n{current_topic['feedback']}")
