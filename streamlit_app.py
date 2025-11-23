import streamlit as st

st.title("My Streamlit App Layout Demo")

col1,col2 = st.columns(2)
with col1:
    st.header("This is column 1")
    st.write("This is the left column")
    st.image("https://mbluxury1.s3.amazonaws.com/2022/02/25172711/versace.jpg")

with col2:
    st.header("This is column 2")
    st.button("Clike me")
