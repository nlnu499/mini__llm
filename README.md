Next Word Prediction System
Overview

This project is a simple Streamlit app that predicts the next word based on user input. It learns word patterns from sample sentences and suggests possible next words.

Objective

To understand the basic working of language models using Python.

How It Works
Sentences are split into words.
Word relationships are stored in a dictionary.
The app predicts the next word using the last entered word.
Streamlit provides the web interface.
Workflow

User Input → Pattern Learning → Prediction → Output

Technologies Used
Python
Streamlit
Dictionary & Lists
Features
Simple web interface
Real-time prediction
Pattern-based learning
Example

Input: i love eating
Output: ice, cream

Run the Project

Install Streamlit:

pip install streamlit

Run the app:

python -m streamlit run mini_llm.py

Open in browser:

http://localhost:8501
Learning

This project shows how basic next-word prediction works using previous word patterns.

Future Improvements
Use larger datasets
Add probability-based prediction
Improve accuracy with ML models
Create a chatbot interface
Note

This is a mini simulation of a language model, not a full LLM.
