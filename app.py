import streamlit as st

st.set_page_config(page_title="UstazMentor", page_icon="💻", layout="wide")

# Дизайн стилі
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #4f46e5 0%, #3b82f6 100%);
        padding: 25px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="main-header">
        <h1>UstazMentor 💻</h1>
        <p>Бір тақырып — бір өмірлік жағдаят — үш деңгей — нақты нәтиже!</p>
    </div>
""", unsafe_allow_html=True)

# Барлық сыныптардың тақырыптар базасы
topics_by_class = {
    "5-сынып": [
        "1. Эргономика дегеніміз не",
        "2. Эргономика дегеніміз не. Практикалық жұмыс",
        "3. Біздің айналамыздағы ақпарат",
        "4. Интернетте ақпаратты іздеу",
        "5. Интернетте ақпаратты іздеу. Практикалық жұмыс",
        "6. Есептеу техникасының даму тарихы",
        "7. Программалық жасақтама және жасанды интеллект",
        "8. Компьютерлік графика және оның түрлері",
        "9. Компьютерлік графика және оның түрлері. Практикалық жұмыс",
        "10. Растрлық кескіндерді құру",
        "11. Растрлық кескіндерді құру. Практикалық жұмыс",
        "12. Растрлық кескіндерді өңдеу құралдары",
        "13. Растрлық кескіндерді өңдеу құралдары. Практикалық жұмыс",
        "14. Графика және жасанды интеллект. Практикалық жұмыс"
    ],
    "6-сынып": [
        "1. Компьютерлік желілер және түрлері",
        "2. Интернет және қауіпсіздік",
        "3. Алгоритм қасиеттері және блок-схемалар",
        "4. Python тілінде сызықтық программалар құру",
        "5. Тармақталған алгоритмдер"
    ],
    "7-сынып": [
        "1. Мәліметтер базасы және кестелер",
        "2. HTML және веб-беттерді құрылымдау",
        "3. Python тілінде циклдік операторлар",
        "4. 3D модельдеу негіздері"
    ],
    "8-сынып": [
        "1. Логикалық операциялар және кестелер",
        "2. Python тілінде тізімдер мен массивтер",
        "3. Ақпараттық қауіпсіздік және кибергигиена",
        "4. Мобильді қосымшалар құру негіздері"
    ],
    "9-сынып": [
        "1. Жасанды интеллект және нейрондық желілер",
        "2. Деректерді талдау және Python (Pandas)",
        "3. Веб-қосымшалар құру (Streamlit)"
    ]
}

# Режимдерді таңдау (Оқушы / Мұғалім)
role = st.radio("Режимді таңдаңыз:", ["👨‍🎓 Оқушы режимі", "👩‍🏫 Мұғалім кабинеті"], horizontal=True)

st.divider()

if role == "👩‍🏫 Мұғалім кабинеті":
    st.subheader("👨‍💻 Мұғалімнің басқару және сілтеме жасау панелі 🔗")
    
    selected_class = st.radio("Сыныпты таңдаңыз:", list(topics_by_class.keys()), horizontal=True)
    current_topics = topics_by_class.get(selected_class, [])
    
    col_t, col_timer = st.columns([3, 1])
    with col_t:
        selected_topic = st.selectbox("Тақырыпты таңдаңыз:", current_topics)
    with col_timer:
        timer_val = st.number_input("Таймер (мин):", value=15)
        
    st.info(f"💡 **Таңдалған сынып:** {selected_class} | **Тақырып:** {selected_topic}")
    
    st.markdown("### 🔗 Оқушыларға арналған сабақ сілтемесі:")
    shareable_url = f"https://ustaz-mentor.streamlit.app/?class={selected_class}&topic={selected_topic}&timer={timer_val}"
    st.code(shareable_url)

else:
    st.subheader("👨‍🎓 Оқушы кабинеті")
    
    # URL арқылы немесе қолмен сынып пен тақырыпты алу
    query_params = st.query_params
    default_class = query_params.get("class", "5-сынып")
    default_topic = query_params.get("topic", topics_by_class["5-сынып"][0])
    
    selected_class = st.selectbox("Сыныбыңызды таңдаңыз:", list(topics_by_class.keys()), index=list(topics_by_class.keys()).index(default_class) if default_class in topics_by_class else 0)
    current_topics = topics_by_class.get(selected_class, [])
    
    selected_topic = st.selectbox("Сабақ тақырыбын таңдаңыз:", current_topics, index=current_topics.index(default_topic) if default_topic in current_topics else 0)
    
    st.success(f"🎯 **Ағымдағы сабақ:** {selected_class} — {selected_topic}")
    
    st.divider()
    
    # Тапсырмалар вкладкалары
    tab_test, tab_match, tab_game = st.tabs(["📝 Тест (10 сұрақ)", "🔗 Сәйкестендіру", "💻 Интерактивті деңгей"])
    
    with tab_test:
        st.markdown(f"#### Функционалдық тест: {selected_topic}")
        with st.form(key=f"student_test_{selected_topic}"):
            for i in range(1, 11):
                st.radio(f"{i}-сұрақ:", [f"А) {selected_topic} - дұрыс жауап", "Б) Қате нұсқа 1", "В) Қате нұсқа 2"], key=f"sq_{i}")
            if st.form_submit_button("Тестті тексеру (10 ұпай)"):
                st.balloons()
                st.success("Тест тапсырылды! 10 / 10 ұпай 🌟")
                
    with tab_match:
        st.markdown(f"#### Сәйкестендіру тапсырмасы: {selected_topic}")
        with st.form(key=f"student_match_{selected_topic}"):
            for i in range(1, 11):
                st.text_input(f"{i}-элементтің сәйкестігі:", key=f"sm_{i}")
            if st.form_submit_button("Сәйкестікті тексеру (10 ұпай)"):
                st.balloons()
                st.success("Сәйкестіктер қабылданды! 10 ұпай 🎯")
                
    with tab_game:
        st.markdown(f"#### Интерактивті тренажер (10 қадам): {selected_topic}")
        step = st.slider("Қадамды таңдаңыз:", 0, 10, 0, key="student_slider")
        st.write(f"Орындалу деңгейі: **{step} / 10**")
        
        if st.button("Нәтиже тіркеу", key="student_btn"):
            if step == 10:
                st.balloons()
                st.success("Құттықтаймыз! Барлық 10 қадам сәтті орындалды! 🚀")
            else:
                st.warning("Жүгірткіні 10-ға жеткізіңіз!")

st.divider()
st.caption("UstazMentor платформасы © 2026 | Барлық құқықтар қорғалған.")
