import streamlit as st
st.write("Hello!")

categories = ['a', 'b', 'c']
st.multiselect("pick an option!", categories)
st.sidebar.button("Click me!")
if st.checkbox("Select me!"):
  st.write("you selected the checkbox!")
