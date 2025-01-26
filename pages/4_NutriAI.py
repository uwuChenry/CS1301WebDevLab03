import requests
import streamlit as st
import google.generativeai as genai

API_URL = "https://www.themealdb.com/api/json/v1/1/"

api_key = "AIzaSyAn0sfx2Btwhycp2r3SubCs-3dmMv_xRik"  
genai.configure(api_key=api_key)

if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'current_recipe' not in st.session_state:
    st.session_state.current_recipe = None
if 'current_ingredients' not in st.session_state:
    st.session_state.current_ingredients = ""
if 'initial_advice_given' not in st.session_state:
    st.session_state.initial_advice_given = False

def search_recipe_by_name(meal_name):
    response = requests.get(f"{API_URL}search.php?s={meal_name}")
    return response.json()

def get_random_recipe():
    response = requests.get(f"{API_URL}random.php")
    return response.json()

def filter_by_category(category):
    response = requests.get(f"{API_URL}filter.php?c={category}")
    return response.json()

def filter_by_ingredient(ingredient):
    response = requests.get(f"{API_URL}filter.php?i={ingredient}")
    return response.json()

def get_nutrition_advice(query):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def chat_with_ai(user_input, context=""):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        full_prompt = f"Context about the recipe:\n{context}\n\nUser question: {user_input}\n\nPlease provide a helpful response about the recipe and nutrition."
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

st.title("NutriAI: Your AI Nutritionist")
search_type = st.selectbox("Search By", ["Meal Name", "Main Ingredient"]) #NEW
info = ""
ing = ""
mname = ""
recipe_overview = None
nutrition_query = None

if search_type == "Meal Name":
    meal_name = st.text_input("Enter Meal Name") #NEW
    if meal_name:
        result = search_recipe_by_name(meal_name)
        if result["meals"]:
            meal = result["meals"][0]
            mname = meal["strMeal"]
            ins = meal['strInstructions']
            st.session_state.current_recipe = meal
            
            for i in range(1, 21):
                ingredient = meal.get(f"strIngredient{i}")
                measure = meal.get(f"strMeasure{i}")
                if ingredient:
                    ing += (f"{ingredient} - {measure} ")
            st.session_state.current_ingredients = ing
            
            recipe_overview = f"{info}\n{ing}\ngive me a very very general overview of the instructions and ingredients"
            nutrition_query = f"{info}\n{ing}\nGive me a general nutrition analysis of this recipe. We don't need to be too specific, just a general overview is fine."
        else:
            st.write("No recipes found. Please try another name.")

elif search_type == "Main Ingredient":
    ingredient = st.text_input("Enter Main Ingredient")
    if ingredient:
        nutrition_query = f"Give me general nutrition advice on {ingredient} as a main ingredient"
        st.session_state.current_ingredients = f"Main ingredient: {ingredient}"
    elif ingredient == "":
        st.write("Enter a valid ingredient")
    else:
        st.write(f"No meals found with {ingredient}.")

query = st.text_area("Ask about Nutrition:", "Give me a general nutrition analysis of the above")

if st.button("Get Advice"): #NEW
    if query:
        with st.spinner("Analyzing nutritional information..."): #NEW
            if recipe_overview:
                summary = get_nutrition_advice(recipe_overview)
                st.subheader(f"Overview for {mname}")
                st.write(summary)
                st.subheader(f"NutriAI Advice for {mname}")
            
            if nutrition_query:
                advice = get_nutrition_advice(nutrition_query)
                st.success("Analysis complete!")
                st.write(advice)
                
                st.session_state.messages = []
                st.session_state.messages.append({"role": "assistant", "content": advice})
                st.session_state.initial_advice_given = True
            

            if search_type == "Meal Name" and 'result' in locals() and len(result["meals"]) > 1:
                st.subheader(f"Other similar recipes for \"{meal_name}\"")
                for things in result["meals"][1:]:
                    st.write(things["strMeal"])
    else:
        st.warning("Please enter a query to get advice.") #NEW

if st.session_state.current_ingredients and st.session_state.initial_advice_given:
    st.subheader("Chat with NutriAI")
    
    if len(st.session_state.messages) == 1:
        with st.chat_message("assistant"): #NEW
            st.write("Let me know if you have any further questions!")
    
    if prompt := st.chat_input("Ask a follow-up question about the recipe or nutrition"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        context = f"Recipe: {mname if mname else 'N/A'}\nIngredients: {st.session_state.current_ingredients}"
        if st.session_state.current_recipe:
            context += f"\nInstructions: {st.session_state.current_recipe['strInstructions']}"
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chat_with_ai(prompt, context)
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})