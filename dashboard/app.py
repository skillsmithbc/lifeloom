import streamlit as st
import pandas as pd

# Dummy data
df = pd.DataFrame({
    'Name': ['User1', 'User2'],
    'Risk Score': [7.5, 11.2],
    'Risk Level': ['Medium', 'High']
})

st.title("Lifeloom Counselor Dashboard")
st.dataframe(df)
