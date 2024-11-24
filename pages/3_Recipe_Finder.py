import streamlit as st
import requests
import random
import folium
from streamlit_folium import st_folium

API_URL = "https://www.themealdb.com/api/json/v1/1/"

AREA_COORDINATES = {
    "Canadian": (56.1304, -106.3468),
    "American": (37.0902, -95.7129),
    "British": (55.3781, -3.4360),
    "Chinese": (35.8617, 104.1954),
    "Italian": (41.8719, 12.5674),
    "Indian": (20.5937, 78.9629),
    "Mexican": (23.6345, -102.5528),
    "Japanese": (36.2048, 138.2529),
    "French": (46.6034, 1.8883),
    "Thai": (15.8700, 100.9925),
    "Malaysian": (4.2105, 101.9758),
    "Tunisian": (33.8869, 9.5375),
    "Greek": (39.0742, 21.8243),
    "Spanish": (40.4637, -3.7492),
    "Vietnamese": (14.0583, 108.2772),
    "Turkish": (38.9637, 35.2433),
    "Korean": (35.9078, 127.7669),
    "Moroccan": (31.7917, -7.0926),
    "Brazilian": (-14.2350, -51.9253),
    "Egyptian": (26.8206, 30.8025),
    "German": (51.1657, 10.4515),
    "Portuguese": (39.3999, -8.2245),
    "Indonesian": (-0.7893, 113.9213),
    "Lebanese": (33.8547, 35.8623),
    "Russian": (61.5240, 105.3188),
    "Ethiopian": (9.1450, 40.4897),
    "Argentinian": (-38.4161, -63.6167),
    "Australian": (-25.2744, 133.7751),
    "South African": (-30.5595, 22.9375),
    "Jamaican": (18.1096, -77.2975),
    "Cuban": (21.5218, -77.7812),
    "Peruvian": (-9.189967, -75.015152),
    "Chilean": (-35.6751, -71.5430),
    "Saudi Arabian": (23.8859, 45.0792),
    "Iranian": (32.4279, 53.6880),
    "Pakistani": (30.3753, 69.3451),
    "Bangladeshi": (23.6850, 90.3563),
    "Nepalese": (28.3949, 84.1240),
    "Sri Lankan": (7.8731, 80.7718),
    "Caribbean": (15.3269, -61.7712),  
    "Polish": (51.9194, 19.1451),
    "Hungarian": (47.1625, 19.5033),
    "Swedish": (60.1282, 18.6435),
    "Norwegian": (60.4720, 8.4689),
    "Finnish": (61.9241, 25.7482),
    "Danish": (56.2639, 9.5018),
    "Croatian": (45.1000, 15.2000),
    "Filipino": (12.8797, 121.7740),  
    "Singaporean": (1.3521, 103.8198),
    "Dutch": (52.1326, 5.2913),
    "Swiss": (46.8182, 8.2275),  
    "Belgian": (50.5039, 4.4699),  
    "Austrian": (47.5162, 14.5501),  
    "Ukrainian": (48.3794, 31.1656),  
    "Czech": (49.8175, 15.4730), 
    "Thai": (15.8700, 100.9925),
    "Malay": (4.2105, 101.9758),
    "New Zealander": (-40.9006, 174.8860),
    "Colombian": (4.5709, -74.2973),
    "Venezuelan": (6.4238, -66.5897),
    "Afghan": (33.9391, 67.7100),
    "Kazakh": (48.0196, 66.9237),
    "Uzbek": (41.3775, 64.5853),
    "Georgian": (42.3154, 43.3569),
    "Armenian": (40.0691, 45.0382),
    "Mongolian": (46.8625, 103.8467),
    "Iraqi": (33.2232, 43.6793),
    "Syrian": (34.8021, 38.9968),
    "Jordanian": (30.5852, 36.2384),
    "Palestinian": (31.9522, 35.2332),
    "Yemeni": (15.5527, 48.5164),
    "Omani": (21.4735, 55.9754),
    "Qatari": (25.2760, 51.2330),
    "Bahraini": (26.0667, 50.5577),
    "Kuwaiti": (29.3759, 47.9774),
    "Emirati": (23.4241, 53.8478),
    "Algerian": (28.0339, 1.6596),
    "Tanzanian": (-6.3690, 34.8888),
    "Kenyan": (-1.286389, 36.817223),
    "Ugandan": (1.3733, 32.2903)
}
def search_recipe_by_name(meal_name):
    response = requests.get(f"{API_URL}search.php?s={meal_name}")
    return response.json()

def get_random_recipe():
    response = requests.get(f"{API_URL}random.php")
    return response.json()

def get_coordinates(area):
    return AREA_COORDINATES.get(area, (None, None))

def filter_by_category(category):
    response = requests.get(f"{API_URL}filter.php?c={category}")
    return response.json()

def filter_by_ingredient(ingredient):
    response = requests.get(f"{API_URL}filter.php?i={ingredient}")
    return response.json()

def display_recipe(meal):
    st.subheader(meal["strMeal"])
    st.image(meal["strMealThumb"])
    st.write(f"**Category**: {meal['strCategory']}")
    st.write(f"**Area**: {meal['strArea']}")
    
    with st.expander("Instructions", expanded=True):
        st.write(meal['strInstructions'])
    
    with st.expander("Ingredients", expanded=True):
        for i in range(1, 21):
            ingredient = meal.get(f"strIngredient{i}")
            measure = meal.get(f"strMeasure{i}")
            if ingredient and ingredient.strip():
                st.write(f"{ingredient} - {measure}")
    
    area = meal["strArea"]
    lat, lon = get_coordinates(area)
    if lat is not None and lon is not None:
        st.write(f"**Location of the {area} cuisine origin:** {lat}, {lon}")
        map_ = folium.Map(location=[lat, lon], zoom_start=5)
        folium.Marker([lat, lon], popup=f"{area}").add_to(map_)
        st_folium(map_, width=700, height=500, key=f"map_{meal['idMeal']}") #NEW (st_folium)
    else:
        st.write(f"Coordinates for the {area} cuisine are not available.")

def display_remaining_recipes(meals, current_meal_id):
    remaining_meals = [meal for meal in meals if meal['idMeal'] != current_meal_id]
    if remaining_meals:
        st.markdown("---")
        st.subheader("Other Matching Recipes")
        cols = st.columns(3)
        for idx, meal in enumerate(remaining_meals):
            with cols[idx % 3]:
                st.image(meal['strMealThumb'], width=200)
                st.write(f"**{meal['strMeal']}**")
                if st.button("View Recipe", key=f"btn_{meal['idMeal']}"):
                    st.session_state.current_meal = meal
                    st.rerun()

def main():
    st.title("Recipe Finder")
    
    # Initialize session state
    if 'current_meal' not in st.session_state:
        st.session_state.current_meal = None
    if 'search_performed' not in st.session_state:
        st.session_state.search_performed = False
    if 'last_search' not in st.session_state:
        st.session_state.last_search = None
    if 'all_meals' not in st.session_state:
        st.session_state.all_meals = None

    search_type = st.selectbox("Search By", 
                             ["Meal Name", "Random", "Category", "Main Ingredient"],
                             key="search_type") #NEW (selectbox)

    if search_type == "Meal Name":
        meal_name = st.text_input("Enter Meal Name", key="meal_name") #NEW (text_input)
        
        # Only perform search if meal name changed or no search performed yet
        if meal_name and (not st.session_state.search_performed or meal_name != st.session_state.last_search):
            result = search_recipe_by_name(meal_name)
            if result["meals"]:
                st.session_state.all_meals = result["meals"]
                st.session_state.current_meal = result["meals"][0]
                st.session_state.search_performed = True
                st.session_state.last_search = meal_name
            else:
                st.write("No recipes found. Please try another name.")
                st.session_state.current_meal = None
                st.session_state.all_meals = None
        
        if st.session_state.current_meal:
            display_recipe(st.session_state.current_meal)
            if st.session_state.all_meals:
                display_remaining_recipes(st.session_state.all_meals, st.session_state.current_meal['idMeal'])

    elif search_type == "Random":
        if st.button("Get New Random Recipe") or (not st.session_state.current_meal): #NEW (button)
            result = get_random_recipe()
            st.session_state.current_meal = result["meals"][0]
            st.session_state.all_meals = result["meals"]
        
        if st.session_state.current_meal:
            display_recipe(st.session_state.current_meal)

    elif search_type == "Category":
        category = st.selectbox("Select Category", 
                              ["Seafood", "Dessert", "Chicken", "Beef", "Vegetarian"],
                              key="category")
        if category:
            result = filter_by_category(category)
            if result["meals"]:
                st.write(f"**Meals in the {category} Category:**")
                cols = st.columns(3)
                for idx, meal in enumerate(result["meals"]):
                    with cols[idx % 3]:
                        st.write(f"- {meal['strMeal']}")
            else:
                st.write(f"No meals found in the {category} category.")

    elif search_type == "Main Ingredient":
        ingredient = st.text_input("Enter Main Ingredient", key="ingredient")
        if ingredient:
            result = filter_by_ingredient(ingredient)
            if result["meals"]:
                st.write(f"**Meals with {ingredient}:**")
                cols = st.columns(3)
                for idx, meal in enumerate(result["meals"]):
                    with cols[idx % 3]:
                        st.write(f"- {meal['strMeal']}")
            else:
                st.write(f"No meals found with {ingredient}.")

if __name__ == "__main__":
    main()
