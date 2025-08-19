import streamlit as st
import pandas as pd
import numpy as np

st.title('Cold Drink and Pizza App')
choice = st.radio(
    "What do you want?",
    ("Pizza", "Cold Drink",'Tea',"Pizza and Cold Drink")
)


if choice=='Cold Drink': 
    flavour = st.selectbox('Select Type Of Cold Drink',['Fanta','Pepsi','Mirinda','Coca-Cola','7UP','Sprite'])
    ice=st.button('With Ice')
    without_ice=st.button('Without Ice')


    if ice:
        st.success(f'Ice is added to your {flavour} Cold Drink')
    else:
        st.success(f'Your {flavour} is Ready without Ice')



if choice=='Pizza':
      base=st.radio('Select Base of Your Pizza',['Sour Dough','Plain Dough','Wheat Dough'])
      zaika=st.radio('Select Flavour Of Your Pizza',['BBQ','Tikka','Malai Boti','Crown Crust','Fajita','Cheese and Tomatoes'])
      size=st.radio('Select Size',['Small','Medium','Large','XL'])
      if base and zaika and size:
        st.success(f'Your {size} Size {zaika} Pizza With {base} Will Be Ready in 25 minutes')

if choice=='Pizza and Cold Drink':
      
      flavour = st.selectbox('Select Type Of Cold Drink',['Fanta','Pepsi','Mirinda','Coca-Cola','7UP','Sprite'])
      ice=st.button('With Ice')
      without_ice=st.button('Without Ice')



      base=st.radio('Select Base of Your Pizza',['Sour Dough','Plain Dough','Wheat Dough'])
      zaika=st.radio('Select Flavour Of Your Pizza',['BBQ','Tikka','Malai Boti','Crown Crust','Fajita','Cheese and Tomatoes'])
      size=st.radio('Select Size',['Small','Medium','Large','XL'])


      if ice:
        st.success(f'Ice is added to your {flavour} Cold Drink')
      else:
        st.success(f'Your {flavour} is Ready without Ice')


      if base and zaika and size:
        st.success(f'Your {size} Size {zaika} Pizza With {base} Will Be Ready in 25 minutes')

if choice=='Tea':
    tea_flavour=st.selectbox('Select flavour of Tea',['Masala Tea','Simple Tea','Almond Milk Tea','Cardamom Tea'])
    sugar=st.radio('Select Sugar or Without Sugar',['With Sugar','Without Sugar'])
    if sugar=='With Sugar':
      st.slider('Select Spoons of sugar ',1,5,2)
    cups=st.number_input('How many cups',min_value=1,max_value=25)  

    st.success(f'Your {cups} cups of {tea_flavour} {sugar} will be ready in 15 minutes')
phone_number=st.text_input('Enter Your Phone Number')

if phone_number:  
    if phone_number.isdigit()  :
        st.success(f"Your phone number is: {phone_number}")
    else:
        st.error("❌ Only digits are allowed! Please remove letters or symbols.")
   
dob=st.date_input('Enter Date Of Birth')
st.write(f'You Date Of Birth is {dob}')
   

