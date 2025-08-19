import pandas as pd
import streamlit as st
import requests

st.title('Live Currency Converter')
amount=st.number_input('Enter amount in pkr',min_value=1)
targeted_currency=st.selectbox('Convert To',['USD','AED','INR','TRY'])

if st.button('Convert'):
    url=('https://api.exchangerate-api.com/v4/latest/PKR')
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        rate=data['rates'][targeted_currency]
        converted=rate*amount
        st.success(f'{amount} PKR= {converted :.2f} {targeted_currency}')
    else:
        st.error('Failed to fetch conversion rate')


