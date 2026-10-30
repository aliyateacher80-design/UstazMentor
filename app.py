import streamlit as st

st.set_page_config(page_title="UstazMentor - 5-сынып", page_icon="💻", layout="wide")

# 1. Сессия базасын баптау
if "classes_list" not in st.session_state:
    st.session_state.classes_list = ["5 «А»", "5 «Ә»"]

if "results_db" not in st.session_state:
    st.session_state.results_db = [
        {"name": "Жайнарбек А.", "grade": "5 «Ә»", "topic": "1. Эргономика дегеніміз не", "task_type": "Тест", "score_num": 10, "score": "10 / 10 ұпай"},
        {"name": "Айша Б.", "grade": "5 «Ә»", "topic": "1. Эргономика дегеніміз не", "task_type": "Тест", "score_num": 9, "score": "9 / 10 ұпай"}
    ]

# 2. Заманауи SaaS интерфейс стилі (Қараңғы, жинақы және премиум орналасу)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

html, body, [data-testid="stAppViewContainer"], .stApp {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    background-color: #0b0f19 !important;
    color: #e2e8f0 !important;
}

[data-testid="stHeader"] { background: transparent !important; }

/* Карточкалар мен блоктардың сыртқы түрі */
.ui-card {
    background: #111827;
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

/* Жоғарғы басты шағын панель */
.top-bar {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    border: 1px solid rgba(56, 189, 248, 0.2);
    border-radius: 16px;
    padding: 20px 24px;
    margin-bottom: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* Заманауи батырмалар */
.stButton > button, .stFormSubmitButton > button {
    background: linear-gradient(135deg, #0284c7 0%, #4f46e5 100%) !important;
    color: white !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    border: none !important;
    padding: 0.5rem 1rem;
    box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3) !important;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-1px);
    opacity: 0.95;
}
</style>
""", unsafe_allow_html=True)

# Жоғарғы заманауи панель (Header Shell)
st.markdown("""
    <div class="top-bar">
        <div>
            <h2 style="margin: 0; color: #ffffff; font-size: 22px;">💻 UstazMentor</h2>
            <p style="margin: 0; color: #94a3b8; font-size: 13px;">5-сынып Информатика | Оқыту және басқару платформасы</p>
        </div>
        <div>
            <span style="background: rgba(56, 189, 248, 0.1); color: #38bdf8; padding: 6px 12px; border-radius: 20px; font-size: 12px; border: 1px solid rgba(56, 189, 248, 0.2);">v2.0 Active</span>
        </div>
    </div>
""", unsafe_allow_html=True)

sections_dict = {
    "📁 Бөлім: Ақпарат және компьютер": [
        "1. Эргономика дегеніміз не", "2. Эргономика дегеніміз не. Практикалық жұмыс",
        "3. Біздің айналамыздағы ақпарат", "4. Интернетте ақпаратты іздеу",
        "5. Интернетте ақпаратты іздеу. Практикалық жұмыс", "6. Есептеу техникасының даму тарихы",
        "7. Есептеу техникасының даму тарихы"
    ],
    "📁 Бөлім: Цифрлық кескіндер": [
        "8. Компьютерлік графика және оның түрлері", "9. Компьютерлік графика және оның түрлері. Практикалық жұмыс",
        "10. Растрлық кескіндерді құру", "11. Растрлық кескіндерді құру. Практикалық жұмыс",
        "12. Растрлық кескіндерді өңдеу құралдары", "13. Растрлық кескіндерді өңдеу құралдары. Практикалық жұмыс",
        "14. Графика және жасанды интеллект. Практикалық жұмыс"
    ]
}

external_links = {
    "7. Есептеу техникасының даму тарихы": "https://aliyateacher80-design.github.io/history-game/",
    "12. Растрлық кескіндерді өңдеу құралдары": "https://aliyateacher80-design.github.io/raastr-game5/",
    "13. Растрлық кескіндерді өңдеу құралдары. Практикалық жұмыс": "https://aliyateacher80-design.github.io/ondeu-qurak-prakt/",
    "14. Графика және жасанды интеллект. Практикалық жұмыс": "https://aliyateacher80-design.github.io/graphics-ai-task/"
}

all_topics = []
for sec, topics in sections_dict.items():
    all_topics.extend(topics)

# Режимді таңдау блогы
col_r1, col_r2 = st.columns([1, 1])
with col_r1:
    role = st.radio("Режимді таңдаңыз:", ["👨‍🎓 Оқушы режимі", "👩‍🏫 Мұғалім кабинеті"], horizontal=True)

st.divider()

if role == "👩‍🏫 Мұғалім кабинеті":
    st.markdown("### 👩‍🏫 Мұғалімнің басқару кабинеті")
    
    with st.popover("📊 Teacher Dashboard — Сыныптар мен нәтижелерді ашу", use_container_width=True):
        st.markdown("### 🏫 Сыныптар навигаторы")
        selected_class = st.radio("Қарағыңыз келетін сыныпты таңдаңыз:", st.session_state.classes_list, horizontal=True)
        
        col_add1, col_add2 = st.columns([3, 1])
        with col_add1:
            new_class_input = st.text_input("Жаңа сынып қосу:", placeholder="Мысалы: 5 «Б»", key="new_class_key")
        with col_add2:
            st.write(""); st.write("")
            if st.button("➕ Қосу"):
                if new_class_input.strip() and new_class_input.strip() not in st.session_state.classes_list:
                    st.session_state.classes_list.append(new_class_input.strip())
                    st.success(f"{new_class_input} сәтті қосылды!")
                    st.rerun()

        st.divider()
        st.markdown(f"#### 📈 {selected_class} сыныбының нәтижелері")
        class_filtered_db = [r for r in st.session_state.results_db if r.get('grade') == selected_class]
        
        if len(class_filtered_db) > 0:
            for idx, res in enumerate(class_filtered_db, 1):
                score_val = res.get('score_num', 10)
                c1, c2, c3 = st.columns([2, 2, 3])
                with c1: st.write(f"**{idx}. {res['name']}**")
                with c2: st.write(f"Ұпайы: **{res['score']}**")
                with c3: st.progress(min(score_val / 10.0, 1.0))
        else:
            st.info(f"{selected_class} сыныбында әзірге сақталған нәтиже жоқ.")

    st.divider()
    st.markdown("### ⚙️ Сабақ баптаулары мен оқушы сілтемесі")
    save_results_enabled = st.toggle("📊 Оқушы нәтижелерін базаға сақтау", value=True)
    selected_section = st.selectbox("Бөлімді таңдаңыз:", list(sections_dict.keys()))
    selected_topic = st.selectbox("Тақырыпты таңдаңыз:", sections_dict[selected_section])
    timer_val = st.number_input("Сабақ таймері (минут):", value=15)
        
    st.info(f"💡 **Таңдалған бөлім:** {selected_section} | **Тақырып:** {selected_topic}")
    shareable_url = f"https://ustaz-mentor.streamlit.app/?topic={selected_topic}&timer={timer_val}&save={'1' if save_results_enabled else '0'}"
    st.code(shareable_url)

    st.divider()
    if len(st.session_state.results_db) > 0:
        if st.button("🗑️ Барлық сақталған нәтижелерді тазарту"):
            st.session_state.results_db = []
            st.rerun()

else:
    st.markdown("### 👨‍🎓 Оқушы кабинеті")
    col_name, col_class = st.columns([2, 1])
    with col_name:
        student_name = st.text_input("Аты-жөніңізді енгізіңіз:", placeholder="Аты-жөніңіз...")
    with col_class:
        student_grade = st.selectbox("Сыныбыңыз:", st.session_state.classes_list)
    
    query_params = st.query_params
    default_topic = query_params.get("topic", all_topics[0])
    if isinstance(default_topic, list): default_topic = default_topic[0]
    
    save_param = query_params.get("save", "1")
    if isinstance(save_param, list): save_param = save_param[0]
    save_mode = (save_param == "1")
    
    topic_index = all_topics.index(default_topic) if default_topic in all_topics else 0
    selected_topic = st.selectbox("Сабақ тақырыбын таңдаңыз:", all_topics, index=topic_index)
    
    st.success(f"🎯 **Ағымдағы сабақ:** {selected_topic}")
    if not save_mode:
        st.warning("⚠️ Ескерту: Бұл сабақта нәтижелерді сақтау өшірілген.")
    
    st.divider()
    
    is_link_topic = any(selected_topic.startswith(prefix) for prefix in ["7.", "12.", "13.", "14."])
    
    if is_link_topic:
        st.markdown(f"### 🌐 Интерактивті тапсырма / Ойын: {selected_topic}")
        game_url = external_links.get(selected_topic, "https://github.com")
        st.markdown(f"👉 **[Тапсырманы / Ойынды ашу 🚀]({game_url})**")
        
        st.divider()
        if st.button("✅ Тапсырманы орындап шықтым"):
            if not student_name.strip():
                st.error("⚠️ Аты-жөніңізді жазыңыз!")
            else:
                st.balloons()
                st.success(f"Құттықтаймыз, {student_name}! Тапсырма орындалды! 🌟")
                if save_mode:
                    st.session_state.results_db.append({
                        "name": student_name, "grade": student_grade,
                        "topic": selected_topic, "task_type": "Интерактивті веб-ойын",
                        "score_num": 10, "score": "10 / 10 (Орындалды)"
                    })
    else:
        tab_test, tab_match, tab_game = st.tabs(["📝 Тест (10 сұрақ)", "🔗 Сәйкестендіру", "💻 Прагматикалық тренажер"])
        
        with tab_test:
            st.markdown(f"#### Функционалдық тест: {selected_topic}")
            with st.form(key=f"test_{selected_topic}"):
                if "1. Эргономика дегеніміз не" in selected_topic:
                    st.radio("1. Монитор мен көздің арақашықтығы қандай болуы тиіс?", ["А) 20-30 см", "Б) 50-70 см", "В) 1-1,5 метр"])
                    st.radio("2. Арқа мен орындықтың бұрышы қандай болуы керек?", ["А) 90-100 градус", "Б) 45 градус", "В) 180 градус"])
                else:
                    st.info("Бұл тақырыпқа тест сұрақтары дайындалуда.")
                
                submit_test = st.form_submit_button("Тестті тексеру және ұпайды есептеу")
                if submit_test:
                    if not student_name.strip():
                        st.error("⚠️ Аты-жөніңізді жазыңыз!")
                    else:
                        st.balloons()
                        st.success(f"Құттықтаймыз, {student_name}! Тест аяқталды! 🌟")
                        if save_mode:
                            st.session_state.results_db.append({
                                "name": student_name, "grade": student_grade,
                                "topic": selected_topic, "task_type": "Тест",
                                "score_num": 10, "score": "10 / 10 ұпай"
                            })

        with tab_match:
            st.markdown(f"#### Сәйкестендіру тапсырмасы: {selected_topic}")
            st.info("📌 Ұғымдарды өзара дұрыс сәйкестендіріңіз.")

        with tab_game:
            st.markdown(f"#### Прагматикалық тренажер: {selected_topic}")
            step = st.slider("Қадамды таңдаңыз:", 0, 10, 0)
            if st.button("Қадамды растау"):
                st.success(f"Тренажер қадамы тіркелді: {step} / 10 🚀")
