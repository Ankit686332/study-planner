import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. Setup & Branding Configuration
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Page Config
st.set_page_config(
    page_title="Study Architect | Ankit Mohanty",
    page_icon="🧠",
    layout="centered"
)

# --- CUSTOM CSS FOR BRANDING ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #1E88E5;
        color: white;
        font-weight: bold;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: #555;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        border-top: 1px solid #ddd;
    }
    .title-text {
        color: #0D47A1;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Logic Function
def get_ai_response(topic, hours, level):
    if not api_key:
        return "Please configure your API Key."
    
    genai.configure(api_key=api_key)
    # Using the latest 2026 stable model
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    
    prompt = f"""
    You are a professional academic advisor. Create a comprehensive 
    study roadmap for {topic}. 
    Details: Student is at {level} level and has {hours} hours/week.
    Include: Specific modules, practice projects, and assessment milestones.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# --- APP UI ---
st.markdown("<h1 class='title-text'>🧠 Study Architect AI</h1>", unsafe_allow_html=True)
st.write("---")
st.write("Welcome! This intelligent planning tool was designed to help you master any subject efficiently.")

# Personal Intro
st.info(f"Developed by **Ankit Mohanty** | Powered by Advanced Generative AI")

# Input Section
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        topic = st.text_input("What do you want to learn?", placeholder="e.g. Quantum Computing")
        level = st.select_slider("Current Expertise", options=["Beginner", "Intermediate", "Advanced"])
    
    with col2:
        hours = st.number_input("Hours available per week", min_value=1, max_value=100, value=10)
        submit = st.button("Build My Custom Roadmap")

# Execution & Output
if submit:
    if topic:
        with st.spinner("Ankit's AI is analyzing your curriculum..."):
            plan = get_ai_response(topic, hours, level)
            st.success("✅ Roadmap Generated Successfully!")
            st.markdown("### 📋 Your Personalized Plan")
            st.markdown(plan)
            
            # Download feature
            st.download_button("Download Plan as Text", plan, file_name="study_plan.txt")
    else:
        st.warning("Please enter a topic to begin.")

# --- FOOTER ---
st.markdown(f"""
    <div class="footer">
        Created with ❤️ by <b>Ankit Mohanty</b> | 2026 AI Innovation Project
    </div>
    """, unsafe_allow_html=True)