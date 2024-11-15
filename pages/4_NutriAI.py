import requests
import streamlit as st
import google.generativeai as genai

# Set your Gemini API Key here
api_key = "AIzaSyAn0sfx2Btwhycp2r3SubCs-3dmMv_xRik"  # Replace with your actual Gemini API key
genai.configure(api_key=api_key)

def get_nutrition_advice(query):
    try:
        # Initialize the model (using 'gemini-1.5-flash' model)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Generate content based on user query
        response = model.generate_content(query)
        
        # Return the generated content (the response text)
        return response.text
    
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit interface
st.title("NutriAI: Your AI Nutritionist")

query = st.text_area("Ask about Nutrition:", "What are the benefits of eating kale?")

if st.button("Get Advice"):
    if query:
        advice = get_nutrition_advice(query)
        st.write(advice)
    else:
        st.write("Please enter a query to get advice.")
