import streamlit as st
import json
from pathlib import Path
from abc import ABC, abstractmethod

# ─── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="EduTrack — Student Management",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── GLOBAL CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Space+Grotesk:wght@500;700&display=swap');

/* ── Reset & Base ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ── Background ── */
.stApp {
    background: #0F1117;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1A1D2E 0%, #0F1117 100%);
    border-right: 1px solid #2A2D3E;
}
[data-testid="stSidebar"] * {
    color: #E2E8F0 !important;
}

/* ── Hero Banner ── */
.hero-banner {
    background: linear-gradient(135deg, #6C63FF 0%, #3B82F6 50%, #06B6D4 100%);
    border-radius: 16px;
    padding: 36px 40px;
    margin-bottom: 28px;
    display: flex;
    align-items: center;
    gap: 20px;
}
.hero-banner h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: #FFFFFF !important;
    margin: 0;
    letter-spacing: -0.5px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.25);
}
.hero-banner p {
    color: rgba(255,255,255,0.88) !important;
    font-size: 1rem;
    margin: 6px 0 0 0;
    font-weight: 500;
}

/* ── Stat Cards ── */
.stat-row {
    display: flex;
    gap: 16px;
    margin-bottom: 28px;
}
.stat-card {
    flex: 1;
    border-radius: 12px;
    padding: 22px 24px;
    display: flex;
    flex-direction: column;
    gap: 6px;
}
.stat-card.blue  { background: linear-gradient(135deg, #1E3A8A, #2563EB); }
.stat-card.purple{ background: linear-gradient(135deg, #4C1D95, #7C3AED); }
.stat-card.teal  { background: linear-gradient(135deg, #134E4A, #0D9488); }
.stat-card .stat-label {
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: rgba(255,255,255,0.72) !important;
}
.stat-card .stat-number {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.4rem;
    font-weight: 700;
    color: #FFFFFF !important;
    line-height: 1;
}
.stat-card .stat-sub {
    font-size: 0.82rem;
    color: rgba(255,255,255,0.65) !important;
    font-weight: 500;
}

/* ── Section Card ── */
.section-card {
    background: #1A1D2E;
    border: 1px solid #2A2D3E;
    border-radius: 14px;
    padding: 28px 30px;
    margin-bottom: 20px;
}
.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: #FFFFFF !important;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-title .pill {
    background: #6C63FF22;
    color: #A78BFA !important;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.8px;
    padding: 3px 10px;
    border-radius: 20px;
    text-transform: uppercase;
}

/* ── Input Overrides ── */
[data-testid="stTextInput"] label,
[data-testid="stNumberInput"] label,
[data-testid="stSelectbox"] label {
    color: #94A3B8 !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 0.6px;
}
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input {
    background: #0F1117 !important;
    border: 1.5px solid #2A2D3E !important;
    border-radius: 8px !important;
    color: #E2E8F0 !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stNumberInput"] input:focus {
    border-color: #6C63FF !important;
    box-shadow: 0 0 0 3px #6C63FF22 !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #6C63FF, #3B82F6) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.4px;
    border: none !important;
    border-radius: 8px !important;
    padding: 10px 24px !important;
    width: 100% !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 14px rgba(108,99,255,0.35) !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(108,99,255,0.5) !important;
}

/* ── Success / Error / Info boxes ── */
.stSuccess {
    background: #052E16 !important;
    border-left: 4px solid #22C55E !important;
    border-radius: 8px !important;
    color: #86EFAC !important;
}
.stError {
    background: #1C0A0A !important;
    border-left: 4px solid #EF4444 !important;
    border-radius: 8px !important;
    color: #FCA5A5 !important;
}
.stInfo {
    background: #0C1A2E !important;
    border-left: 4px solid #3B82F6 !important;
    border-radius: 8px !important;
    color: #93C5FD !important;
}
.stWarning {
    background: #1C1100 !important;
    border-left: 4px solid #F59E0B !important;
    color: #FCD34D !important;
}

/* ── Tabs ── */
[data-testid="stTabs"] [data-baseweb="tab-list"] {
    background: #1A1D2E !important;
    border-radius: 10px !important;
    padding: 4px !important;
    gap: 4px !important;
    border: 1px solid #2A2D3E;
}
[data-testid="stTabs"] [data-baseweb="tab"] {
    background: transparent !important;
    color: #64748B !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    border-radius: 7px !important;
    padding: 8px 18px !important;
    border: none !important;
}
[data-testid="stTabs"] [aria-selected="true"] {
    background: linear-gradient(135deg, #6C63FF, #3B82F6) !important;
    color: #FFFFFF !important;
}

/* ── Dataframe / Table ── */
[data-testid="stDataFrame"] {
    border: 1px solid #2A2D3E !important;
    border-radius: 10px !important;
    overflow: hidden;
}

/* ── Profile Card ── */
.profile-card {
    background: linear-gradient(135deg, #1E1B4B, #1A1D2E);
    border: 1px solid #3730A3;
    border-radius: 14px;
    padding: 24px 26px;
    margin-bottom: 16px;
}
.profile-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: #FFFFFF !important;
    margin-bottom: 4px;
}
.profile-role {
    display: inline-block;
    background: #6C63FF33;
    color: #A78BFA !important;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 3px 12px;
    border-radius: 20px;
    margin-bottom: 14px;
}
.profile-row {
    display: flex;
    gap: 24px;
    flex-wrap: wrap;
}
.profile-field {
    display: flex;
    flex-direction: column;
    gap: 2px;
}
.profile-field .field-label {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #64748B !important;
}
.profile-field .field-value {
    font-size: 0.95rem;
    font-weight: 600;
    color: #E2E8F0 !important;
}

/* ── Grade Badge ── */
.grade-badge {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 8px;
    font-weight: 700;
    font-size: 0.88rem;
    margin: 3px;
}
.grade-A { background: #052E16; color: #4ADE80 !important; border: 1px solid #16A34A; }
.grade-B { background: #0C1A2E; color: #60A5FA !important; border: 1px solid #2563EB; }
.grade-C { background: #1C1100; color: #FCD34D !important; border: 1px solid #D97706; }
.grade-D { background: #1C0A0A; color: #F87171 !important; border: 1px solid #DC2626; }

/* ── Divider ── */
.custom-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #2A2D3E, transparent);
    margin: 20px 0;
}

/* ── Sidebar Nav Buttons ── */
[data-testid="stSidebar"] .stButton > button {
    background: #1A1D2E !important;
    border: 1px solid #2A2D3E !important;
    box-shadow: none !important;
    text-align: left !important;
    justify-content: flex-start !important;
    color: #94A3B8 !important;
    font-weight: 600 !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background: #6C63FF22 !important;
    border-color: #6C63FF !important;
    color: #A78BFA !important;
    transform: none !important;
}

/* ── Radio ── */
[data-testid="stRadio"] label { color: #94A3B8 !important; font-weight: 600 !important; }
[data-testid="stRadio"] [data-testid="stMarkdownContainer"] p { color: #E2E8F0 !important; }

/* Headings inside main area */
h2, h3 { color: #F1F5F9 !important; font-family: 'Space Grotesk', sans-serif !important; }
p, li { color: #94A3B8 !important; }

/* Make all text clearly readable */
.stMarkdown p, .stMarkdown li { color: #CBD5E1 !important; }

/* ── Metric overrides ── */
[data-testid="metric-container"] {
    background: #1A1D2E;
    border: 1px solid #2A2D3E;
    border-radius: 10px;
    padding: 14px 18px;
}
[data-testid="metric-container"] [data-testid="stMetricLabel"] {
    color: #64748B !important;
    font-size: 0.78rem !important;
    font-weight: 700 !important;
    text-transform: uppercase;
    letter-spacing: 0.6px;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)

# ─── DATA LAYER ────────────────────────────────────────────────────────────────
DATABASE = "school_data.json"
DEFAULT_DATA = {"students": [], "teachers": []}

def load_data():
    if Path(DATABASE).exists():
        with open(DATABASE, 'r') as f:
            content = f.read()
            if content:
                return json.loads(content)
    return {"students": [], "teachers": []}

def save_data(data):
    with open(DATABASE, 'w') as f:
        json.dump(data, f, indent=4)

def email_ok(email):
    return "@" in email and "." in email

if "data" not in st.session_state:
    st.session_state.data = load_data()

data = st.session_state.data

# ─── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding: 10px 0 20px 0;'>
        <div style='font-family: Space Grotesk, sans-serif; font-size: 1.35rem; font-weight: 700; color: #FFFFFF;'>🎓 EduTrack</div>
        <div style='font-size: 0.78rem; color: #475569; font-weight: 500; margin-top: 2px;'>School Management System</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<div style='font-size:0.72rem; font-weight:700; letter-spacing:1px; color:#475569; text-transform:uppercase; margin-bottom:8px;'>Navigation</div>", unsafe_allow_html=True)

    page = st.radio(
        "",
        ["🏠  Dashboard", "🎓  Students", "👨‍🏫  Teachers", "📊  Grades"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    students_count = len(data['students'])
    teachers_count = len(data['teachers'])
    total_grades = sum(len(s.get('grades', {})) for s in data['students'])

    st.markdown(f"""
    <div style='background:#0F1117; border:1px solid #2A2D3E; border-radius:10px; padding:14px 16px;'>
        <div style='font-size:0.72rem; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:#475569; margin-bottom:10px;'>Quick Stats</div>
        <div style='display:flex; justify-content:space-between; margin-bottom:6px;'>
            <span style='color:#94A3B8; font-size:0.85rem; font-weight:500;'>Students</span>
            <span style='color:#A78BFA; font-weight:700; font-size:0.9rem;'>{students_count}</span>
        </div>
        <div style='display:flex; justify-content:space-between; margin-bottom:6px;'>
            <span style='color:#94A3B8; font-size:0.85rem; font-weight:500;'>Teachers</span>
            <span style='color:#60A5FA; font-weight:700; font-size:0.9rem;'>{teachers_count}</span>
        </div>
        <div style='display:flex; justify-content:space-between;'>
            <span style='color:#94A3B8; font-size:0.85rem; font-weight:500;'>Grade Records</span>
            <span style='color:#4ADE80; font-weight:700; font-size:0.9rem;'>{total_grades}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── PAGE: DASHBOARD ───────────────────────────────────────────────────────────
if page == "🏠  Dashboard":
    st.markdown("""
    <div class='hero-banner'>
        <div style='font-size:3rem;'>🎓</div>
        <div>
            <h1>EduTrack Dashboard</h1>
            <p>Manage students, teachers, and academic records in one place.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='stat-row'>
        <div class='stat-card blue'>
            <div class='stat-label'>Total Students</div>
            <div class='stat-number'>{students_count}</div>
            <div class='stat-sub'>Registered this session</div>
        </div>
        <div class='stat-card purple'>
            <div class='stat-label'>Total Teachers</div>
            <div class='stat-number'>{teachers_count}</div>
            <div class='stat-sub'>Faculty members</div>
        </div>
        <div class='stat-card teal'>
            <div class='stat-label'>Grade Records</div>
            <div class='stat-number'>{total_grades}</div>
            <div class='stat-sub'>Across all subjects</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>📋 Recent Students <span class='pill'>Latest 5</span></div>", unsafe_allow_html=True)
        if data['students']:
            for s in data['students'][-5:][::-1]:
                grades = s.get('grades', {})
                avg = sum(grades.values()) / len(grades) if grades else 0
                color = "#4ADE80" if avg >= 75 else "#FCD34D" if avg >= 50 else "#F87171"
                st.markdown(f"""
                <div style='display:flex; justify-content:space-between; align-items:center;
                            padding:10px 14px; background:#0F1117; border-radius:8px; margin-bottom:8px;
                            border:1px solid #2A2D3E;'>
                    <div>
                        <div style='color:#E2E8F0; font-weight:700; font-size:0.92rem;'>{s['name']}</div>
                        <div style='color:#475569; font-size:0.78rem; font-weight:500;'>Roll #{s['roll_no']} · Age {s['age']}</div>
                    </div>
                    <div style='text-align:right;'>
                        <div style='color:{color}; font-weight:800; font-size:1.05rem; font-family:Space Grotesk,sans-serif;'>{avg:.1f}</div>
                        <div style='color:#475569; font-size:0.72rem;'>avg marks</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No students registered yet.")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>👨‍🏫 Recent Teachers <span class='pill'>Latest 5</span></div>", unsafe_allow_html=True)
        if data['teachers']:
            for t in data['teachers'][-5:][::-1]:
                st.markdown(f"""
                <div style='display:flex; justify-content:space-between; align-items:center;
                            padding:10px 14px; background:#0F1117; border-radius:8px; margin-bottom:8px;
                            border:1px solid #2A2D3E;'>
                    <div>
                        <div style='color:#E2E8F0; font-weight:700; font-size:0.92rem;'>{t['name']}</div>
                        <div style='color:#475569; font-size:0.78rem; font-weight:500;'>ID #{t['emp_id']} · {t['subject']}</div>
                    </div>
                    <div style='background:#7C3AED22; border:1px solid #7C3AED; border-radius:6px;
                                padding:3px 10px; color:#A78BFA; font-size:0.75rem; font-weight:700;'>
                        FACULTY
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No teachers registered yet.")
        st.markdown("</div>", unsafe_allow_html=True)

# ─── PAGE: STUDENTS ─────────────────────────────────────────────────────────────
elif page == "🎓  Students":
    st.markdown("""
    <div class='hero-banner' style='background:linear-gradient(135deg,#1E3A8A,#2563EB,#0891B2);'>
        <div style='font-size:2.5rem;'>🎓</div>
        <div>
            <h1>Student Management</h1>
            <p>Register students and view their profiles.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["  ➕  Register Student  ", "  🔍  View Profile  "])

    # ── Register ──
    with tab1:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>📝 New Student Registration</div>", unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            s_name = st.text_input("Full Name", placeholder="e.g. Rahul Sharma", key="s_name")
            s_roll = st.number_input("Roll Number", min_value=1, step=1, key="s_roll")
        with c2:
            s_age = st.number_input("Age", min_value=5, max_value=30, step=1, value=18, key="s_age")
            s_email = st.text_input("Email Address", placeholder="student@example.com", key="s_email")

        st.markdown("<div style='margin-top:6px;'></div>", unsafe_allow_html=True)

        if st.button("Register Student →", key="reg_stud"):
            if not s_name.strip():
                st.error("⚠️  Name cannot be empty.")
            elif not email_ok(s_email):
                st.error("⚠️  Enter a valid email address.")
            elif any(s['roll_no'] == s_roll for s in data['students']):
                st.warning("⚠️  A student with this roll number already exists.")
            else:
                data['students'].append({
                    "name": s_name.strip(),
                    "roll_no": s_roll,
                    "age": s_age,
                    "email": s_email.strip(),
                    "grades": {}
                })
                save_data(data)
                st.session_state.data = data
                st.success(f"✅  {s_name} registered successfully!")
        st.markdown("</div>", unsafe_allow_html=True)

        if data['students']:
            st.markdown("<div class='section-card'>", unsafe_allow_html=True)
            st.markdown("<div class='section-title'>👥 All Students <span class='pill'>" + str(len(data['students'])) + " total</span></div>", unsafe_allow_html=True)
            rows = []
            for s in data['students']:
                grades = s.get('grades', {})
                avg = sum(grades.values()) / len(grades) if grades else 0
                rows.append({
                    "Name": s['name'],
                    "Roll No": s['roll_no'],
                    "Age": s['age'],
                    "Email": s['email'],
                    "Subjects": len(grades),
                    "Avg Marks": f"{avg:.1f}"
                })
            import pandas as pd
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
            st.markdown("</div>", unsafe_allow_html=True)

    # ── View Profile ──
    with tab2:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>🔍 Search Student Profile</div>", unsafe_allow_html=True)

        search_roll = st.number_input("Enter Roll Number", min_value=1, step=1, key="view_roll")

        if st.button("Find Student →", key="find_stud"):
            found = next((s for s in data['students'] if s['roll_no'] == search_roll), None)
            if found:
                grades = found.get('grades', {})
                avg = sum(grades.values()) / len(grades) if grades else 0

                def grade_class(m):
                    if m >= 80: return "grade-A"
                    elif m >= 65: return "grade-B"
                    elif m >= 50: return "grade-C"
                    else: return "grade-D"

                grade_html = "".join(
                    f"<span class='grade-badge {grade_class(v)}'>{k}: {v}</span>"
                    for k, v in grades.items()
                ) if grades else "<span style='color:#475569;'>No grades recorded</span>"

                avg_color = "#4ADE80" if avg >= 75 else "#FCD34D" if avg >= 50 else "#F87171"

                st.markdown(f"""
                <div class='profile-card'>
                    <div class='profile-name'>{found['name']}</div>
                    <div class='profile-role'>Student</div>
                    <div class='profile-row'>
                        <div class='profile-field'>
                            <span class='field-label'>Roll Number</span>
                            <span class='field-value'>#{found['roll_no']}</span>
                        </div>
                        <div class='profile-field'>
                            <span class='field-label'>Age</span>
                            <span class='field-value'>{found['age']} years</span>
                        </div>
                        <div class='profile-field'>
                            <span class='field-label'>Email</span>
                            <span class='field-value'>{found['email']}</span>
                        </div>
                        <div class='profile-field'>
                            <span class='field-label'>Average</span>
                            <span class='field-value' style='color:{avg_color};'>{avg:.1f} / 100</span>
                        </div>
                    </div>
                    <div class='custom-divider'></div>
                    <div style='font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:0.8px; color:#475569; margin-bottom:8px;'>Subject Grades</div>
                    <div>{grade_html}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error(f"No student found with Roll No {search_roll}.")
        st.markdown("</div>", unsafe_allow_html=True)

# ─── PAGE: TEACHERS ─────────────────────────────────────────────────────────────
elif page == "👨‍🏫  Teachers":
    st.markdown("""
    <div class='hero-banner' style='background:linear-gradient(135deg,#4C1D95,#7C3AED,#A855F7);'>
        <div style='font-size:2.5rem;'>👨‍🏫</div>
        <div>
            <h1>Teacher Management</h1>
            <p>Register faculty and view teacher profiles.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["  ➕  Register Teacher  ", "  🔍  View Profile  "])

    with tab1:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>📝 New Teacher Registration</div>", unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            t_name = st.text_input("Full Name", placeholder="e.g. Dr. Priya Singh", key="t_name")
            t_emp = st.number_input("Employee ID", min_value=1, step=1, key="t_emp")
        with c2:
            t_age = st.number_input("Age", min_value=21, max_value=70, step=1, value=35, key="t_age")
            t_email = st.text_input("Email Address", placeholder="teacher@school.com", key="t_email")

        t_subject = st.text_input("Specialization Subject", placeholder="e.g. Mathematics, Physics", key="t_subject")

        st.markdown("<div style='margin-top:6px;'></div>", unsafe_allow_html=True)

        if st.button("Register Teacher →", key="reg_teach"):
            if not t_name.strip():
                st.error("⚠️  Name cannot be empty.")
            elif not email_ok(t_email):
                st.error("⚠️  Enter a valid email address.")
            elif not t_subject.strip():
                st.error("⚠️  Subject cannot be empty.")
            elif any(t['emp_id'] == t_emp for t in data['teachers']):
                st.warning("⚠️  A teacher with this Employee ID already exists.")
            else:
                data['teachers'].append({
                    "name": t_name.strip(),
                    "email": t_email.strip(),
                    "emp_id": t_emp,
                    "age": t_age,
                    "subject": t_subject.strip()
                })
                save_data(data)
                st.session_state.data = data
                st.success(f"✅  {t_name} registered successfully!")
        st.markdown("</div>", unsafe_allow_html=True)

        if data['teachers']:
            st.markdown("<div class='section-card'>", unsafe_allow_html=True)
            st.markdown("<div class='section-title'>👥 All Teachers <span class='pill'>" + str(len(data['teachers'])) + " total</span></div>", unsafe_allow_html=True)
            import pandas as pd
            rows = [{"Name": t['name'], "Emp ID": t['emp_id'], "Age": t['age'], "Email": t['email'], "Subject": t['subject']} for t in data['teachers']]
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
            st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>🔍 Search Teacher Profile</div>", unsafe_allow_html=True)

        search_emp = st.number_input("Enter Employee ID", min_value=1, step=1, key="view_emp")

        if st.button("Find Teacher →", key="find_teach"):
            found = next((t for t in data['teachers'] if t['emp_id'] == search_emp), None)
            if found:
                st.markdown(f"""
                <div class='profile-card' style='background:linear-gradient(135deg,#2E1065,#1A1D2E); border-color:#6D28D9;'>
                    <div class='profile-name'>{found['name']}</div>
                    <div class='profile-role' style='background:#7C3AED33; color:#C4B5FD;'>Faculty</div>
                    <div class='profile-row'>
                        <div class='profile-field'>
                            <span class='field-label'>Employee ID</span>
                            <span class='field-value'>#{found['emp_id']}</span>
                        </div>
                        <div class='profile-field'>
                            <span class='field-label'>Age</span>
                            <span class='field-value'>{found['age']} years</span>
                        </div>
                        <div class='profile-field'>
                            <span class='field-label'>Email</span>
                            <span class='field-value'>{found['email']}</span>
                        </div>
                        <div class='profile-field'>
                            <span class='field-label'>Specialization</span>
                            <span class='field-value' style='color:#A78BFA;'>{found['subject']}</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error(f"No teacher found with Employee ID {search_emp}.")
        st.markdown("</div>", unsafe_allow_html=True)

# ─── PAGE: GRADES ───────────────────────────────────────────────────────────────
elif page == "📊  Grades":
    st.markdown("""
    <div class='hero-banner' style='background:linear-gradient(135deg,#134E4A,#0D9488,#0891B2);'>
        <div style='font-size:2.5rem;'>📊</div>
        <div>
            <h1>Grade Management</h1>
            <p>Add and review subject-wise marks for students.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["  ➕  Add Grade  ", "  📋  Grade Report  "])

    with tab1:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>✏️ Enter Marks</div>", unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        with c1:
            g_roll = st.number_input("Student Roll Number", min_value=1, step=1, key="g_roll")
        with c2:
            g_subject = st.text_input("Subject Name", placeholder="e.g. Mathematics", key="g_subject")
        with c3:
            g_marks = st.number_input("Marks", min_value=0, max_value=100, step=1, key="g_marks")

        st.markdown("<div style='margin-top:6px;'></div>", unsafe_allow_html=True)

        if st.button("Save Grade →", key="save_grade"):
            target = next((s for s in data['students'] if s['roll_no'] == g_roll), None)
            if not target:
                st.error(f"⚠️  No student found with Roll No {g_roll}.")
            elif not g_subject.strip():
                st.error("⚠️  Subject name cannot be empty.")
            else:
                target['grades'][g_subject.strip()] = g_marks
                save_data(data)
                st.session_state.data = data
                st.success(f"✅  Grade saved — {target['name']}: {g_subject} = {g_marks}/100")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>📋 Full Grade Report <span class='pill'>All Students</span></div>", unsafe_allow_html=True)

        students_with_grades = [s for s in data['students'] if s.get('grades')]

        if not students_with_grades:
            st.info("No grades recorded yet. Add grades from the 'Add Grade' tab.")
        else:
            for s in students_with_grades:
                grades = s['grades']
                avg = sum(grades.values()) / len(grades)
                avg_color = "#4ADE80" if avg >= 75 else "#FCD34D" if avg >= 50 else "#F87171"

                def g_class(m):
                    if m >= 80: return "grade-A"
                    elif m >= 65: return "grade-B"
                    elif m >= 50: return "grade-C"
                    else: return "grade-D"

                badges = "".join(f"<span class='grade-badge {g_class(v)}'>{k}: {v}</span>" for k, v in grades.items())

                st.markdown(f"""
                <div style='background:#0F1117; border:1px solid #2A2D3E; border-radius:12px;
                            padding:16px 20px; margin-bottom:12px;'>
                    <div style='display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:10px;'>
                        <div>
                            <div style='color:#F1F5F9; font-weight:700; font-size:1rem; font-family:Space Grotesk,sans-serif;'>{s['name']}</div>
                            <div style='color:#475569; font-size:0.78rem; font-weight:500;'>Roll #{s['roll_no']}</div>
                        </div>
                        <div style='text-align:right;'>
                            <div style='color:{avg_color}; font-weight:800; font-size:1.3rem; font-family:Space Grotesk,sans-serif;'>{avg:.1f}</div>
                            <div style='color:#475569; font-size:0.72rem;'>Average</div>
                        </div>
                    </div>
                    <div>{badges}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        if students_with_grades:
            st.markdown("<div class='section-card'>", unsafe_allow_html=True)
            st.markdown("<div class='section-title'>🏆 Class Leaderboard</div>", unsafe_allow_html=True)
            import pandas as pd
            leaderboard = []
            for s in data['students']:
                grades = s.get('grades', {})
                if grades:
                    avg = sum(grades.values()) / len(grades)
                    leaderboard.append({"Rank": 0, "Name": s['name'], "Roll No": s['roll_no'], "Subjects": len(grades), "Average": round(avg, 1)})
            leaderboard.sort(key=lambda x: x['Average'], reverse=True)
            for i, row in enumerate(leaderboard):
                row['Rank'] = f"{'🥇' if i==0 else '🥈' if i==1 else '🥉' if i==2 else str(i+1)}"
            st.dataframe(pd.DataFrame(leaderboard), use_container_width=True, hide_index=True)
            st.markdown("</div>", unsafe_allow_html=True)