import streamlit as st
import json
import os

# Беттің баптаулары
st.set_page_config(
    page_title="UstazMentor - Функционалдық сауаттылық платформасы",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Стильдерді беру
st.markdown("""
<style>
    .main {
        background-color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
</style>
""", unsafe_allow_html=True)

# tasks.json файлынан тапсырмаларды жүктеу функциясы
@st.cache_data
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

tasks_data = load_tasks()

# Басты бет интерфейсі
st.title("🎓 UstazMentor — Информатика мұғаліміне арналған платформа")
st.markdown("---")

# Бүйірлік панель (Sidebar) сынып таңдау үшін
st.sidebar.header("📁 Сыныптар мен модульдер")
grade_option = st.sidebar.selectbox(
    "Сыныпты таңдаңыз:",
    ["5-сынып", "6-сынып", "7-сынып", "8-сынып", "9-сынып", "10-сынып", "11-сынып"]
)

if grade_option == "5-сынып":
    st.subheader("📚 5-сынып: Функционалдық сауаттылық тапсырмалары")
    
    grade_5_tasks = tasks_data.get("grade_5", [])
    
    if grade_5_tasks:
        for task in grade_5_tasks:
            st.markdown(f"### 🔹 Тақырып: {task['topic']}")
            st.info(f"**Жағдаят/Кейс:** {task['case']}")
            
            with st.form(key=f"task_form_{task['id']}"):
                user_answers = {}
                
                for idx, q in enumerate(task['questions']):
                    st.markdown(f"**{idx+1}. {q['text']}**")
                    
                    if q['type'] == 'checkbox':
                        # Чекбокс арқылы бірнеше жауапты таңдау
                        user_answers[idx] = []
                        for opt_idx, opt in enumerate(q['options']):
                            if st.checkbox(opt, key=f"q_{task['id']}_{idx}_{opt_idx}"):
                                user_answers[idx].append(opt_idx)
                                
                    elif q['type'] == 'radio':
                        # Радио батырма арқылы бір ғана дұрыс жауапты таңдау
                        user_answers[idx] = st.radio(
                            "Нұсқалар:", 
                            q['options'], 
                            key=f"q_{task['id']}_{idx}",
                            label_visibility="collapsed"
                        )
                
                submitted = st.form_submit_button("Жауапты тексеру")
                
                if submitted:
                    score = 0
                    total = len(task['questions'])
                    
                    for idx, q in enumerate(task['questions']):
                        if q['type'] == 'checkbox':
                            # Жиынтықтардың сәйкестігін тексеру
                            if set(user_answers[idx]) == set(q['correct']):
                                score += 1
                        elif q['type'] == 'radio':
                            if user_answers[idx] == q['correct']:
                                score += 1
                    
                    if score == total:
                        st.success(f"🎉 Керемет! Барлық жауап ДҰРЫС! ({score}/{total})")
                        st.balloons()
                    else:
                        st.warning(f"⚠️ Кейбір жауаптар қате немесе толық емес. Ұпай: {score}/{total}. Қайта көріңіз!")
    else:
        st.info("Бұл сыныпқа әзірге тапсырмалар қосылған жоқ.")
else:
    st.subheader(f"📚 {grade_option}")
    st.info("Бұл сыныптың модульдері мен практикалық тапсырмалары дайындалу үстінде...")
