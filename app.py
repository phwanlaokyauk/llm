import streamlit as st
from openai import OpenAI
import os

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def create_study_plan(school, degree, year):
    response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": "# Identity\nYou are a senior academic coach for SIM undergraduates in Computer Science. Your goal is to convert the actual SIM/UoL CS curriculum into effective study techniques, time plans, resource stacks, and exam tactics that improve grades and mastery quickly.\n\n# Instruction\nRecommend effective study strategies for an undergraduate student pursuing a Computer Science degree at Singapore Institute of Management.\nPlan for each of the following:\n1.Effective study techniques\n2.Time management strategies\n3.Resource recommendations\n4.Tips for exam preparation\n\n# Context\nSIM delivers the UoL BSc (Hons) Computer Science in blended mode: Coursera/VLE + SIM teaching support, two semesters/year, up to 4 new modules/semester.\n2.Programme structure: 23 modules (8 L4 compulsory, 8 L5 compulsory, 6 L6 electives) + final project.\n"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": f"What are some effective study strategies for a {year} undergraduate {degree} student in {school} at Singapore Institute of Management?"
            }
        ]
        }
    ],
    response_format={
        "type": "text"
    },
    temperature=0,
    max_completion_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response

st.title("SIM STUDY PLANNING APP")

option_school = st.selectbox(
    "Your school",
    ("UOL", "UOW", "RMIT"),
    key="school"
)

option_degree = st.selectbox(
    "Your degree",
    ("Computer Science", "Business Management", "Data Science", "Finance"),
    key="degree"
)


option_year = st.selectbox(
    "Your year",
    ("Year 1", "Year 2", "Year 3", "Pre-U"),
    key="year"
)

if st.button("Generate Plan!"):
    res = create_study_plan(option_school, option_degree, option_year)
    st.markdown(res.choices[0].message.content)
    
