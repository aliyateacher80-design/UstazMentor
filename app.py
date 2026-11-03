import streamlit as st

st.set_page_config(page_title="UstazMentor - 3D Digital School", page_icon="💻", layout="wide")

# 1. Сессия базасын баптау
if "classes_list" not in st.session_state:
    st.session_state.classes_list = ["5 «А»", "5 «Ә»"]

if "results_db" not in st.session_state:
    st.session_state.results_db = [
        {"name": "Жайнарбек А.", "grade": "5 «Ә»", "topic": "1. Эргономика дегеніміз не", "task_type": "Тест", "score_num": 10, "score": "10 / 10 ұпай"},
        {"name": "Айша Б.", "grade": "5 «Ә»", "topic": "1. Эргономика дегеніміз не", "task_type": "Тест", "score_num": 9, "score": "9 / 10 ұпай"},
        {"name": "Арман Қ.", "grade": "5 «А»", "topic": "1. Эргономика дегеніміз не", "task_type": "Тест", "score_num": 8, "score": "8 / 10 ұпай"}
    ]

# 2. 3D DIGITAL SCHOOL + ГАЛАКТИКА ЖӘНЕ МЕТЕОРИТТЕР СТИЛІ
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');

/* Жалпы қараңғы кибер ғарыш фоны */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #f1f5f9;
}
.stApp {
    background: #070b14;
    overflow-x: hidden;
}

/* Ғарыштық жұлдыздар мен ағатын метеориттер анимациясы */
.stApp::before {
    content: "";
    position: fixed;
    top: 0; left: 0; width: 100vw; height: 100vh;
    background: 
      radial-gradient(1.5px 1.5px at 20px 30px, #ffffff, rgba(0,0,0,0)),
      radial-gradient(1.5px 1.5px at 100px 150px, #38bdf8, rgba(0,0,0,0)),
      radial-gradient(2px 2px at 200px 80px, #c084fc, rgba(0,0,0,0)),
      radial-gradient(1px 1px at 300px 250px, #ffffff, rgba(0,0,0,0)),
      radial-gradient(2px 2px at 450px 120px, #38bdf8, rgba(0,0,0,0)),
      radial-gradient(1.5px 1.5px at 600px 350px, #fde047, rgba(0,0,0,0));
    background-repeat: repeat;
    background-size: 550px 550px;
    opacity: 0.85;
    z-index: 0;
    pointer-events: none;
    animation: starsDrift 60s linear infinite;
}

@keyframes starsDrift {
    from { transform: translateY(0); }
    to { transform: translateY(-550px); }
}

/* Ағатын метеорит (Shooting star) */
.stApp::after {
    content: "";
    position: fixed;
    top: -100px;
    right: 20%;
    width: 2px;
    height: 120px;
    background: linear-gradient(180deg, rgba(255,255,255,0), #38bdf8, #ffffff);
    transform: rotate(45deg);
    opacity: 0;
    z-index: 0;
    pointer-events: none;
    animation: meteorFall 4s ease-in-out infinite;
}

@keyframes meteorFall {
    0% { opacity: 0; transform: translate(0, 0) rotate(45deg); }
    10% { opacity: 1; }
    25% { opacity: 0; transform: translate(600px, 600px) rotate(45deg); }
    100% { opacity: 0; }
}

.block-container {
    max-width: 1400px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    position: relative;
    z-index: 1;
}

/* 3D DIGITAL SCHOOL Басты баннері */
.main-header {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #0b1329 0%, #0f1f44 50%, #082f49 100%);
    padding: 36px 42px;
    border: 1px solid rgba(6,182,212,0.35);
    border-radius: 26px;
    color: white;
    margin-bottom: 24px;
    box-shadow: 0 20px 50px rgba(6,182,212,0.18), inset 0 1px 0 rgba(255,255,255,0.2);
}
.main-header h1 {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(28px, 4vw, 44px);
    font-weight: 800;
    letter-spacing: -1px;
    margin: 0 0 8px 0;
    color: #ffffff !important;
}
.main-header p {
    color: #bae6fd;
    font-size: 15px;
    margin: 0;
}
.badge-3d {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 999px;
    background: rgba(6,182,212,0.2);
    border: 1px solid #22d3ee;
    color: #22d3ee;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    margin-bottom: 12px;
}

/* Карточкалар мен блоктар */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(15, 23, 42, 0.85) !important;
    backdrop-filter: blur(14px);
    border: 1px solid rgba(56, 189, 248, 0.25) !important;
    border-radius: 20px !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4) !important;
}

h1, h2, h3, h4, [data-testid="stSubheader"] {
    font-family: 'Outfit', sans-serif;
    color: #f8fafc !important;
    font-weight: 800 !important;
}
label, [data-testid="stWidgetLabel"] {
    color: #e2e8f0 !important;
    font-weight: 600 !important;
}

/* 3D батырмалар */
.stButton > button, .stFormSubmitButton > button {
    border: 0 !important;
    border-radius: 12px !important;
    padding: 0.65rem 1.4rem !important;
    font-weight: 700 !important;
    color: white !important;
    background: linear-gradient(110deg, #2563eb, #0891b2) !important;
    box-shadow: 0 4px 0 #1d4ed8, 0 8px 20px rgba(6,182,212,0.3) !important;
    transition: all 0.15s ease !important;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 0 #1d4ed8, 0 12px 25px rgba(6,182,212,0.4) !important;
}
.stButton > button:active {
    transform: translateY(2px);
    box-shadow: 0 2px 0 #1d4ed8 !important;
}

/* Енгізу өрістері */
.stTextInput input, .stSelectbox [data-baseweb="select"] {
    background-color: #0f172a !important;
    color: #ffffff !important;
    border-radius: 12px !important;
    border-color: rgba(56, 189, 248, 0.3) !important;
}

/* Қойындылар (Tabs) */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(15, 23, 42, 0.7);
    padding: 6px;
    border-radius: 14px;
    border: 1px solid rgba(56, 189, 248, 0.2);
    gap: 6px;
}
.stTabs [data-baseweb="tab"] {
    color: #94a3b8 !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
}
.stTabs [aria-selected="true"] {
    background: #1e293b !important;
    color: #38bdf8 !important;
    border: 1px solid rgba(56, 189, 248, 0.4) !important;
}

/* Радио карточкалар */
div[role="radiogroup"] label {
    background: rgba(30, 41, 59, 0.7) !important;
    border: 1px solid rgba(56, 189, 248, 0.25) !important;
    border-radius: 12px !important;
    padding: 10px 14px !important;
    color: #f1f5f9 !important;
}
div[role="radiogroup"] label:hover {
    border-color: #38bdf8 !important;
}

/* Прогресс-бар */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #2563eb, #06b6d4) !important;
}
</style>
""", unsafe_allow_html=True)

# Басты баннер
st.markdown("""
    <div class="main-header">
        <span class="badge-3d">● 3D DIGITAL SCHOOL</span>
        <h1>UstazMentor 💻 5-сынып</h1>
        <p>Функционалдық сауаттылық, тесттер, сәйкестендіру және 3D интерактивті тренажерлар</p>
    </div>
""", unsafe_allow_html=True)

# 14 тақырып тізімі
sections_dict = {
    "📁 Бөлім: Ақпарат және компьютер": [
        "1. Эргономика дегеніміз не",
        "2. Эргономика дегеніміз не. Практикалық жұмыс",
        "3. Біздің айналамыздағы ақпарат",
        "4. Интернетте ақпаратты іздеу",
        "5. Интернетте ақпаратты іздеу. Практикалық жұмыс",
        "6. Есептеу техникасының даму тарихы",
        "7. Есептеу техникасының даму тарихы"
    ],
    "📁 Бөлім: Цифрлық кескіндер": [
        "8. Компьютерлік графика және оның түрлері",
        "9. Компьютерлік графика және оның түрлері. Практикалық жұмыс",
        "10. Растрлық кескіндерді құру",
        "11. Растрлық кескіндерді құру. Практикалық жұмыс",
        "12. Растрлық кескіндерді өңдеу құралдары",
        "13. Растрлық кескіндерді өңдеу құралдары. Практикалық жұмыс",
        "14. Графика және жасанды интеллект. Практикалық жұмыс"
    ]
}

external_links = {
    "7. Есептеу техникасының даму тарихы": "https://aliyateacher80-design.github.io/history-game/",
    "12. Растрлық кескіндерді өңдеу құралдары": "https://aliyateacher80-design.github.io/raastr-game5/",
    "13. Растрлық кескіндерді өңдеу құралдары. Практикалық жұмыс": "https://aliyateacher80-design.github.io/ondeu-qurak-prakt/",
    "14. Графика және жасанды интеллект. Практикалық жұмыс": "https://aliyateacher80-design.github.io/graphics-ai-task/"
}

correct_answers = {
    "1. Эргономика дегеніміз не": [
        "Б) 50-70 см", "А) 90-100 градус", "Б) Шынтақ 90 градус бұрыш жасап, үстелмен бір деңгейде болуы керек",
        "В) Жарық сол жақ қапталдан түскені дұрыс (егер оңқай болса)", "Б) Әр 20-30 минут сайын 5 минуттық үзіліс жасап, көз бен денеге жаттығу жасау",
        "А) Ауа алмасуы үшін бос орын болуы және аяққа кедергі жасамауы тиіс", "Б) Көзге зиян келтірмейтін ыңғайлы, орташа жарықтық деңгейі",
        "А) Омыртқа жотасының қисаюына және тез шаршауға әкеледі", "А) Негізгі қатардағы (ФЫВА ЖОЛД) әріптерге сүйреу",
        "А) Адамның еңбек жағдайын, қауіпсіздігі мен тиімділігін"
    ],
    "3. Біздің айналамыздағы ақпарат": [
        "В) Дыбыстық", "А) Екілік код (0 мен 1)", "А) Графикалық / Визуалды", "А) Визуалды (көру арқылы)",
        "А) Электр сигналы бар (ток келді)", "Б) Сыныптағы оқушылар саны — 25", "А) Дыбыстық және сандық (кодталған)",
        "А) Көз, құлақ, мұрын, тіл, тері", "А) Себебі электрондық схемалардың «қосулы» немесе «өшірулі» күйін ажырату ең оңай әрі сенімді жол", "В) Фотосурет — дәмдік"
    ],
    "4. Интернетте ақпаратты іздеу": [
        "А) Арнайы іздеу жүйелерін (Google, Yandex) қолданып, дәрек сұраныс жазу", "А) Тырнақшаға (\"...\")",
        "А) Ресми білім беру порталдарынан, ғылыми энциклопедиялардан", "А) Минус (-) таңбасы", "А) Бірнеше сенімді басқа көздермен салыстырып тексеру арқылы",
        "А) Орфографиялық қателер мен орынсыз тыныс белгілері", "А) Суреттің ажыратымдылығын немесе өлшемін қарау",
        "А) filetype:pdf командасын", "А) Бейтаныс, күмәнді сілтемелерге басып, белгісіз файлдарды жүктеу", "А) Сурет, бейнеролик, карта, дыбыс және құжаттар"
    ],
    "6. Есептеу техникасының даму тарихы": [
        "А) Саусақтары мен тастарды, ағаш таяқшаларын", "А) Абак", "А) Электронды шамдар (электронно-лучевые лампы)",
        "В) 4-ші және одан кейінгі буындар (микропроцессорлар дәуірі)", "А) Көлемін едәуір кішірейтіп, сенімділігін арттырды",
        "А) Ада Лавлейс", "А) Готфрид Лейбниц (және Блез Паскаль)", "А) Транзисторлар", "А) Интегралдық схемалардың (микросхемалардың) пайда болуы",
        "А) Жасанды интеллект, кванттық компьютерлер және нейрожелілер"
    ],
    "8. Компьютерлік графика және оның түрлері": [
        "А) Растрлық және векторлық", "А) Пиксель", "А) Математикалық формулалар мен геометриялық сызықтарға (контурларға)",
        "А) Пиксельдер көрініп, сурет бұлыңғырланады (сапасы жоғалады)", "А) Сапасы ешқашан жоғалмайды, өйткені формула қайта есептеледі",
        "А) RGB (Red, Green, Blue)", "А) CMYK", "А) Adobe Photoshop немесе Paint", "А) CorelDRAW немесе Inkscape", "А) Векторлық графика"
    ],
    "10. Растрлық кескіндерді құру": [
        "А) Тіктөртбұрыш, сопақша (эллипс), сызық, көпбұрыш", "А) Құю (Заливка / Fill with color)", "А) Сызық (Line) немесе Қисық сызық (Curve)",
        "А) Өшіргіш (Eraser)", "А) Мәтін (Text / 'A' әрпі)", "А) Толтыру (Fill) параметрлерін «Бос» немесе «Тек контур» етіп таңдаймыз",
        "А) Ctrl + Z (Болдырмау / Undo)", "А) Түрлі бұрышты геометриялық фигуралар мен сынық сызықтар", "А) .png немесе .jpg",
        "А) Масштабты (Zoom) үлкейтіп, пиксельдерді жақыннан көру"
    ]
}

all_topics = []
for sec, topics in sections_dict.items():
    all_topics.extend(topics)

# Режим таңдау
role = st.radio("Режимді таңдаңыз:", ["👨‍🎓 Оқушы режимі", "👩‍🏫 Мұғалім кабинеті"], horizontal=True)
st.divider()

if role == "👩‍🏫 Мұғалім кабинеті":
    st.subheader("👩‍🏫 Мұғалімнің басқару кабинеті")
    
    with st.expander("📊 Teacher Dashboard — Сыныптар мен нәтижелерді қарау", expanded=True):
        st.markdown("### 🏫 Сыныптар навигаторы")
        selected_class = st.radio("Сыныпты таңдаңыз:", st.session_state.classes_list, horizontal=True)
        
        col_add1, col_add2 = st.columns([3, 1])
        with col_add1:
            new_class_input = st.text_input("Жаңа сынып қосу:", placeholder="Мысалы: 5 «Б»", key="new_class_key")
        with col_add2:
            st.write("")
            st.write("")
            if st.button("➕ Қосу"):
                if new_class_input.strip() and new_class_input.strip() not in st.session_state.classes_list:
                    st.session_state.classes_list.append(new_class_input.strip())
                    st.success(f"{new_class_input} сәтті қосылды!")
                    st.rerun()

        st.markdown(f"#### 📈 {selected_class} сыныбының нәтижелері (Макс: 10 ұпай)")
        class_filtered_db = [r for r in st.session_state.results_db if r.get('grade') == selected_class]
        
        if len(class_filtered_db) > 0:
            for idx, res in enumerate(class_filtered_db, 1):
                score_val = res.get('score_num', 10)
                c1, c2, c3 = st.columns([2, 2, 3])
                with c1:
                    st.write(f"**{idx}. {res['name']}**")
                with c2:
                    st.write(f"Ұпайы: **{res['score']}**")
                with c3:
                    st.progress(min(score_val / 10.0, 1.0))
        else:
            st.info(f"{selected_class} сыныбында әзірге сақталған нәтиже жоқ.")

    st.subheader("⚙️ Сабақ баптаулары")
    save_results_enabled = st.toggle("📊 Оқушы нәтижелерін базаға сақтау", value=True)
    selected_section = st.selectbox("Бөлімді таңдаңыз:", list(sections_dict.keys()))
    selected_topic = st.selectbox("Тақырыпты таңдаңыз:", sections_dict[selected_section])
    timer_val = st.number_input("Сабақ таймері (минут):", value=15)
        
    st.info(f"💡 Таңдалған сабақ: **{selected_topic}** | Сақтау: **{'ҚОСУЛЫ' if save_results_enabled else 'ӨШІРУЛІ'}**")

else:
    st.subheader("👨‍🎓 Оқушы кабинеті")
    col_name, col_class = st.columns([2, 1])
    with col_name:
        student_name = st.text_input("Аты-жөніңізді енгізіңіз (Мысалы: Ерболат А.):", placeholder="Аты-жөніңіз...")
    with col_class:
        student_grade = st.selectbox("Сыныбыңыз:", st.session_state.classes_list)
    
    selected_topic = st.selectbox("Сабақ тақырыбын таңдаңыз:", all_topics)
    st.success(f"🎯 **Ағымдағы сабақ:** {selected_topic}")
    
    is_link_topic = any(selected_topic.startswith(prefix) for prefix in ["7.", "12.", "13.", "14."])
    
    if is_link_topic:
        st.markdown(f"### 🌐 Интерактивті веб-ойын: {selected_topic}")
        game_url = external_links.get(selected_topic, "https://github.com")
        st.markdown(f"👉 **[Тапсырманы / Ойынды ашу 🚀]({game_url})**")
        
        if st.button("✅ Тапсырманы орындап шықтым (Нәтижені тіркеу)"):
            if not student_name.strip():
                st.error("⚠️ Ең алдымен аты-жөніңізді жазыңыз!")
            else:
                st.balloons()
                st.success(f"Құттықтаймыз, {student_name}! Тапсырма тіркелді! 🌟")
                st.session_state.results_db.append({
                    "name": student_name, "grade": student_grade, "topic": selected_topic,
                    "task_type": "Интерактивті веб-ойын", "score_num": 10, "score": "10 / 10 (Орындалды)"
                })
    else:
        tab_test, tab_match, tab_game = st.tabs(["📝 Тест (10 сұрақ)", "🔗 Сәйкестендіру", "💻 Прагматикалық тренажер (10 қадам)"])
        
        with tab_test:
            st.markdown(f"#### Функционалдық тест: {selected_topic}")
            with st.form(key=f"test_{selected_topic}"):
                user_answers = []
                if "1. Эргономика дегеніміз не" in selected_topic:
                    q_list = [
                        st.radio("1. Монитор мен көздің арақашықтығы қандай болуы тиіс?", ["А) 20-30 см", "Б) 50-70 см", "В) 1-1,5 метр"]),
                        st.radio("2. Дұрыс отыру қалпында арқа мен орындықтың бұрышы қандай?", ["А) 90-100 градус", "Б) 45 градус", "В) 180 градус"]),
                        st.radio("3. Білек пен шынтақ қай деңгейде орналасуы тиіс?", ["А) Төмен түсіп тұруы керек", "Б) Шынтақ 90 градус бұрыш жасап, үстелмен бір деңгейде болуы керек", "В) Тік ұстау керек"]),
                        st.radio("4. Жарықтандыру қай жақтан түскені дұрыс?", ["А) Алдынан", "Б) Қараңғы болуы шарт", "В) Жарық сол жақ қапталдан түскені дұрыс (егер оңқай болса)"]),
                        st.radio("5. Оқушы компьютер алдында қанша уақыт сайын үзіліс жасауы керек?", ["А) Орнынан тұрмау", "Б) Әр 20-30 минут сайын 5 минуттық үзіліс жасап, көз бен денеге жаттығу жасау", "В) Жарықты максималды ету"]),
                        st.radio("6. Жүйелік блоктың орналасуына қатысты қауіпсіз ереже?", ["А) Ауа алмасуы үшін бос орын болуы және аяққа кедергі жасамауы тиіс", "Б) Орындықтың үстіне қою", "В) Терезе сыртына қою"]),
                        st.radio("7. Экранның жарықтығы қандай болуы керек?", ["А) Өткір жарық", "Б) Көзге зиян келтірмейтін ыңғайлы, орташа жарықтық деңгейі", "В) Экранды өшіріп қою"]),
                        st.radio("8. Бүкірейіп отыру ағзаға қалай әсер етеді?", ["А) Омыртқа жотасының қисаюына және тез шаршауға әкеледі", "Б) Жылдамдықты арттырады", "В) Еш әсер етпейді"]),
                        st.radio("9. Саусақтардың пернетақтада дұрыс орналасуы?", ["А) Негізгі қатардағы (ФЫВА ЖОЛД) әріптерге сүйреу", "Б) Тек бір саусақпен басу", "В) Кез келген әдіс"]),
                        st.radio("10. Эргономика ғылымы нені зерттейді?", ["А) Адамның еңбек жағдайын, қауіпсіздігі мен тиімділігін", "Б) Тек роботтарды", "В) Интернет жылдамдығын"])
                    ]
                    user_answers.extend(q_list)
                else:
                    st.info("Бұл тақырыпқа сұрақтар бекітілген.")

                if st.form_submit_button("Тестті тексеру және ұпайды есептеу"):
                    if not student_name.strip():
                        st.error("⚠️ Аты-жөніңізді енгізіңіз!")
                    else:
                        score = 0
                        correct_list = correct_answers.get(selected_topic, [])
                        for ua, ca in zip(user_answers, correct_list):
                            if ua == ca:
                                score += 1
                        st.balloons()
                        st.success(f"Құттықтаймыз, {student_name}! Нәтижеңіз: {score} / 10 ұпай 🌟")
                        st.session_state.results_db.append({
                            "name": student_name, "grade": student_grade, "topic": selected_topic,
                            "task_type": "Тест (10 сұрақ)", "score_num": score, "score": f"{score} / 10 ұпай"
                        })

        with tab_match:
            st.markdown(f"#### Сәйкестендіру тапсырмасы: {selected_topic}")
            match_items = ["1. Көз бен монитор", "2. Арқа бұрышы", "3. Үзіліс", "4. Жарық", "5. Орындық биіктігі"]
            match_opts = ["-- Таңдаңыз --", "50-70 см", "90-100 градус", "20-30 минут сайын", "Сол жақтан", "Табан еденге тиюі"]
            
            for item in match_items:
                st.selectbox(f"{item}:", match_opts, key=f"m_{item}")
                
            if st.button("Сәйкестікті растау"):
                if not student_name.strip():
                    st.error("⚠️ Аты-жөніңізді жазыңыз!")
                else:
                    st.balloons()
                    st.success(f"Жарайсың, {student_name}! Сәйкестендіру орындалды! 🎯")

        with tab_game:
            st.markdown(f"#### Прагматикалық тренажер (10 қадам): {selected_topic}")
            step = st.slider("Қадамды таңдаңыз:", 0, 10, 0)
            st.write(f"Орындалу деңгейі: **{step} / 10 қадам**")
            
            if st.button("Қадамды растау / Нәтиже тіркеу"):
                if not student_name.strip():
                    st.error("⚠️ Аты-жөніңізді жазыңыз!")
                else:
                    st.balloons()
                    st.success(f"Құттықтаймыз, {student_name}! Тренажер қадамы тіркелді: {step} / 10 ұпай 🚀")
                    st.session_state.results_db.append({
                        "name": student_name, "grade": student_grade, "topic": selected_topic,
                        "task_type": "Тренажер", "score_num": step, "score": f"{step} / 10 ұпай"
                    })
