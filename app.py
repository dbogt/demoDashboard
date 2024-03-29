import streamlit as st
st.write("Hello!")

categories = ['a', 'b', 'c']
st.multiselect("pick an option!", categories)
st.sidebar.button("Click me!")
if st.checkbox("Select me!"):
  st.write("you selected the checkbox!")

import pandas as pd
st.title("Last 100 IPOs")
df = pd.read_html('https://www.iposcoop.com/last-100-ipos/')[0]

industries = df['Industry'].unique()
pickSector = st.multiselect("Pick an industry to filter", industries)

st.dataframe(df)
filterDF = df[df['Industry'].isin(pickSector)]

st.write("Filtered table")
st.dataframe(filterDF)

