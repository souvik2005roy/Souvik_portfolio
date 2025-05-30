import streamlit as st
from PIL import Image
import json
from streamlit_lottie import st_lottie

# Load local image and animation
img = Image.open('./Resume Photo.jpg')

def load_lottie_local(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

lottie_coding = load_lottie_local("lottiefile.json")

# Custom CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Poppins', sans-serif;
            background-color: #1e1e2f;
            color: white;
        }

        /* MAIN CONTENT SIZING */
        h1 { font-size: 3rem !important; }
        h2 { font-size: 2.2rem !important; }
        h3 { font-size: 1.8rem !important; }
        h4 { font-size: 1.5rem !important; }
        p, li, a { font-size: 1.25rem !important; }
        .stTabs [role="tab"] {
            font-size: 1.4rem !important;
            padding: 0.8rem 1.6rem;
        }

        .project-box {
            background-color: #f8f8f8;
            color: black;
            border-radius: 12px;
            padding: 26px;
            margin-bottom: 20px;
            font-size: 1.25rem;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        }

        .project-box h4 {
            font-size: 1.8rem;
            margin-bottom: 0.5rem;
        }

        .skills-bar-container {
            background-color: #444;
            border-radius: 12px;
            overflow: hidden;
            margin-bottom: 16px;
            height: 26px;
        }

        .skills-bar {
            height: 100%;
            background-color: #1e90ff;
        }

        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 14px;
            margin-top: 8px;
            margin-bottom: 16px;
            font-size: 1.2rem;
            border: none;
            border-radius: 8px;
        }

        .contact-form button {
            background-color: #4CAF50;
            color: white;
            font-size: 1.2rem;
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }

        /* SIDEBAR FONT CONTROL */
        section[data-testid="stSidebar"] {
            font-size: 1.05rem;
        }

        section[data-testid="stSidebar"] h1, 
        section[data-testid="stSidebar"] h2, 
        section[data-testid="stSidebar"] h3 {
            font-size: 1.4rem !important;
        }

        section[data-testid="stSidebar"] a {
            font-size: 1.05rem !important;
            word-break: break-word;
        }
    </style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    st.image(img, width=200)
    st.title("Souvik Kumar Roy")
    st.markdown("📧 **Email:** [souvik.roy0946@gmail.com](mailto:souvik.roy0946@gmail.com)")
    st.markdown("💼 **LinkedIn:** [souvik-roy](https://www.linkedin.com/in/souvik-roy)")
    st.markdown("🐙 **GitHub:** [souvik2005roy](https://github.com/souvik2005roy)")
    st.divider()
    st_lottie(lottie_coding, height=220, key="sidebar_lottie")


# --- TABS Layout ---
tabs = st.tabs(["🚀 Projects", "🧠 Skills", "💬 Testimonials", "📬 Contact Me"])

# Projects Tab
with tabs[0]:
    project_data = [
        {"title": "OCR Text Extraction", "desc": "Extract text from images or PDFs using OCR.", "url": "https://github.com/souvik2005roy/ocr-project"},
        {"title": "Data Visualizer App", "desc": "Interactive data visualization using Streamlit.", "url": "https://github.com/souvik2005roy/dataviz-app"},
        {"title": "Hospital DBMS", "desc": "DBMS with Python and MySQL for hospital systems.", "url": "https://github.com/souvik2005roy/hospital-dbms"}
    ]
    cols = st.columns(2)
    for idx, project in enumerate(project_data):
        with cols[idx % 2]:
            st.markdown(f"""
                <div class='project-box'>
                    <h4>📁 {project['title']}</h4>
                    <p>{project['desc']}</p>
                    <a href="{project['url']}" target="_blank">🔗 View on GitHub</a>
                </div>
            """, unsafe_allow_html=True)

# Skills Tab
with tabs[1]:
    skills = {
        "Python": 90,
        "Machine Learning": 55,
        "Data Visualization": 60,
        "MySQL": 80
    }
    for skill, value in skills.items():
        st.write(f"**{skill}**")
        st.markdown(f"""
            <div class='skills-bar-container'>
                <div class='skills-bar' style='width: {value}%;'></div>
            </div>
        """, unsafe_allow_html=True)

# Testimonials Tab
with tabs[2]:
    st.markdown("""
    > "Souvik is a dedicated developer with a great attitude toward learning."  
    > — Peer Review

    > "Excellent team player and communicator."  
    > — Project Mentor
    """)

# Contact Tab
with tabs[3]:
    st.markdown("""
<form class="contact-form" action="https://formsubmit.co/souvik.roy0946@gmail.com" method="POST">
    <div style="display: flex; flex-direction: column; gap: 12px;">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" rows="6" placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
    </div>
    <input type="hidden" name="_captcha" value="false">
</form>
""", unsafe_allow_html=True)




