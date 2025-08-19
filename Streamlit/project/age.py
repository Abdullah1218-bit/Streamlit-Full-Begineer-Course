import streamlit as st
import datetime

st.title('This App tells your current age')
enter=st.date_input('Enter your Date Of Birth')
today=datetime.date.today()
dob=today-enter

st.write("You selected:", dob)