import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="Web Development Lab 03 - Home", layout="wide")

# Function to load the video and return as base64
@st.cache_resource
def load_video():
    with open("vid/bgvid.mp4", "rb") as video_file:
        video_bytes = video_file.read()
    return base64.b64encode(video_bytes).decode()

# Load resources
video_str = load_video()

# Custom CSS for the video container and overlay text
st.markdown("""
    <style>
    body {
        background-color: black;
        color: #9ca3af;
    }
    .title {
        color: #9ca3af;
        font-size: 2.5em;
        text-shadow: 1px 1px 4px #0f766e;
    }
    .video-container {
        position: relative;
        width: 100%;
        height: 70vh;
        overflow: hidden;
    }
    .video-wrapper {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        opacity: 0.2;
    }
    .video-wrapper video {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .overlay-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-size: 3vw;
        font-weight: bold;
        text-align: center;
        width: 100%;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        z-index: 1;
    }
    .grey-box {
        background-color: #333333;
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
        box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.5);
    }
    .cryptic {
        font-size: 1.25em;
        letter-spacing: 0.1em;
    }
    </style>
""", unsafe_allow_html=True)

# Display the page content

st.title("Web Development Lab 03")
st.header("CS 1301")
st.subheader("Team 29, Web Development - Section A")
st.subheader("Rayeed Zaman, Po Cheng Chen")

# Display video with overlay text
st.markdown(f"""
    <div class="video-container">
        <div class="video-wrapper">
            <video autoplay loop muted playsinline>
                <source src="data:video/mp4;base64,{video_str}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
        <div class="overlay-text">
            Welcome to our Lab 3 Project<br>
            <span style="font-size: 35px;">Web Development Lab 03</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Page descriptions with grey contrast boxes
st.header("Pages")
st.markdown("""
<div class="grey-box cryptic">1. Henry's Portfolio: Explore projects, skills, and achievements by Henry.</div>
<div class="grey-box cryptic">2. Rayeed's Portfolio: Discover Rayeed's journey, projects, and expertise in tech.</div>
<div class="grey-box cryptic">3. Recipe Finder: Find delicious recipes tailored to your tastes and preferences.</div>
<div class="grey-box cryptic">4. NutriAI: Get personalized nutritional insights and suggestions with AI.</div>
""", unsafe_allow_html=True)
