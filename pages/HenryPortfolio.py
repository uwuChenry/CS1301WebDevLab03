import streamlit as st
import info
import pandas as pd


def about_me_section():
    st.header("About Me")
    st.image(info.profile_picture, width=200)
    st.write(info.about_me)
    st.write('---')
about_me_section()


def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on Linkedin")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src = "{info.linkedin_image_url}" alt = "linkedin" width = "75" height= "75"</a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Check out my work")
    linkedin_link = f'<a href="{info.}"><img src = "{info.linkedin_image_url}" alt = "linkedin" width = "75" height= "75"</a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)


    