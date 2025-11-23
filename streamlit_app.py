import streamlit as st

st.title("My Streamlit App Layout Demo")

col1,col2 = st.columns(2)
with col1:
    st.header("This is column 1")
    st.write("This is the left column")

with col2:
    st.header("This is column 2")
