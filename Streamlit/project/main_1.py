# import streamlit as st

# st.title('Hello I am a Boy!!')
# st.subheader('Its Made From Streamlit')
# st.text('Welcome To First App')
# st.write('Choose your favourite food')

# food = st.selectbox('Your Favourite Food',['Burger','Pizza','Lasgna','Pasta','Nihari'])
# st.write(f'Your Choose {food} very good choice')
# st.success('Your Food has been made')



import streamlit as st
st.title('Welcome To My Website')
st.subheader('We have made a website to take a survey from people which tell me which is the most used programming language')
lang=st.selectbox('Choose Your Favourtie Langauge',['HTML','CSS','JS','JAVA','Python','Ruby','C#'])
st.success(f'Your Have Select {lang}  \nThanks for your survey')