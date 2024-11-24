import requests
import streamlit as st
import google.generativeai as genai

# Base URL for the MealDB API
API_URL = "https://www.themealdb.com/api/json/v1/1/"

api_key = "AIzaSyAn0sfx2Btwhycp2r3SubCs-3dmMv_xRik"  
genai.configure(api_key=api_key)

def search_recipe_by_name(meal_name):
    response = requests.get(f"{API_URL}search.php?s={meal_name}")
    return response.json()

# Function to get a random recipe
def get_random_recipe():
    response = requests.get(f"{API_URL}random.php")
    return response.json()

# Function to filter meals by category
def filter_by_category(category):
    response = requests.get(f"{API_URL}filter.php?c={category}")
    return response.json()

# Function to filter meals by main ingredient
def filter_by_ingredient(ingredient):
    response = requests.get(f"{API_URL}filter.php?i={ingredient}")
    return response.json()
    # Search by meal name


def get_nutrition_advice(query):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(query)
        return response.text
    
    except Exception as e:
        return f"Error: {str(e)}"

st.title("NutriAI: Your AI Nutritionist")



search_type = st.selectbox("Search By", ["Meal Name", "Main Ingredient"])
info = ""
ing = ""

if search_type == "Meal Name":
    meal_name = st.text_input("Enter Meal Name")
    if meal_name:
        result = search_recipe_by_name(meal_name)
        if result["meals"]:
            meal = result["meals"][0]
            ins = meal['strInstructions']
            for i in range(1, 21):
                ingredient = meal.get(f"strIngredient{i}")
                measure = meal.get(f"strMeasure{i}")
                if ingredient:
                    ing += (f"{ingredient} - {measure}")
            # print(ing)
        else:
            st.write("No recipes found. Please try another name.")
            query = ""
    query = st.text_area("Ask about Nutrition:", "Give me general nutrition analysis of the above recipe")
    fq = info + "\n" + ing + "\n" + query + "we don't need to be too specific, just general overview is fine. "
    print(ing)
    print(info)
    print(query)
    # Display a random recipe

elif search_type == "Main Ingredient":
    ingredient = st.text_input("Enter Main Ingredient")
    query = st.text_area("Ask about Nutrition:", "Give me general nutrition advice on the main ingredient")

    if ingredient:
        fq = query + f"with the main ingredient being {ingredient}"
    elif ingredient == "":
        st.write("Enter a valid ingredient")
    else:
        st.write(f"No meals found with {ingredient}.")


if st.button("Get Advice"):
    if query and fq:
        advice = get_nutrition_advice(fq)
        st.write(advice)
    else:
        st.write("Please enter a query to get advice.")
