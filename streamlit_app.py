import streamlit as st
# Create two rows and three columns
row1_col1, row1_col2, row1_col3 = st.columns(3)
row2_col1, row2_col2, row2_col3 = st.columns(3)
# Add content to the cells
with row1_col1:
 st.write("Row 1, Column 1")
 # Add your content for this cell
with row1_col2:
 st.write("Row 1, Column 2")
 # Add your content for this cell
 ith row1_col3:
 st.write("Row 1, Column 3")
 # Add your content for this cell
with row2_col1:
 st.write("Row 2, Column 1")
 # Add your content for this cell
with row2_col2:
 st.write("Row 2, Column 2")
 # Add your content for this cell
with row2_col3:
 st.write("Row 2, Column 3")
 # Add your content for this cell
