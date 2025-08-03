
# 🤖 Market Insight AI Agent

**Market Insight AI Agent** is an interactive AI-powered business assistant that uses **Google Gemini AI** to analyze structured and unstructured data, helping businesses make better decisions by understanding product trends, regional revenue, and board-level insights.

---

##  Features

-  Reads and processes:
  - Structured data (CSV - customer orders)
  - Unstructured data (TXT, PDF - market trends, board meeting notes)
-  Business analytics:
  - Revenue by product category
  - Units sold by region and time
  - Monthly and quarterly trends
-  Interactive Q&A:
  - Ask questions about sales performance, trends, top products, and more
  - Powered by **Gemini 2.5 Flash** for fast and accurate insights
-  Simple web UI built with **Streamlit**

---

##  Technologies Used

- Python
- Google Gemini AI (via `google.generativeai`)
- Pandas, NumPy
- Matplotlib, Seaborn
- PyPDF2
- Streamlit

---

##  How to Run

1. Install dependencies:
```bash
pip install pandas numpy matplotlib seaborn PyPDF2 streamlit google-generativeai
```

2. Add your Gemini API key in `app.py`:
```python
my_key = "YOUR_GEMINI_API_KEY"
```

3. Launch the Streamlit app:
```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
📦 Market-Insight-AI-Agent
 ┣ 📄 app.py
 ┣ 📄 marketDataAnalysis.ipynb
 ┣ 📄 customer_orders_cleaned.csv
 ┣ 📄 Market.txt
 ┣ 📄 board_meeting_2024_summary.pdf
 ┗ 📄 README.md
```

---

##  Example Queries

- "What is the top product category in 2023?"
- "Summarize the board meeting for 2024"
- "How is revenue distributed across regions?"
- "What are the trends in Q2?"

---

##  Author

**[Pratik_Bhuwad]**  
📧 [pratikbhuwad192k4@gmail.com]  
🔗 [www.linkedin.com/in/pratik-bhuwad-a62576293]  

---

##  Tags

`#AI #Gemini #GoogleAI #Streamlit #DataAnalytics #BusinessIntelligence #Python #NLP #GenerativeAI`
