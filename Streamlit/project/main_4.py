import pandas as pd
import numpy as np
import streamlit as st

st.title('Chai Sales Dashboard')
file=st.file_uploader('Upload Your File',['csv'])
if file:
    df =pd.read_csv('chai_sales.csv')
    st.subheader('Your Data Preview')
    st.dataframe(df)
    if file:
        st.subheader('Data Stats')
        st.write(df.describe())
    if file:
        city=df['City'].unique()
        selected_city=st.selectbox('Filter by cites',city)
        filtered_data=df[df["City"] == selected_city]
        st.dataframe(filtered_data)