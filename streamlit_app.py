import streamlit as st

st.title("My Streamlit App Layout Demo")

# Top section
with st.container():
    st.header("Overview Section")

    col1, col2 = st.columns(2)
    col1.write("Left side content (text, charts, etc.)")
    col2.write("Right side content")

# Middle section
with st.container():
    st.header("Statistics Section")

    colA, colB, colC = st.columns(3)

    colA.metric("Sales", "1500", "+10%")
    colB.metric("Visitors", "5000", "-5%")
    colC.metric("Profit", "$12,000", "+3%")

# Bottom section
with st.container():
    st.header("Details Section")

    col_left, col_right = st.columns([1.5, 1])
    
    col_left.write("Big chart or table goes here")
    col_right.write("Small widgets or filters here")
