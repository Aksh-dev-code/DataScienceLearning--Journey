import streamlit as st

st.title("The Heabits that will change your life")
st.subheader("Be your best version")
st.text("Hope you build good habits live a better life")
st.write("Small changes can make a big difference")

habits = st.selectbox("Choose a habit:", ["Exercise", "Reading", "Meditation", "Cooking", "Writing","Socializing","Mindfulness"])

st.write(f"You have chosen to build the habit of {habits}.Good luck on your journey!")
