# app.py

import streamlit as st

# Set the title of the app with a colorful background
st.markdown(
    """
    <style>
    .title {
        font-size: 30px;
        font-weight: bold;
        color: white;
        background-color: #FF5733;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    <div class="title">🌈 Welcome to the Colorful Streamlit App! 🌈</div>
    """,
    unsafe_allow_html=True
)

# Add a colorful header
st.markdown(
    """
    <style>
    .header {
        font-size: 30px;
        font-weight: bold;
        color: #33FF57;
        text-align: center;
    }
    </style>
    <div class="header">✨ Let's Get Started! ✨</div>
    """,
    unsafe_allow_html=True
)

# Ask for the user's name
name = st.text_input("👋 What's your name?", "Type your name here...")

# Ask for the user's favorite color
color = st.selectbox(
    "🎨 What's your favorite color?",
    ("Red", "Blue", "Green", "Yellow", "Purple", "Orange")
)

# Map colors to their respective hex codes
color_map = {
    "Red": "#FF0000",
    "Blue": "#0000FF",
    "Green": "#00FF00",
    "Yellow": "#FFFF00",
    "Purple": "#800080",
    "Orange": "#FFA500"
}

# Display a personalized message in the selected color
if name and color:
    st.markdown(
        f"""
        <style>
        .message {{
            font-size: 25px;
            font-weight: bold;
            color: {color_map[color]};
            text-align: center;
        }}
        </style>
        <div class="message">🎉 Hello, {name}! Your favorite color is {color}. 🎉</div>
        """,
        unsafe_allow_html=True
    )

# Add a colorful footer
st.markdown(
    """
    <style>
    .footer {
        font-size: 20px;
        color: #33C1FF;
        text-align: center;
        margin-top: 50px;
    }
    </style>
    <div class="footer">🚀 Thanks for using the Colorful Streamlit App! 🚀</div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .explanation {
        font-size: 25px;
        font-weight: bold;
        color: #FF33A8;
        text-align: center;
        margin-top: 50px;
    }
    .subheader {
        font-size: 22px;
        font-weight: bold;
        color: #33A8FF;
        margin-top: 20px;
    }
    .text {
        font-size: 18px;
        color: #333333;
        margin-top: 10px;
    }
    .highlight {
        font-size: 18px;
        color: #FF5733;
        font-weight: bold;
    }
    .explanation {
        font-size: 25px;
        font-weight: bold;
        color: #FF33A8;
        text-align: center;
        margin-top: 50px;
    }
    .text {
        font-size: 18px;
        color: #05aafc;
        margin-top: 10px;
    }
    .subheader {
        font-size: 22px;
        font-weight: bold;
        color: #c205fc;
        margin-top: 20px;
    }
    </style>
    <div class="explanation">📘 What is Streamlit?</div>
    <div class="text">Streamlit is a Python library that lets you build web apps for data visualization, machine learning models, and other data-driven applications quickly.</div>
    """,
    unsafe_allow_html=True
)

# Add project instructions
st.markdown(
    """
    <div class="subheader">📌 What You Need to Do in This Project</div>
    <div class="text">
        1. <span class="highlight">Set Up the Environment:</span> Install Streamlit and create a Python file.<br>
        2. <span class="highlight">Understand Streamlit Basics:</span> Learn to add interactive elements like text, buttons, and charts.<br>
        3. <span class="highlight">Build a Simple Web App:</span> Create a web app that displays data or performs calculations.<br>
        4. <span class="highlight">Run and Test the App:</span> Launch your Streamlit app locally.
    </div>
    """,
    unsafe_allow_html=True
)

# Add how to run the project
st.markdown(
    """
    <div class="subheader">📚 How to Run This Project</div>
    <div class="text">
        1. Ensure you have Python installed (version 3.8 or later).<br>
        2. <span class="highlight">Install Streamlit:</span> Run <code>pip install streamlit</code> in your terminal.<br>
        3. <span class="highlight">Save the Code:</span> Save the above code in a file named <code>app.py</code>.<br>
        4. <span class="highlight">Run the App:</span> Navigate to the directory where <code>app.py</code> is saved and run the following command:<br>
        <code>streamlit run app.py</code><br>
        5. Open the link (usually <code>http://localhost:8501</code>) in your browser.
    </div>
    """,
    unsafe_allow_html=True
)

# Add what the app does
st.markdown(
    """
    <div class="subheader">🎯 What the App Does</div>
    <div class="text">
        1. <span class="highlight">Title:</span> The app starts with a colorful title that welcomes the user.<br>
        2. <span class="highlight">Header:</span> A header encourages the user to get started.<br>
        3. <span class="highlight">Input:</span> The user is asked to input their name and select their favorite color from a dropdown menu.<br>
        4. <span class="highlight">Output:</span> The app displays a personalized message in the selected color.<br>
        5. <span class="highlight">Footer:</span> A colorful footer thanks the user for using the app.
    </div>
    """,
    unsafe_allow_html=True
)

# Final note
st.markdown(
    """
    <div class="text" style="text-align: center; margin-top: 30px;">
        🎨🚀 This project is simple, colorful,<br> and easy to understand,<br> making it perfect for beginners learning Streamlit! 🎨🚀
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="text" style="text-align: center; margin-top: 30px; color: red; font-weight:bold;">
        📓✒️  Author : Azmat Ali 📓✒️
    </div>
    """,
    unsafe_allow_html=True
)