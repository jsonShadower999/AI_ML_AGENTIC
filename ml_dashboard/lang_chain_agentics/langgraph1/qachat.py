from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL_NAME = os.getenv("MODEL_NAME")  # Ensure this is in your .env file

# Initialize the model
model = genai.GenerativeModel(MODEL_NAME)
chat = model.start_chat(history=[])

def get_gemini_response(ques):
    # Sending the message to the chat model and returning the response
    response = chat.send_message(ques, stream=True)
    return response

# Streamlit UI setup
st.set_page_config(page_title="Q&A Demo Quizzer")
st.header("LLM Application :::")

# Initialize chat history if it doesn't exist in the session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input from the user
input = st.text_input("Enter query", key="input")
submit = st.button("Ask the query")

if submit and input:
    # Get response from the generative model
    response = get_gemini_response(input)
    
    # Add user query to session history
    st.session_state['chat_history'].append(("You", input))
    
    # Display the response
    st.subheader("Response is::::")
    
    # Display the chunks of the response
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display chat history
st.subheader("The chat history:")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
