#This File will contain the information to be displayed in your portfolio

#CHANGE BELOW
profile_picture = "Images/yae miko square 512 512.png"
about_me = "Hi, I am Henry Chen, and I am an undergrad student at the Georgia Institute of Technology majoring in Computer Engineering. For eight years, I have participated in robotics competitions and gained extensive experience in designing robots and developing robotics algorithms for time-critical systems. In addition, I have honed my skills in leadership, teamwork, project management, event organization and mentoring. Providing educational opportunities for robotics in New Zealand has been a mission for me due to the lack of resources when I was starting out. I founded Skywalker Robotics in 2019 to create a place for passionate students that wanted to improve their skills in robotics through a variety of different robotic competitions such as FLL, VRC and Vex IQ. Outside of Skywalker Robotics. Throughout the years, I've found my passion for robotics and I hope to continue pursuing my passion for my career in fields such as planning, controls, computer vision as well as low level programming and embedded systems. Feel free to contact me at pchen432@gatech.edu. I look forward to meeting passionate like-minded peers and professionals."


#CHANGE BELOW (OPTIONAL)
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

#CHANGE BELOW
my_linkedin_url = "https://www.linkedin.com/in/henry-chen-980s"
my_github_url = "https://github.com/uwuChenry"
my_email_address = "pochengchen@gatech.edu"


education_data ={
    'Degree': 'Bachelor of Science in Computer Engineering',
    'Institution': 'Georgia Institute of Technology',
    'Location': 'Atlanta, GA',
    'Graduation Date': 'Never',
    'GPA': '4.0'
}
course_data = {
    "code":["CS 1301", "MATH 1552", "MATH 1554", "ENG 1102", "INTA 1200"], 
    "names":["Intro to CS", "Calculus II", "Linear Algebra", "English Composition II", "American Government"], 
    "semester_taken":["1st", "1st", "1st", "1st", "1st"],
    "skills":["Python is not my favorite snake anymore", "Integration and Series", "Basically row reduction", "I write English", "I hate politics"],
    }
experience_data = {
    "Skywalker Robotics Club | Founder": (["- Established a community-based club for motivated teenagers without access to robotics in school in New Zealand.",
                            "- Hosted 7 outreach workshops with 1000+ attendees to promote STEM Education in New Zealand.", 
                            "- Taught 650+ hrs of CAD & programming, provided troubleshooting consultation and competition tips to teams in New Zealand, Taiwan, Australia and United States both in person and online.",
                            "- Mentored 10+ teams, leading to a score increase of 150% and qualifying to the Vex World Championship 6 times"],"Images/SR.png"),
}

projects_data = {
    "Drone Assisted Water Sampling": ["- Developed and 3D-printed a custom quadcopter equipped with a retractable water collection payload, designed to sample water at targeted depths and specified GPS locations.","- Achieved up to 50% reduction in water sampling time compared to conventional methods such as boats and kayaks.","- Awarded Honorable mention at the Taiwan Macronix Science Fair."],
    "VEX Robotics Team 980s": ["- Integrated motion profile with feedforward velocity control, achieving 99.5% increase in movement accuracy and 80% in reliability, resulting in a 60% enhancement in smoothness and accuracy over traditional PID control.",
"- Developed and implemented 6+ autonomous robot control algorithms library including odometry and path tracking from research papers using embedded C++ and OOP, reducing robot programming time by 60%.",
"- Utilized concurrent control of robot subsystems through RTOS based multi-threading, finite state machines, and mutexes, eliminating race conditions and enhancing overall performance and reliability.",
"- Awarded at 2022 VEX Worlds Championship: Overall High School quarterfinalist, 8th Overall Worlds Skills Ranking, 1st seed Divisional Tournament Champion, Divisional Amaze Award (Most reliable performance)."]
}

programming_data = {
    "Python": 90,
    "Java": 70,
    "C/C++": 90,
}

#CHANGE BELOW (OPTIONAL)
programming_icons = {
    "Python": "🐍",
    "Java": "☕",
    "C": "🔍",
}
spoken_icons = {
    "French": "🇫🇷",
    "English": "🇬🇧",
    "Spanish":"🇪🇸",
    "Taiwanese": "🇹🇼",
    "Chinese": "㊗️"
}

#CHANGE BELOW
spoken_data = {
    "English": "Native",
    "Chinese": "Native",
    "Taiwanese": "Fluent",
}
leadership_data = {
    "Technical Captain, Programming Leader for FRC Team 7130": (["- Led a 15-member software team, mentoring new members in embedded control programming principles.",
"- Played a key role in the design process to ensure subsystem integration from a control and programming perspective, contributed to CAD and design of the drivetrain and intake.",
"- Implemented various control algorithms for subsystem control, used April tags (limelight & photonvision) for computer vision localization.",
"- Facilitated strategic project planning, culminating in the design, build, and testing of a 120-pound competition robot within a six-week timeframe.",
"- Collaborated with school administrators to organize seasonal activities, host STEM fairs for 7,000+ students, and lead participation in regional scrimmages."],"Images/prog.png"),

}
activity_data={
    "Georgia Tech Medical Robotics": ["- Making prosthetic arm with sensory feedback for optimal sensory restoration for arm amputees.",
"- Using Mediapipe to recognize continuous hand gestures to map it to EMG data using deep learning.",
"- Processing EMG data using python (NumPy, Pandas) with fast Fourier transform, low pass filter and RMS filter."]
}
