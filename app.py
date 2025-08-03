#--------------------------- Building Bot using Gemini api --------------------------

# -------------------------- importing necessary libraries -----------------------
import pandas as pd
import numpy as np
from datetime import datetime
import PyPDF2
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from pathlib import Path

# -------------------------- Setting up the GeminiAI client --------------------------

import google.generativeai as genai

my_key="Your_Gemini_API_Key_Here"  # Replace with your actual Gemini API key
genai.configure(api_key=my_key)
model = genai.GenerativeModel('models/gemini-2.5-flash')

# print('Available Gemini models and supported methods:')
# for m in genai.list_models():
#     print(m.name, m.supported_generation_methods)


# -------------------------- Loading data --------------------------
def load_data():
    df= pd.read_csv('customer_orders_cleaned.csv')

    with open('Market.txt', 'r') as f:
        market=f.read()

    reader = PyPDF2.PdfReader('board_meeting_2024_summary.pdf')
    pdf= ""
    for page in reader.pages:
        pdf += page.extract_text()

    return df, market, pdf

#storing the data in variables
df, market_text, pdf_text = load_data()

#Processing of data
df['Order Date']=pd.to_datetime(df['Order Date'])
df['Month']=df['Order Date'].dt.to_period('M')
df['Quarter']=df['Order Date'].dt.to_period('Q')
df['Year']=df['Order Date'].dt.year
top_product=df.groupby('Product Category')['Revenue'].sum().sort_values(ascending=False).head(5)
region_pref=df.groupby('Region')['Revenue'].sum()
product_units=df.groupby('Product Category')['Units Sold'].sum().sort_values(ascending=False)

#Streamlit UI setup
import streamlit as st
st.set_page_config(page_title="Sales AI Agent", layout="wide")
st.title('Sales Business AI Agent')
st.markdown('Ask anything about the company performance, product sales, customer feedback, and market trends.')

query = st.text_input("Enter your query here:")

if st.button('Get Insights from AI Agent'):
    prompt = f"""
            You are a highly skilled business analyst AI Assistant
            Here is the business context to use in your answer.

            Top Product Category by Revenue:
            {top_product.to_string()}

            Product Category Units Sold Per Product Category:
            {product_units.to_string()}

            Revenue By Region:
            {region_pref.to_string()}

            Market Trend Highlights:
            {market_text[:100]}

            Board Meeting Summary:
            {pdf_text[:100]}

            Now analyze and answer the query:{query}
"""

    with st.spinner('Analyzing...'):
        try:
            response = model.generate_content(prompt)
            st.success('Analysis complete!')
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")