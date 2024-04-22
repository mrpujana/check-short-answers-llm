import streamlit as st
import google.generativeai as genai
from dotenv import dotenv_values
from check import AnswerChecker
import json

config = dotenv_values(".env")
GOOGLE_API_KEY = config["GOOGLE_API_KEY"]
st.write("# Checker")

checker = AnswerChecker(GOOGLE_API_KEY)

question = "Define polymorphism in OOP."

full_marks = st.selectbox("Marks: ", range(1, 11))

answer = st.text_input(question, placeholder="Type your answer here")


feedback = checker.generate_feedback(question, answer, full_marks)
feedback_cleaning = feedback.strip('```json').strip('```')
feedback=json.loads(feedback_cleaning)
st.write(feedback['marks'])
st.write(feedback['feedback'])