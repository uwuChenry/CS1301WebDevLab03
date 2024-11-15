import streamlit as st
import requests

# Base URL for the MealDB API
API_URL = "https://www.themealdb.com/api/json/v1/1/"

# Function to search for recipes by meal name
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

# Display the main page
def main():
    st.title("Recipe Finder")
    
    # Options to search for recipes
    search_type = st.selectbox("Search By", ["Meal Name", "Random", "Category", "Main Ingredient"])
    
    # Search by meal name
    if search_type == "Meal Name":
        meal_name = st.text_input("Enter Meal Name")
        if meal_name:
            result = search_recipe_by_name(meal_name)
            if result["meals"]:
                for meal in result["meals"]:
                    st.subheader(meal["strMeal"])
                    st.image(meal["strMealThumb"])
                    st.write(f"**Category**: {meal['strCategory']}")
                    st.write(f"**Area**: {meal['strArea']}")
                    st.write(f"**Instructions**: {meal['strInstructions']}")
                    st.write("**Ingredients**:")
                    for i in range(1, 21):
                        ingredient = meal.get(f"strIngredient{i}")
                        measure = meal.get(f"strMeasure{i}")
                        if ingredient:
                            st.write(f"{ingredient} - {measure}")
            else:
                st.write("No recipes found. Please try another name.")
    
    # Display a random recipe
    elif search_type == "Random":
        result = get_random_recipe()
        meal = result["meals"][0]
        st.subheader(meal["strMeal"])
        st.image(meal["strMealThumb"])
        st.write(f"**Category**: {meal['strCategory']}")
        st.write(f"**Area**: {meal['strArea']}")
        st.write(f"**Instructions**: {meal['strInstructions']}")
        st.write("**Ingredients**:")
        for i in range(1, 21):
            ingredient = meal.get(f"strIngredient{i}")
            measure = meal.get(f"strMeasure{i}")
            if ingredient:
                st.write(f"{ingredient} - {measure}")
    
    # Filter by category
    elif search_type == "Category":
        category = st.selectbox("Select Category", ["Seafood", "Dessert", "Chicken", "Beef", "Vegetarian"])
        if category:
            result = filter_by_category(category)
            if result["meals"]:
                st.write(f"**Meals in the {category} Category:**")
                for meal in result["meals"]:
                    st.write(f"- {meal['strMeal']}")
            else:
                st.write(f"No meals found in the {category} category.")
    
    # Filter by main ingredient
    elif search_type == "Main Ingredient":
        ingredient = st.text_input("Enter Main Ingredient")
        if ingredient:
            result = filter_by_ingredient(ingredient)
            if result["meals"]:
                st.write(f"**Meals with {ingredient}:**")
                for meal in result["meals"]:
                    st.write(f"- {meal['strMeal']}")
            else:
                st.write(f"No meals found with {ingredient}.")

if __name__ == "__main__":
    main()
