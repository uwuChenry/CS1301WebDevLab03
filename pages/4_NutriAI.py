import requests
import streamlit as st
import google.generativeai as genai

api_key = "AIzaSyAn0sfx2Btwhycp2r3SubCs-3dmMv_xRik"  
genai.configure(api_key=api_key)

def get_nutrition_advice(query):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(query)
        return response.text
    
    except Exception as e:
        return f"Error: {str(e)}"

st.title("NutriAI: Your AI Nutritionist")

query = st.text_area("Ask about Nutrition:", "What are the benefits of eating kale?")

if st.button("Get Advice"):
    if query:
        advice = get_nutrition_advice(query)
        st.write(advice)
    else:
        st.write("Please enter a query to get advice.")
