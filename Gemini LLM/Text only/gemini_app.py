import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
import numpy as np
genai.configure(api_key=os.getenv('GEMINI'))
database_str=''
with open('database.txt', 'r',encoding='utf-8') as f:
    database_str = f.read()


def generate_response(query):
    prompt = f'''
    You are a Course suggestor based on the user requirement and the from the given database which consist of 
    the course name and description of the course.

    You're tasked to use the description of each course and compare it with the user input and output which course's
    description matches the user requirement.
    Output the course name alone which matches the user requirement.
    you may output a max of 3 courses if you find that are good matches. name of the course should be exactly same as the database provided to you.
    # Database
    {database_str}

    # User Input
    {query[-1]}

    # Output : (Course Name with | as splitter)
    '''
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text.split("|")


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
            for i in message['content']:
                st.write('* '+i)
