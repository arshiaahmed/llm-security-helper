import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI


# Load API key from .env


load_dotenv()
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),  # use your Gemini key here
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
                                                               )

st.title("🔐 LLM Security Helper")

# Choose analysis mode
mode = st.radio(
    "Choose analysis type:",
    ["Code Security Check", "GenAI Spec Risk Check"]
)

# User input
user_input = st.text_area("Paste your input here:")

# Analyze function using Gemini
def analyze(prompt):
    response = client.chat.completions.create(
        model="gemini-2.5-flash",  # simple, human-readable model
        messages=[{"role": "user", "content": prompt}]
    )
    # Gemini API returns same structure as OpenAI
    return response.choices[0].message.content

# Button click
if st.button("Analyze") and user_input:

    if mode == "Code Security Check":
        prompt = f"""
Analyze the following code ONLY for security vulnerabilities.
For each issue provide:
- Vulnerability name
- Why it is dangerous
- Clear recommended fix

Code:
{user_input}
"""
    else:
        prompt = f"""
Analyze the following GenAI/Agentic app specification.

Identify security risks mapped to:
- OWASP Top 10 for LLM Applications
- ATLAS threat categories

Provide clear, actionable mitigations.

Specification:
{user_input}
"""

    # Get result and show
    result = analyze(prompt)
    st.subheader("Result")
    st.write(result)


# I want to build a GenAI-powered travel assistant that:
# - Recommends flights, hotels, and tours
# - Stores user preferences and credit card info
# - Can call other APIs to book tickets automatically


# I want to build a GenAI-powered coding assistant that:
# - Generates code snippets in multiple programming languages
# - Can access GitHub repositories and push changes
# - Reads and writes project configuration files
# - Provides debugging suggestions and automated code fixes
# - Allows multiple users to collaborate in real time


# # Vulnerable login code
# username = input("Enter username: ")
# password = input("Enter password: ")

# query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
# cursor.execute(query)


# # Vulnerable API usage
# api_key = "12345SECRET67890"
# response = requests.get(f"https://example.com/data?api_key={api_key}")

