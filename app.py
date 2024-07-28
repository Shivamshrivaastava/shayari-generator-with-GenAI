import streamlit as st
import google.generativeai as genai
import os

# Configure API key for google.generativeai
API_KEY = 'AIzaSyBGW3XJYQWzRfrSs7wtFzkS80sIEl7-j1k'
genai.configure(api_key=API_KEY)

# Initialize the GenerativeModel
model = genai.GenerativeModel('gemini-1.5-flash')

# Streamlit app title
st.title("Custom Shayari Generator")

# Input field for the user to enter the theme/topic
theme = st.text_input("Enter the theme or topic for the Shayari:")

if theme:
    # Generate content based on the user input
    prompt = f'create a shayari on {theme} in English and Hindi'
    response = model.generate_content(prompt)

    # Display the response text in Streamlit app
    st.subheader("Generated Shayari")
    st.write(response.text)
else:
    st.write("Please enter a theme or topic to generate a Shayari.")


