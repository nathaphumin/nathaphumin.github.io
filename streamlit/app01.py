import streamlit as st

st.header('My Web Site')
st.subheader('website')
st.write('hello')
st.image('https://picsum.photos/900/250')
b = st.button('click!')

t = st.text_input('input')
if t :
    st.write(f'hello {t}')
    st.button('click')
