import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
import numpy as np
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv('GEMINI'))
database_str=''
with open('data_base.txt', 'r',encoding='utf-8') as f:
    database_str = f.read()


def generate_response(query):
    prompt = f'''
    You are a Course suggestor based on the user requirement and the given database, which consists of 
    the course name, description, and link to each course.

    You're tasked to use the description of each course and compare it with the user input, then output the courses
    whose description matches the user requirement.
    
    Strictly output the course name and its corresponding link, following the exact format below:
    - Output a maximum of 3 courses if they match well.
    - The format should be exactly: Course Name || Course Link
    - Each course should be on a new line.
    - No extra text or commentary, only the exact output format specified.
    - Example Output : Creating Problem-Solving Agents using GenAI for Action Composition || https://courses.analyticsvidhya.com/courses/Creating%20Problem-Solving%20Agents%20using%20GenAI%20for%20Action%20Composition

    # Database
    {database_str}

    # User Input
    {query[-1]}

    # Output (maximum of 3 courses):
    '''
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip().split("\n")



# Define session state variables
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'mess' not in st.session_state:
    st.session_state.mess=[]


if st.sidebar.button("RESET"):
    st.session_state.messages=[]
    st.session_state.mess=[]
    
# User input
st.title('Analytics Vidhya Course Finder')
user_input = st.chat_input('Write your message here...')

if user_input:
    # Append user input to messages
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.mess+=[user_input]
    # Generate chatbot response
    bot_response = generate_response(st.session_state.mess)
    st.session_state.messages.append({"role": "bot", "content": bot_response})

# Display chat messages in correct order
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("human"):
            st.write(message['content'])
    else:
        with st.chat_message("ai"):
            for item in message['content']:
                # Skip if the item is empty
                if not item.strip():
                    continue

                try:
                    name, link = item.split('||')
                    # Strip any extra whitespace
                    name = name.strip()
                    link = link.strip()
                    st.markdown(f"[{name}]({link})", unsafe_allow_html=True)
                except ValueError:
                    print("Warning: Unable to parse the course recommendation properly.")
                            
