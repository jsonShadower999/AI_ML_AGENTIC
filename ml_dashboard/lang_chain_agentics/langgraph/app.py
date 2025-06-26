import streamlit as st
import google.generativeai as genai
import os
from constants import API_KEY, MODEL_NAME

# Configure API key
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel(MODEL_NAME)

def get_gemini_response(ques):
    if ques:
        response = model.generate_content(ques)
        return response.text
    else:
        return "Please ask a question!"

# Streamlit UI
st.set_page_config(page_title="Ques-Answer quiz")
st.header("genai appllm")

input_question = st.text_input("Enter your question", key="input")
submit_button = st.button("Ask your query")

if submit_button:
    output = get_gemini_response(input_question)
    st.write(output)
