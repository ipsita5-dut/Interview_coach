import os
import streamlit as st
import google.generativeai as genai

# 🔹 Configure Gemini API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAoaF0hEQejJfy6bcd8_bbYKO88uU3wz_w"  # Replace with your actual API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 🔹 Load Gemini model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# 🔹 Function to generate interview questions
def generate_questions(job_description, num_questions=5):
    prompt = f"Generate {num_questions} interview questions for the following job description:\n\n{job_description}"
    response = model.generate_content(prompt)
    return response.text

# 🔹 Function to evaluate candidate response
def evaluate_response(candidate_response, job_description):
    prompt = f"""Evaluate this interview response:\n\n'{candidate_response}'\n\n
    Consider the job description:\n\n'{job_description}'\n
    Provide feedback on clarity, technical depth, and communication."""
    
    response = model.generate_content(prompt)
    return response.text

# 🔹 Function to generate follow-up questions
def follow_up_question(candidate_response, job_description):
    prompt = f"Based on the candidate's answer:\n\n'{candidate_response}',\n\nGenerate a follow-up interview question for the job:\n\n'{job_description}'."
    
    response = model.generate_content(prompt)
    return response.text

# 🚀 **Streamlit UI**
st.set_page_config(page_title="AI Interview Coach", layout="centered")
st.title("🧑‍💼 AI Interview Coach 🤖")
st.markdown("Generate interview questions, evaluate responses, and get follow-up questions using Gemini AI!")

# 📌 **Section 1: Generate Interview Questions**
st.subheader("📝 Generate Interview Questions")
job_desc = st.text_area("Enter Job Description:", height=100)
num_questions = st.number_input("Number of Questions:", min_value=1, max_value=10, value=5)

if st.button("Generate Questions"):
    if job_desc.strip():
        with st.spinner("Generating questions..."):
            questions = generate_questions(job_desc, num_questions)
        st.subheader("📌 Interview Questions:")
        st.write(questions)
    else:
        st.warning("Please enter a job description.")

# 📌 **Section 2: Evaluate Candidate Response**
st.subheader("💡 Evaluate Candidate Response")
candidate_response = st.text_area("Enter Candidate's Answer:", height=150)

if st.button("Evaluate Response"):
    if candidate_response.strip() and job_desc.strip():
        with st.spinner("Evaluating response..."):
            feedback = evaluate_response(candidate_response, job_desc)
        st.subheader("📌 Feedback:")
        st.write(feedback)
    else:
        st.warning("Please enter both a job description and a candidate response.")

# 📌 **Section 3: Generate Follow-Up Question**
st.subheader("🔄 Follow-Up Question Generator")

if st.button("Generate Follow-Up Question"):
    if candidate_response.strip() and job_desc.strip():
        with st.spinner("Generating follow-up question..."):
            follow_up = follow_up_question(candidate_response, job_desc)
        st.subheader("📌 Follow-Up Question:")
        st.write(follow_up)
    else:
        st.warning("Please enter both a job description and a candidate response.")

