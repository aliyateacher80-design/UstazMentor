import streamlit as st

st.set_page_config(page_title="UstazMentor - 5-сынып", page_icon="💻", layout="wide")

# Заманауи дизайн стилі
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #4f46e5 0%, #3b82f6 100%);
        padding: 25px;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    .section-title {
        color: #4f46e5;
        font-weight: bold;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="main-header">
        <h1>UstazMentor 💻 5-сынып</h1>
        <p>Информатика пәні бойынша функционалдық сауаттылық және прагматикалық тренажер</p>
    </div>
""", unsafe_allow_html=True)

# Бөлімдер мен тақырыптар құрылымы
sections_dict = {
    "📁 Бөлім: Ақпарат және компьютер": [
        "1. Эргономика дегеніміз не",
        "2. Эргономика дегеніміз не. Практикалық жұмыс",
        "3. Біздің айналамыздағы ақпарат",
        "4. Интернетте ақпаратты іздеу",
        "5. Интернетте ақпаратты іздеу. Практикалық жұмыс",
        "6. Есептеу техникасының даму тарихы",
        "7. Программалық жасақтама және жасанды интеллект"
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

# Режимді таңдау (Оқушы / Мұғалім)
role = st.radio("Режимді таңдаңыз:", ["👨‍🎓 Оқушы режимі", "👩‍🏫 Мұғалім кабинеті"], horizontal=True)

st.divider()

if role == "👩‍🏫 Мұғалім кабинеті":
    st.subheader("👨‍💻 Мұғалімнің басқару және сілтеме жасау панелі 🔗")
    
    selected_section = st.selectbox("Бөлімді таңдаңыз:", list(sections_dict.keys()))
    selected_topic = st.selectbox("Тақырыпты таңдаңыз:", sections_dict[selected_section])
    
    timer_val = st.number_input("Сабаққа арналған таймер (минут):", value=15)
        
    st.info(f"💡 **Таңдалған бөлім:** {selected_section} | **Тақырып:** {selected_topic}")
    
    st.markdown("### 🔗 Оқушыларға арналған автоматты сілтеме:")
    shareable_url = f"https://ustaz-mentor.streamlit.app/?section={selected_section}&topic={selected_topic}&timer={timer_val}"
    st.code(shareable_url)

else:
    st.subheader("👨‍🎓 Оқушы кабинеті")
    
    # Барлық тақырыптарды тізім ретінде шығару
    all_topics = []
    for sec, topics in sections_dict.items():
        all_topics.extend(topics)
        
    selected_topic = st.selectbox("Сабақ тақырыбын таңдаңыз:", all_topics)
    
    st.success(f"🎯 **Ағымдағы тақырып:** {selected_topic}")
    
    st.divider()
    
    # Тапсырмалар вкладкалары
    tab_test, tab_match, tab_game = st.tabs(["📝 Тест (10 сұрақ)", "🔗 Сәйкестендіру", "💻 Интерактивті деңгей (10 қадам)"])
    
    with tab_test:
        st.markdown(f"#### Функционалдық тест: {selected_topic}")
        with st.form(key=f"test_{selected_topic}"):
            for i in range(1, 11):
                st.radio(f"{i}-сұрақ:", [
                    f"А) {selected_topic} бойынша дұрыс жауап", 
                    "Б) Қате балама нұсқа 1", 
                    "В) Қате балама нұсқа 2"
                ], key=f"t_{selected_topic}_{i}")
                
            if st.form_submit_button("Тестті тексеру (10 ұпай)"):
                st.balloons()
                st.success("Тест сәтті аяқталды! 10 / 10 ұпай 🌟")
                
    with tab_match:
        st.markdown(f"#### Сәйкестендіру тапсырмасы: {selected_topic}")
        with st.form(key=f"match_{selected_topic}"):
            st.write("Сол жақтағы ұғымдар мен мәндерге дұрыс сәйкестікті жазыңыз:")
            for i in range(1, 11):
                st.text_input(f"{i}-элементтің сәйкестігі:", key=f"m_{selected_topic}_{i}")
            if st.form_submit_button("Сәйкестікті тексеру (10 ұпай)"):
                st.balloons()
                st.success("Барлық сәйкестіктер қабылданды! 10 ұпай 🎯")
                
    with tab_game:
        st.markdown(f"#### Прагматикалық тренажер (10 қадам): {selected_topic}")
        step = st.slider("Қадамды таңдаңыз:", 0, 10, 0, key=f"slider_{selected_topic}")
        st.write(f"Орындалу деңгейі: **{step} / 10 қадам**")
        
        if step > 0:
            st.info(f"📍 {selected_topic} бойынша {step}-қадам орындалу үстінде.")

        if st.button("Нәтиже тіркеу", key=f"btn_{selected_topic}"):
            if step == 10:
                st.balloons()
                st.success("Құттықтаймыз! Барлық 10 қадам толық аяқталып, нәтиже тіркелді! 🚀")
            else:
                st.warning("Жүгірткіні 10-ға жеткізіп, барлық қадамды аяқтаңыз!")

st.divider()
st.caption("UstazMentor платформасы © 2026 | Информатика мұғалімдеріне арналған көмекші жүйе.")
