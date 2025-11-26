import streamlit as st
# Add a title to the app
st.title("Interactive Widget Example")
# Add a slider widget
selected_value = st.slider("Select a value", 1, 10)
# Display a message based on the selected value
st.write(f"You selected: {selected_value}")
