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
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt = "linkedin" width = "75" height= "75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Check out my work")
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt = "github" width = "75" height= "75"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Email Me!")
    email_link = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt = "email" width = "75" height= "75"></a>'
    st.sidebar.markdown(email_link, unsafe_allow_html=True)
links_section()

def education_section(education_data, course_data):
    st.header("Education")
    st.subheader(f"**{education_data["Institution"]}**")
    st.write(f"**Degree:** {education_data["Degree"]}")
    st.write(f"**Graduation Date:** {education_data["Graduation Date"]}")
    st.write(f"**GPA:** {education_data["GPA"]}")
    st.write("Relevant Coursework:")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I Learned"},
        hide_index=True,
        )
    st.write("---")
education_section(info.education_data, info.course_data)

def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title, (job_desc, img) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(img, width=250)
        for bullet in job_desc:
            expander.write(bullet)
    st.write("---")
experience_section(info.experience_data)


def project_section(projects_data):
    st.header("Projects")
    for name, desc in projects_data.items():
        expander = st.expander(f"{name}")
        expander.write(desc)
    st.write("---")

project_section(info.projects_data)


def skills_section(prog, spoken):
    st.header("Skills")
    st.subheader("Programming Languages:")
    for lang, percentage in prog.items():
        st.write(f"{lang}{info.programming_icons.get(lang, "")}")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken.items():
        st.write(f"{spoken}{info.spoken_icons.get(spoken, "")}: {proficiency}")
skills_section(info.programming_data, info.spoken_data)


def activities_section(leadership, activity):
    st.header("Activities")
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])
    with tab1:
        st.subheader("Leadership")
        for title, (details, img) in leadership.items():
            expander = st.expander(f"{title}")
            expander.image(img, width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title, details in activity.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
    st.write("---")
activities_section(info.leadership_data, info.activity_data)