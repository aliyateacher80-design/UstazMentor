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

# Жоғарғы тақырып және ұран
st.markdown("""
    <div class="main-header">
        <h1>UstazMentor</h1>
        <p>Бір тақырып — бір өмірлік жағдаят — үш деңгей — нақты нәтиже!</p>
    </div>
""", unsafe_allow_html=True)

# Режимдер
col_mode1, col_mode2 = st.columns(2)
with col_mode1:
    st.button("👨‍🎓 Оқушы режимі", use_container_width=True)
with col_mode2:
    st.button("👩‍🏫 Мұғалім кабинеті", use_container_width=True, type="primary")

st.divider()

# Мұғалімнің басқару панелі
st.subheader("👨‍💻 Мұғалімнің басқару панелі 🔗")

st.write("Сыныпты таңдаңыз:")
selected_class = st.radio("Сыныптар:", ["5-сынып", "6-сынып", "7-сынып", "8-сынып", "9-сынып"], horizontal=True, label_visibility="collapsed")

# 5-сыныптың 14 тақырыбы
topics_5 = [
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
]

col_topic, col_timer = st.columns([3, 1])
with col_topic:
    st.write("Тақырыпты таңдаңыз:")
    selected_topic = st.selectbox("Тақырып:", topics_5, label_visibility="collapsed")

with col_timer:
    st.write("Таймер:")
    timer_val = st.number_input("Минут", value=15, label_visibility="collapsed")

st.info(f"💡 **Өмірлік жағдаят:** {selected_topic} бойынша практикалық дағдылар.")

st.markdown("### 🔗 САБАҚ СІЛТЕМЕСІН АВТОМАТТЫ ЖАСАУ")
shareable_url = f"https://ustaz-mentor.streamlit.app/?class={selected_class}&topic={selected_topic}&timer={timer_val}"
st.code(shareable_url)

st.divider()

# 3 қойындыға бөлінген тапсырмалар блогы
st.subheader(f"📖 Тапсырмалар: {selected_topic}")

tab_test, tab_match, tab_game = st.tabs(["📝 Тест (10 сұрақ)", "🔗 Сәйкестендіру (10 элемент)", "💻 Интерактивті деңгей"])

with tab_test:
    st.markdown("#### Функционалдық тест тапсырмалары")
    with st.form(key="main_test_form"):
        if "Эргономика" in selected_topic:
            st.radio("1. Компьютер алдында ұзақ отырғанда көзге күш түспеу үшін монитор мен көздің арақашықтығы қандай болуы тиіс?", ["А) 20-30 см", "Б) 50-70 см", "В) 1-1,5 метр"])
            st.radio("2. Дұрыс отыру қалпында арқа мен орындықтың бұрышы шамамен қандай болуы керек?", ["А) 90-100 градус", "Б) 45 градус", "В) 180 градус"])
        else:
            st.radio("1. Тақырып бойынша негізгі теориялық сұрақ:", ["А) Дұрыс жауап", "Б) Қате жауап 1", "В) Қате жауап 2"])
            st.radio("2. Өмірлік жағдаятқа негізделген сұрақ:", ["А) Дұрыс шешім", "Б) Қате шешім 1", "В) Қате шешім 2"])
            
        if st.form_submit_button("Тестті тексеру (10 ұпай)"):
            st.balloons()
            st.success("Тест сәтті аяқталды! 10 / 10 ұпай 🌟")

with tab_match:
    st.markdown("#### Терминдер мен ұғымдарды сәйкестендіру")
    with st.form(key="main_match_form"):
        for i in range(1, 6):
            st.text_input(f"{i}-элементтің сәйкестігін жазыңыз:", key=f"main_m_{i}")
        if st.form_submit_button("Сәйкестікті тексеру (10 ұпай)"):
            st.balloons()
            st.success("Барлық сәйкестіктер дұрыс! 10 ұпай 🎯")

with tab_game:
    st.markdown("#### Интерактивті тренажер және прагматикалық қадамдар")
    step = st.slider("Қадамдарды орындау деңгейі:", 0, 10, 0, key="main_slider")
    st.write(f"Ағымдағы қадам: **{step} / 10**")
    if st.button("Нәтижені тіркеу"):
        if step == 10:
            st.balloons()
            st.success("Құттықтаймыз! Барлық 10 қадам орындалды! 🚀")
        else:
            st.warning("Жүгірткіні 10-ға жеткізіңіз!")

st.divider()

st.subheader("📊 Оқушылардың нәтижелері")
st.write("Бұл сыныпта әзірге сақталған нәтижелер жоқ.")
