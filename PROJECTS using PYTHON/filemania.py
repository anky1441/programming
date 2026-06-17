import streamlit as st
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FILE MAFIA",
    page_icon="🔫",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────────────────────────────────────
#  CSS  –  HIGH CONTRAST MAFIA THEME
#  Background : #1A1A2E  (deep navy)
#  Card bg    : #16213E  (slightly lighter navy)
#  Input bg   : #0F3460  (rich dark blue)
#  Primary    : #E94560  (vivid crimson-red)
#  Gold       : #F5A623  (warm amber/gold)
#  Text main  : #FFFFFF  (pure white)
#  Text muted : #B8C5D6  (light steel blue)
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700&display=swap');

/* ── FULL APP BACKGROUND ── */
.stApp {
    background: linear-gradient(135deg, #1A1A2E 0%, #16213E 50%, #0F3460 100%) !important;
    min-height: 100vh;
}

/* Hide streamlit default elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1rem !important; max-width: 760px !important; }

/* ── GLOBAL TEXT ── */
html, body, p, div, span, li {
    color: #FFFFFF !important;
    font-family: 'Inter', sans-serif !important;
}

/* ── HERO ── */
.hero-wrap {
    text-align: center;
    padding: 2.5rem 1rem 0.5rem;
}
.hero-title {
    font-family: 'Bebas Neue', cursive !important;
    font-size: 5.5rem;
    letter-spacing: 0.22em;
    line-height: 1;
    margin: 0;
    background: linear-gradient(90deg, #F5A623 0%, #FFD580 50%, #F5A623 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 0 24px rgba(245,166,35,0.35));
}
.hero-sub {
    font-family: 'Inter', sans-serif;
    font-size: 0.85rem;
    font-weight: 600;
    letter-spacing: 0.5em;
    color: #E94560 !important;
    text-transform: uppercase;
    margin-top: 0.5rem;
}
.hero-line {
    height: 2px;
    background: linear-gradient(90deg, transparent, #E94560 30%, #F5A623 70%, transparent);
    margin: 1.5rem auto;
    max-width: 500px;
    border-radius: 2px;
}

/* ── OPERATION CARDS ── */
.op-card {
    background: rgba(22, 33, 62, 0.95) !important;
    border: 1px solid rgba(233,69,96,0.35) !important;
    border-top: 3px solid #E94560 !important;
    border-radius: 10px !important;
    padding: 1.8rem 2rem !important;
    margin-bottom: 0.5rem !important;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4), 0 0 0 1px rgba(245,166,35,0.05) !important;
}
.card-tag {
    display: inline-block;
    background: rgba(233,69,96,0.15);
    border: 1px solid rgba(233,69,96,0.5);
    color: #E94560 !important;
    font-family: 'Inter', sans-serif;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    padding: 0.2rem 0.8rem;
    border-radius: 20px;
    margin-bottom: 0.8rem;
}
.card-heading {
    font-family: 'Bebas Neue', cursive !important;
    font-size: 2rem !important;
    letter-spacing: 0.12em !important;
    color: #FFFFFF !important;
    margin: 0.3rem 0 1.2rem 0 !important;
    line-height: 1 !important;
}
.card-heading span { color: #F5A623 !important; }

/* ── INPUT FIELDS ── */
.stTextInput > div > div > input {
    background-color: rgba(15, 52, 96, 0.8) !important;
    border: 1.5px solid rgba(233,69,96,0.4) !important;
    border-radius: 6px !important;
    color: #FFFFFF !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    padding: 0.6rem 0.9rem !important;
    caret-color: #F5A623 !important;
}
.stTextInput > div > div > input::placeholder { color: #7A8FAF !important; }
.stTextInput > div > div > input:focus {
    border-color: #E94560 !important;
    box-shadow: 0 0 0 3px rgba(233,69,96,0.2) !important;
}

.stTextArea > div > div > textarea {
    background-color: rgba(15, 52, 96, 0.8) !important;
    border: 1.5px solid rgba(233,69,96,0.4) !important;
    border-radius: 6px !important;
    color: #FFFFFF !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.93rem !important;
    caret-color: #F5A623 !important;
    line-height: 1.6 !important;
}
.stTextArea > div > div > textarea::placeholder { color: #7A8FAF !important; }
.stTextArea > div > div > textarea:focus {
    border-color: #E94560 !important;
    box-shadow: 0 0 0 3px rgba(233,69,96,0.2) !important;
}

/* ── LABELS above inputs ── */
.stTextInput label > div > p,
.stTextArea label > div > p,
.stTextInput label p,
.stTextArea label p {
    color: #B8C5D6 !important;
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
}

/* ── RADIO ── */
div[data-testid="stRadio"] label p {
    color: #FFFFFF !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
}
div[data-testid="stRadio"] > label > div > p {
    color: #B8C5D6 !important;
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
}
div[data-testid="stRadio"] > div {
    gap: 0.5rem !important;
}

/* ── CHECKBOX ── */
div[data-testid="stCheckbox"] label p {
    color: #FFD580 !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
}

/* ── BUTTONS ── */
.stButton > button {
    background: linear-gradient(135deg, #C0392B, #E94560) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 6px !important;
    font-family: 'Bebas Neue', cursive !important;
    font-size: 1.05rem !important;
    letter-spacing: 0.2em !important;
    padding: 0.6rem 2.2rem !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 16px rgba(233,69,96,0.4) !important;
    width: 100% !important;
    margin-top: 0.5rem !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #E94560, #FF6B8A) !important;
    box-shadow: 0 6px 24px rgba(233,69,96,0.6) !important;
    transform: translateY(-2px) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── TABS ── */
div[data-testid="stTabs"] {
    background: rgba(22,33,62,0.6) !important;
    border-radius: 10px 10px 0 0 !important;
    padding: 0 !important;
}
div[data-testid="stTabs"] button {
    font-family: 'Bebas Neue', cursive !important;
    font-size: 1.05rem !important;
    letter-spacing: 0.16em !important;
    color: #7A8FAF !important;
    padding: 0.8rem 1.4rem !important;
    border-radius: 0 !important;
    border-bottom: 3px solid transparent !important;
    transition: all 0.2s !important;
}
div[data-testid="stTabs"] button:hover {
    color: #FFFFFF !important;
    background: rgba(233,69,96,0.08) !important;
}
div[data-testid="stTabs"] button[aria-selected="true"] {
    color: #F5A623 !important;
    border-bottom: 3px solid #E94560 !important;
    background: rgba(233,69,96,0.1) !important;
}
div[data-testid="stTabsContent"] {
    border: none !important;
    padding-top: 1.5rem !important;
}

/* ── FILE CONTENT VIEWER ── */
.file-viewer {
    background: #0D1B2A;
    border: 1px solid rgba(245,166,35,0.3);
    border-left: 4px solid #F5A623;
    border-radius: 6px;
    padding: 1.2rem 1.4rem;
    margin-top: 0.8rem;
    font-family: 'Courier New', monospace;
    font-size: 0.9rem;
    color: #E8F4F8 !important;
    white-space: pre-wrap;
    word-break: break-word;
    line-height: 1.8;
    max-height: 300px;
    overflow-y: auto;
}
.viewer-label {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.25em;
    color: #F5A623 !important;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}

/* ── SUCCESS / ERROR / WARNING ── */
div[data-testid="stAlert"] {
    border-radius: 8px !important;
}
div[data-testid="stAlert"][data-baseweb="notification"] {
    background-color: rgba(22,33,62,0.9) !important;
}

/* ── FOOTER ── */
.mafia-footer {
    text-align: center;
    padding: 2.5rem 0 1.5rem;
}
.mafia-footer p {
    color: #4A5568 !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.2em !important;
    text-transform: uppercase !important;
}
.mafia-footer span {
    color: #E94560 !important;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #1A1A2E; }
::-webkit-scrollbar-thumb { background: #E94560; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #FF6B8A; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  CRUD FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def create_file_op(name: str, data: str):
    path = Path(name)
    if path.exists():
        return False, f"A file named **{name}** already exists."
    with open(path, "w") as f:
        f.write(data)
    return True, f"File **{name}** created successfully."

def read_file_op(name: str):
    path = Path(name)
    if not path.exists():
        return False, None, f"No file named **{name}** found."
    with open(path, "r") as f:
        content = f.read()
    if not content.strip():
        return True, "(File is empty)", None
    return True, content, None

def rename_file_op(name: str, new_name: str):
    path = Path(name)
    new_path = Path(new_name)
    if not path.exists():
        return False, f"File **{name}** does not exist."
    if new_path.exists():
        return False, f"**{new_name}** already exists. Choose a different name."
    path.rename(new_path)
    return True, f"File renamed to **{new_name}** successfully."

def append_file_op(name: str, data: str):
    path = Path(name)
    if not path.exists():
        return False, f"File **{name}** does not exist."
    with open(path, "a") as f:
        f.write("\n" + data)
    return True, f"Content appended to **{name}** successfully."

def overwrite_file_op(name: str, data: str):
    path = Path(name)
    if not path.exists():
        return False, f"File **{name}** does not exist."
    with open(path, "w") as f:
        f.write(data)
    return True, f"**{name}** has been overwritten successfully."

def delete_file_op(name: str):
    path = Path(name)
    if not path.exists():
        return False, f"No file named **{name}** found."
    path.unlink()
    return True, f"**{name}** has been permanently deleted."

# ─────────────────────────────────────────────────────────────────────────────
#  HERO
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
    <p class="hero-title">FILE MAFIA</p>
    <p class="hero-sub">🔫 &nbsp; Every File Has a Price &nbsp; 🔫</p>
    <div class="hero-line"></div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  TABS
# ─────────────────────────────────────────────────────────────────────────────
tabs = st.tabs(["🗡  CREATE", "📖  READ", "✏️  UPDATE", "💀  DELETE"])

# ══════════════════════════════════════════════
#  TAB 1 — CREATE
# ══════════════════════════════════════════════
with tabs[0]:
    st.markdown("""
    <div class="op-card">
        <div class="card-tag">Operation · Genesis</div>
        <div class="card-heading">🗡 Create a <span>New File</span></div>
    </div>
    """, unsafe_allow_html=True)

    c_name = st.text_input("File Name", placeholder="example.txt", key="c_name")
    c_data = st.text_area("File Content", placeholder="Type what you want to write into the file...", height=150, key="c_data")

    if st.button("⚡  CREATE FILE", key="btn_create"):
        if not c_name.strip():
            st.error("❌  Please enter a file name.")
        else:
            ok, msg = create_file_op(c_name.strip(), c_data)
            if ok:
                st.success(f"✅  {msg}")
                st.balloons()
            else:
                st.error(f"❌  {msg}")

# ══════════════════════════════════════════════
#  TAB 2 — READ
# ══════════════════════════════════════════════
with tabs[1]:
    st.markdown("""
    <div class="op-card">
        <div class="card-tag">Operation · Dossier</div>
        <div class="card-heading">📖 Read a <span>File</span></div>
    </div>
    """, unsafe_allow_html=True)

    r_name = st.text_input("File Name", placeholder="example.txt", key="r_name")

    if st.button("🔍  READ FILE", key="btn_read"):
        if not r_name.strip():
            st.error("❌  Please enter a file name.")
        else:
            ok, content, err = read_file_op(r_name.strip())
            if ok:
                st.success(f"✅  File found — displaying contents below:")
                st.markdown(f'<p class="viewer-label">📄 {r_name.strip()}</p><div class="file-viewer">{content}</div>', unsafe_allow_html=True)
            else:
                st.error(f"❌  {err}")

# ══════════════════════════════════════════════
#  TAB 3 — UPDATE
# ══════════════════════════════════════════════
with tabs[2]:
    st.markdown("""
    <div class="op-card">
        <div class="card-tag">Operation · Reshape</div>
        <div class="card-heading">✏️ Update a <span>File</span></div>
    </div>
    """, unsafe_allow_html=True)

    u_name = st.text_input("Target File Name", placeholder="example.txt", key="u_name")

    operation = st.radio(
        "Select Operation",
        ["🏷️  Rename File", "➕  Append Content", "🔄  Overwrite File"],
        key="u_op"
    )

    if operation == "🏷️  Rename File":
        u_new = st.text_input("New File Name", placeholder="new_name.txt", key="u_newname")
        if st.button("✏️  RENAME FILE", key="btn_rename"):
            if not u_name.strip() or not u_new.strip():
                st.error("❌  Both old and new names are required.")
            else:
                ok, msg = rename_file_op(u_name.strip(), u_new.strip())
                st.success(f"✅  {msg}") if ok else st.error(f"❌  {msg}")

    elif operation == "➕  Append Content":
        u_append = st.text_area("Content to Append", placeholder="This will be added at the end of the file...", height=130, key="u_append")
        if st.button("➕  APPEND CONTENT", key="btn_append"):
            if not u_name.strip():
                st.error("❌  Please enter a file name.")
            elif not u_append.strip():
                st.warning("⚠️  Nothing to append.")
            else:
                ok, msg = append_file_op(u_name.strip(), u_append)
                st.success(f"✅  {msg}") if ok else st.error(f"❌  {msg}")

    elif operation == "🔄  Overwrite File":
        u_over = st.text_area("New Content (replaces everything)", placeholder="Old content will be erased. Type new content here...", height=130, key="u_over")
        if st.button("🔄  OVERWRITE FILE", key="btn_over"):
            if not u_name.strip():
                st.error("❌  Please enter a file name.")
            else:
                ok, msg = overwrite_file_op(u_name.strip(), u_over)
                st.success(f"✅  {msg}") if ok else st.error(f"❌  {msg}")

# ══════════════════════════════════════════════
#  TAB 4 — DELETE
# ══════════════════════════════════════════════
with tabs[3]:
    st.markdown("""
    <div class="op-card">
        <div class="card-tag">Operation · Cleanup</div>
        <div class="card-heading">💀 Delete a <span>File</span></div>
    </div>
    """, unsafe_allow_html=True)

    d_name = st.text_input("File Name", placeholder="example.txt", key="d_name")
    confirm = st.checkbox("⚠️  I confirm this action is irreversible", key="d_confirm")

    if st.button("🗑️  DELETE FILE", key="btn_delete"):
        if not d_name.strip():
            st.error("❌  Please enter a file name.")
        elif not confirm:
            st.warning("⚠️  Tick the confirmation checkbox first.")
        else:
            ok, msg = delete_file_op(d_name.strip())
            st.success(f"🩸  {msg}") if ok else st.error(f"❌  {msg}")

# ─────────────────────────────────────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="mafia-footer">
    <p>✦ &nbsp; FILE MAFIA &nbsp; <span>·</span> &nbsp; CRUD File Operations &nbsp; <span>·</span> &nbsp; Built with Python &nbsp; ✦</p>
    <p style="margin-top:0.3rem; font-size:0.7rem !important;">Made by ANKIT SRIVASTVA</p>
</div>
""", unsafe_allow_html=True)