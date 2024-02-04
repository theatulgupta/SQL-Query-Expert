import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
import sqlite3

# Load environment variables from .env file
load_dotenv()

# Configure genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get genai response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel(model_name="gemini-pro")
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the SQLite database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

# Custom Prompt
prompt = ["You are an expert in converting English questions to SQL queries! The SQL database named STUDENT has the following columns: NAME, CLASS, SECTION. For example, Example 1 - How many entries of records are present? The SQL command will be something like SELECT COUNT(*) FROM STUDENT; Example 2 - What is the average age of the students? The SQL command will be something like SELECT AVG(AGE) FROM STUDENT; Also, the SQL code should not have ``` at the beginning or end, and the word 'sql' should not be in the output."]

# Setup Streamlit app
st.set_page_config(
    page_title="SQL Query Expert", page_icon=":robot:")

st.header("SQL Query Expert")

question = st.text_input("Enter your query:", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question, prompt)
    data = read_sql_query(response, "student.db")
    st.subheader("Response:")
    for row in data:
        st.write(row)
