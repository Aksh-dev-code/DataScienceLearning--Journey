import streamlit as st

st.title("Be the best version of yourself")

if st.button("Make chai"):
    st.success("Chai is ready!")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added!")

base = st.radio("Choose your Chai Base:", ("Water","Milk","Almond Milk","Oat Milk"))
st.write(f"Selected base: {base}")
flavor = st.selectbox("Choose your Chai Flavor:", ["Ginger","Cardamom","Tulsi","Elaichi","Saffron"])
st.write(f"Selected flavor: {flavor}")

sugar = st.slider("Select sugar level (in tsp):", 0, 5, 2)
st.write(f"Selected sugar level: {sugar} tsp")

num_cups = st.number_input("How many cups of chai would you like?", min_value=1, max_value=10, value=1, step=1)
st.write(f"Selected number of cups: {num_cups}")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Thank you, {name}! Your chai will be ready soon.")
dob = st.date_input("Enter your date of birth:")
st.write(f"Your date of birth is: {dob}")