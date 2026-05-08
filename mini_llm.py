import streamlit as st

st.title("Next Word Prediction Demo")

# Sample training data
data = [
    "i love eating ice cream",
    "i love machine learning",
    "i love artificial intelligence",
    "how are you doing",
    "good morning everyone",
    "python is awesome",
    "machine learning is powerful"
]

# Build simple pattern model
model = {}

for sentence in data:
    words = sentence.lower().split()

    for i in range(len(words) - 1):
        word = words[i]
        next_w = words[i + 1]

        if word not in model:
            model[word] = []

        model[word].append(next_w)

# Prediction function
def predict(text):
    words = text.lower().split()
    last = words[-1]

    if last in model:
        return model[last][:3]
    else:
        return ["No result"]

# UI
input_text = st.text_input("Enter text:")

if st.button("Predict"):
    result = predict(input_text)
    st.write("Prediction:", result)

st.subheader("Process Flow")
st.write("Input > Word pattern>  Output")

if st.checkbox("Show data patterns"):
    st.write(model)
