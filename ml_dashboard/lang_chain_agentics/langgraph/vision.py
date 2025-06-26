import streamlit as st
import google.generativeai as genai
import os
from constants import API_KEY, MODEL_NAME
from PIL import Image
import base64
from io import BytesIO

# Configure API key
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel(MODEL_NAME)

def image_to_base64(image):
    """Converts an image to a base64-encoded string."""
    buffered = BytesIO()
    image.save(buffered, format="PNG")  # You can change "PNG" to "JPEG" if required.
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

def get_gemini_response(input_text, image):
    if input_text and image:
        # Convert the image to base64 format
        image_base64 = image_to_base64(image)

        # Now pass both text and the base64-encoded image as inputs (check model docs for exact format)
        combined_input = f"Question: {input_text}\nImage: {image_base64}"
        response = model.generate_content(combined_input)  # Assuming the model handles both text and image in a single input
    elif input_text:
        # If only text is provided
        response = model.generate_content(input_text)
    else:
        return "Please provide a question or upload an image."

    return response.text  # Return the response

# Streamlit UI
st.set_page_config(page_title="Image-Ques-Answer quiz")
st.header("genai appllm")

# Input for the text question
input_question = st.text_input("Enter your question", key="input")

# Image upload for the image input (supporting jpg, jpeg, png)
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Initialize image variable
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)  # Open image file

    # Convert to RGB to ensure uniform format (important for different image types like PNG, JPG, etc.)
    image = image.convert("RGB")
    
    st.image(image, caption="Uploaded Image", use_column_width=True)  # Display the image

# Button to submit query
submit_button = st.button("Ask your query")

if submit_button:
    if input_question or image:  # Check if either input is provided
        output = get_gemini_response(input_question, image)  # Call function with both question and image
        st.write(output)  # Display the response
    else:
        st.write("Please enter a question or upload an image for further description.")
