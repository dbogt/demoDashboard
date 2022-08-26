import streamlit as st
st.write("Hello!")

categories = ['a', 'b', 'c']
st.multiselect("pick an option!", categories)
st.sidebar.button("Click me!")
if st.checkbox("Select me!"):
  st.write("you selected the checkbox!")

import pandas as pd
df = pd.read_html('https://www.iposcoop.com/last-100-ipos/')[0]
st.dataframe(df)
