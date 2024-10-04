import streamlit as st 
from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd
import numpy as np
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
df = pd.read_csv('course_data.csv',index_col=0)
courses = df.to_dict('records')
descriptions = [course['Content'] for course in courses]
embeddings = model.encode(descriptions)
index = faiss.IndexFlatL2(embeddings.shape[1])  # L2 distance index
index.add(np.array(embeddings))


def generate_response(query,k=5):
    # print(query)
    query_embedding = model.encode([query[-1]])  
    D, I = index.search(np.array(query_embedding), k=k)  # k is the number of top results
    # Retrieve course titles based on the search results
    results = []
    desc = []
    for idx in I[0]:
        course_title = courses[idx]['Course_Name']  # Get the course title
        desc.append(courses[idx]['Content'])
        results.append(course_title)
    # output=''
    # for i,j in enumerate(list(set(results))):
    #     output+=str(i+1)+j+'\n'
    return list(set(results))


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
