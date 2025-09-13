import streamlit as st

st.title('chai test poll')

col1, col2 = st.columns(2)

with col1:
    st.header('Masala Chai')
    vote1 = st.button('Vote for Masala Chai')
    st.image('https://i.pinimg.com/736x/b1/02/9c/b1029cb08385fdd5297dc83d64312025.jpg',width=200)

with col2:
    st.header('Adrak Chai')
    vote2 = st.button('Vote for Adrak Chai')
    st.image('https://i.pinimg.com/736x/c8/0d/0a/c80d0a27dc7fd534c164b226dcf162ab.jpg', width=200)

if  vote1:
    st.success('You voted for Masala Chai!')

if vote2:
    st.success('You voted for Adrak Chai!')

name = st.sidebar.text_input('Enter your name')
tea = st.sidebar.selectbox('Select your favorite tea', ['Masala Chai', 'Adrak Chai', 'Green Tea', 'Black Tea', 'Oolong Tea'])

st.write(f'your chai is getting ready {name}, enjoy your {tea}!')

with st.expander('Show chai making instructions'):
    st.write("""
    1. Boil water
    2. Add tea leaves and spices
    3. Add milk and sugar
    4. Simmer for a few minutes
    5. Strain and serve hot
    """)

    st.markdown("### Enjoy your chai! ☕with love ❤️")
    st.markdown(['>Blog post on making chai'])
