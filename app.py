from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import fitz 
from PIL import Image
import google.generativeai as genai
import io
import base64

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content,prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Read PDF file bytes
        pdf_bytes = uploaded_file.read()
        
        # Open PDF with PyMuPDF
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
        
        # Get first page
        first_page = pdf_document[0]
        
        # Convert page to image
        pix = first_page.get_pixmap()
        
        # Convert to PIL Image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Convert to bytes
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_document.close()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode(),
            }
        ]

        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

##  streamlit app 

st.set_page_config(page_title="Resume Classifier", page_icon=":robot_face:")
st.header("A ATS Resume Classifier")
input_text =st.text_area("Job Description: ",key="input")
uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

if uploaded_file is not None:
    st.write("Uploaded Resume Successfully!")

submit1 = st.button("Tell Me About this resume")

submit2 = st.button("How can i imporvise my skills")

submit3 = st.button("Percentage Match")

input_prompt1 = """
You are an expert HR with Tech Experience in the field of Data Science , Full Stack development, web development, big data engineering, DEVOPS, data analyist , your task is to analyze the provided resume against the  job description for these profiles. Please share your professional evaluation on whether the candidate's profile aligns with the role. Highlight the strengths and weaknesses of the candidate's profile in relation to the job description.
"""

input_prompt2 = """
You are an TEchnical Human Resource Manager with expertise in  the field of Data Science , Full Stack development, web development, big data engineering, DEVOPS, data analyist, your role is to scrutinize the provided resume against the job description for these profiles. Share your insights on the candiate's suitability for the role from an HR perspective. Additionally, provide constructive feedback on how the candidate can enhance their skills to better align with the job requirements.
"""

input_prompt3 = """
You are an Skilled ATS (Applicant Tracking System) with expertise in the field of Data Science , Full Stack development, web development, big data engineering, DEVOPS, data analyist. Your task is to evaluate the provided resume against the job description for these profiles. Calculate the percentage match between the candidate's profile and the job description, providing a clear and concise percentage score, and then the keywords that contributed to this score.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.header("Response is: ")
        st.write(response)
    else:
        st.error("Please upload a resume PDF file to get a response.")

if submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.header("Response is: ")
        st.write(response)
    else:
        st.error("Please upload a resume PDF file to get a response.")

if submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.header("Response is: ")
        st.write(response)
    else:
        st.error("Please upload a resume PDF file to get a response.")

