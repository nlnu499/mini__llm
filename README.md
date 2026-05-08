# mini__llm
Next Word Prediction System
Project Overview

This project is a simple Streamlit application that demonstrates the basic idea of language models. It learns word patterns from sample sentences and predicts the next word based on user input.

Objective

The objective of this project is to understand how language models work by building a simple next word prediction system using Python.

How It Works

The system uses a small dataset of sentences. It splits the sentences into words and stores relationships between consecutive words in a dictionary. When the user enters input text, the model checks the last word and predicts possible next words based on learned patterns. Streamlit is used to create a simple web interface.

Workflow

User Input → Text Processing → Pattern Learning → Prediction → Output Display

Technologies Used

Python
Streamlit
Basic Data Structures (Dictionary, Lists)

Features

Simple web-based interface
Real-time next word prediction
Pattern-based learning from sample data

Example

Input: i love eating
Output: ice, cream (depending on training data)

How to Run
Install Streamlit if not installed:
pip install streamlit
Go to  project folder:
cd path_to_folder
Run the application:
python -m streamlit run mini_llm.py
Open the link shown in terminal:
http://localhost:8501
Key Learning

This project demonstrates the basic concept of language models where prediction is based on previous word patterns.

Future Improvements

Improve prediction accuracy using machine learning models
Use larger datasets for better results
Add probability-based predictions
Build a chatbot interface

Note

This is a mini simulation of a language model and not a full large language model.
