import streamlit as st

st.title("Hello, Streamlit!")
st.subheader("This is a simple web app.")
st.text("Welcome to your first Streamlit app.")
st.write("The data science journey begins here.")

skills = st.selectbox("Choose a skill:", ["Python", "Data Analysis", "Machine Learning", "Deep Learning", "NLP"])

st.write(f"You are learning {skills}.Hope you are enjoying it!")