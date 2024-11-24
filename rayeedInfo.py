#This File will contain the information to be displayed in your portfolio

#CHANGE BELOW
profile_picture = "Images/bobafett.png"
about_me = "I am Rayeed Zaman, an international student at Georgia Tech, majoring in Computer Science. With a strong background in Python, React, Node, Express, and Flask, I have developed a variety of full-stack applications, including my AI app called AquaRoute, aimed at optimizing ocean route planning to reduce plastic pollution, which won the best use of DataBricks at the AI ATL Hackathon. As the Head of IT at Asha Bangladesh, I have led teams of developers in leveraging GitHub for collaboration, while also contributing to the organization’s broader goals. I’m also passionate about outreach and currently serve as the Head of Outreach at Crisis Brigade. Outside of my professional responsibilities, I love to play the guitar and hang out with my friends. I make songs for fun sometimes and I also found myself making a recipe app for this project because I love food! "


#CHANGE BELOW (OPTIONAL)
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

#CHANGE BELOW
my_linkedin_url = "https://www.linkedin.com/in/rayeed"
my_github_url = "https://github.com/itsrayeedscodespace"
my_email_address = "rayeedzaman@gmail.com"


education_data ={
    'Degree': 'Bachelor of Science in Computer Science',
    'Institution': 'Georgia Institute of Technology',
    'Location': 'Atlanta, GA',
    'Graduation Date': '2028',
    'GPA': '4.0'
}
course_data = {
    "code":["CS 1301", "CS 2050", "ENGL 1101", "INTA 1200", "PSYC 1101"], 
    "names":["Intro to CS", "Discrete Math", "English Composition I", "American Government", "General Psychology"], 
    "semester_taken":["1st", "1st", "1st", "1st", "1st"],
    "skills":["Python is not a real programming language", "I've been lost since the first day of class", "Writing efficiently", "Bicameral Legislature", "The mind is what the brain does"],
    }
experience_data = {
    "Head of Web Development @ GTPL": (["- Led a team of 3 students in building the organization’s professional website from scratch using Tailwind CSS and JavaScript.",
                                                                          "- Increased the organization’s online reach by close collaboration with the marketing team, through strategic campaigns."],"Images/Web.png"),
    "IT Project Lead @ Bellissima Apparels Ltd.":(["- Worked in collaboration with a software engineer in building the company’s professional website from scratch using a CMS tool called Wordpress.",
                                                           "- Learnt about domain management, deployment, secure web hosting and maintenance."],"Images/IT.png"),

}

projects_data = {
    "AquaRoute | Streamlit, Databricks, Python, Plotly, Geopy, Numpy, Folium": ["- An AI-powered Streamlit app to optimize ocean routes based on plastic concentration data, using Folium for map visualization, KDTree for spatial queries and a modified A* using k-nearest neighbors to find the optimal route.", "- Won the Best Use of Databricks award at the AI ATL hackathon."],
    "MemoMe | MongoDB Compass, Flask, Python, React, HTML, CSS, Gradio": ["- Developed an AI web app to assist individuals with memory impairments by enabling users to interact with a speech-to-text chatbot which stores patient details using MongoDB Compass.", "- Implemented a user-friendly interface with React which enhances accessibility for patients, and also allows their caregivers to monitor their activity through the caregiver portal."]
}

programming_data = {
    "Python": 90,
    "Java": 50,
    "Dart": 80,
    "C": 60
}

#CHANGE BELOW (OPTIONAL)
programming_icons = {
    "Python": " 🐍",
    "Java": " ☕",
    "Dart": " 🔍",
    "C": " 🕹️"
}
spoken_icons = {"Bengali": " 🇧🇩",
    "English": " 🇬🇧",
    "Hindi":" 🇮🇳",
}

#CHANGE BELOW
spoken_data = {
    "Bengali": "Fluent",
    "English": "Fluent",
    "Hindi": "Fluent"
}
leadership_data = {
    "Head of Information Technology | Asha Bangladesh; Non-profit organization": (["- Independently developed the professional website for the non-profit, resulting in a 50% increase in site traffic within the first 3 months.", "- Contributed to social media campaigns that engaged over 1,000 supporters, leading to a 40% rise in fundraising contributions."],"Images/asha.png"),

}
activity_data={
    "Head of Marketing | Crisis Brigade; Non-profit organization": ["- Monitored customer feedback across 5 major social media platforms, leading to the identification of around 10 key areas for improvement, rised over $1000 in fundraisers.", 
            "- Collaborated with the graphics department on 10 posts a week, which led to a 20% increase in reach, as analysed by instagram’s business tools."]
}
