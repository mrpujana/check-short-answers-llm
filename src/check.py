import streamlit as st
import google.generativeai as genai

# st.write("# Marker")


class AnswerChecker:
    def __init__(self, api_key):
        self.api_key = api_key
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")

    def generate_feedback(self, question, answer, full_marks=10):
        try:
            response = self.model.generate_content(
                f"the question is {question} and the answer to this question as responded by student is {answer}. Now evaluate this answer based on the question, grade it out of {full_marks} and provide feedback. provide grade in `marks` field and feedback in `feedback` field.",
                # stream=True,
            )
            return response.text
        except Exception as e:
            st.error(f"Failed to generate summary: {str(e)}")
            return None
