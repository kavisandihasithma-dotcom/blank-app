#Import the streamlit library
import streamlit as st

st.title("My First Streamlit App")
st.markdown("Welcome to this introductory Streamlit app!")

col1, col2 = st.columns(2)

col1.write("This is Column 1")
col2.write("This is Column 2")
