import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import re
import json

# Load environment variables
load_dotenv()

# Configure Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to clean text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Function to extract text from PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Function to get response from Gemini API
def get_gemini_response(input_text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_text)
    return response.text

# Input Prompt Template
input_prompt_template = """
Hey, act like a highly skilled ATS (Application Tracking System) with expertise in software engineering, 
data science, data analysis, and big data engineering. Your task is to evaluate the resume provided 
against the job description given below.

Please assign a percentage match between the job description and resume, and identify any missing key skills or keywords. 
Also, provide a brief profile summary of the resume.

Format your response as follows: 
{{"JD Match":"<percentage>%","MissingKeywords":["list of keywords"],"Profile Summary":"<brief summary>"}}

Resume: {resume_text}

Job Description: {jd_clean}
"""

# Streamlit app
st.title("Track Your Resume ATS Score")
st.text("Improve Your Resume for ATS Systems")

jd = st.text_area("Paste the Job Description", help="Enter the job description you want to match.")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload your resume in PDF format.")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)
        resume_text_clean = clean_text(resume_text)

        jd_clean = clean_text(jd)
        
        if jd_clean:
            input_prompt = input_prompt_template.format(resume_text=resume_text_clean, jd_clean=jd_clean)

            response = get_gemini_response(input_prompt)
            
            try:
                response_json = json.loads(response)
                
                jd_match = response_json.get("JD Match", "N/A")
                missing_keywords = response_json.get("MissingKeywords", [])
                profile_summary = response_json.get("Profile Summary", "")

                st.subheader("ATS Score Report")
                st.write(f"**Job Description Match:** {jd_match}")
                st.write("**Missing Keywords:**")
                for keyword in missing_keywords:
                    st.write(f"- {keyword}")
                st.write("**Profile Summary:**")
                st.write(profile_summary)
                
            except json.JSONDecodeError:
                st.error("Failed to parse the response. Please check the API output.")
        else:
            st.error("Please provide a valid job description.")
    else:
        st.error("Please upload a valid resume in PDF format.")
