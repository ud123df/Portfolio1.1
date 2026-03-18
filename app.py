import streamlit as st

st.set_page_config(layout="wide")

# 🔥 CSS
st.markdown("""
<style>

/* 🌌 Background */
.stApp {
    background: radial-gradient(circle at top, #1a1a1a, #050505);
    color: white;
    font-family: 'Poppins', sans-serif;
}

/* 🔥 Fade-in animation */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(40px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* 🔥 Glow animation */
@keyframes glow {
    0% { box-shadow: 0 0 5px #00bfff; }
    50% { box-shadow: 0 0 25px #00bfff; }
    100% { box-shadow: 0 0 5px #00bfff; }
}

/* 🔥 HERO */
.hero {
    text-align: center;
    padding: 80px 0;
    animation: fadeIn 1.2s ease-in-out;
}

.hero h1 {
    font-size: 80px;
    letter-spacing: 6px;
    font-weight: 800;
    animation: fadeIn 1.5s ease-in-out;
}

/* 🔥 CARD */
.card {
    background: #0a0a0a;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0px 20px 50px rgba(0,0,0,0.8);
    margin: 40px auto;
    max-width: 1100px;
    animation: fadeIn 1.2s ease-in-out;
}

/* 🔥 PROJECT BLOCK */
.project {
    background: #111;
    padding: 25px;
    border-radius: 12px;
    border: 1px solid #222;
    transition: all 0.4s ease;
    animation: fadeIn 1.5s ease-in-out;
}

/* Hover animation */
.project:hover {
    transform: translateY(-12px) scale(1.02);
    border: 1px solid #00bfff;
    box-shadow: 0px 0px 25px rgba(0,191,255,0.4);
}

/* Title glow */
.project h3 {
    color: #00bfff;
    transition: 0.3s;
}

.project:hover h3 {
    text-shadow: 0px 0px 15px #00bfff;
}

/* 🔥 Buttons */
.stButton>button {
    background: linear-gradient(90deg, #00bfff, #0077ff);
    color: white;
    border-radius: 6px;
    padding: 10px 20px;
    border: none;
    transition: 0.3s;
}

/* Button hover */
.stButton>button:hover {
    transform: scale(1.08);
    box-shadow: 0px 0px 20px #00bfff;
}

/* 🔥 Contact box */
.contact-box {
    background: #111;
    padding: 30px;
    border-radius: 10px;
    animation: fadeIn 2s ease-in-out;
}

/* Inputs */
input, textarea {
    background: transparent !important;
    color: white !important;
    border-bottom: 1px solid #555 !important;
    transition: 0.3s;
}

/* Input focus glow */
input:focus, textarea:focus {
    border-bottom: 1px solid #00bfff !important;
    box-shadow: 0px 2px 10px rgba(0,191,255,0.3);
}

/* 🔥 Footer */
.footer {
    text-align: center;
    color: #888;
    padding: 50px;
    animation: fadeIn 2.5s ease-in-out;
}

</style>
""", unsafe_allow_html=True)

# 🔥 HERO
st.markdown("""
<div class="hero">
    <p>I AM</p>
    <h1>UDIT SHARMA</h1>
    <p>AI / ML ENGINEER</p>
</div>
""", unsafe_allow_html=True)

# 🔥 PROJECT SECTION
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("MY PROJECTS")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="project">
        <h3>DOC RAG System</h3>
        <p>Document Question Answering system using RAG architecture.</p>
        <p><b>Tech:</b> LLM, Embeddings, AWS</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("View Project", key="rag")

with col2:
    st.markdown("""
    <div class="project">
        <h3>Object Detection System</h3>
        <p>Real-time object detection using YOLO with high accuracy.</p>
        <p><b>Tech:</b> YOLOv8, OpenCV, PyTorch</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("View Project", key="object")

# 👉 Second row
col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="project">
        <h3>AI Analyst</h3>
        <p>Automated data analysis tool with intelligent insights.</p>
        <p><b>Tech:</b> Python, Pandas, LLM</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("View Project", key="ai")

with col4:
    st.markdown("""
    <div class="project">
        <h3>YouTube RAG System</h3>
        <p>Ask questions from YouTube videos using transcript-based RAG.</p>
        <p><b>Tech:</b> LLM, LangChain, Vector DB</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("View Project", key="yt")

st.markdown('</div>', unsafe_allow_html=True)

# 🔥 CONTACT
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### CONTACT
    
    📍 Himachal Pradesh, India  
    📧 udit.sharma2312@gmail.com  
    💻 github.com/ud123df
    """)

with col2:
    st.markdown('<div class="contact-box">', unsafe_allow_html=True)

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    msg = st.text_area("Message")

    if st.button("SEND MESSAGE"):
        st.success("Message sent!")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 🔥 FOOTER
st.markdown("""
<div class="footer">
    Thanks for watching
</div>
""", unsafe_allow_html=True)