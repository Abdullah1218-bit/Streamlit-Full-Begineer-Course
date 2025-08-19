import streamlit as st
st.title('Making Poll of Linkedin and Upwork')

col1,col2=st.columns(2)

with col1:

    st.header('Linkedin')
    st.image('https://imgs.search.brave.com/ZtKciIPFtc5ZJmg268AwqSgwqDgv_vXXQKT3XOxZ5f4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/bG9nby53aW5lL2Ev/bG9nby9MaW5rZWRJ/bi9MaW5rZWRJbi1J/Y29uLUxvZ28ud2lu/ZS5zdmc',width=100)

    vote_1=st.button('Click This Button to Vote Linkedin')
with col2:

    st.header('Upwork')
    st.image('https://imgs.search.brave.com/V7DBO1z3i-Np-CUCvmYSv9O7xg937wM0hKwS8KE8pRA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9sb2dv/cy13b3JsZC5uZXQv/d3AtY29udGVudC91/cGxvYWRzLzIwMjEv/MDQvVXB3b3JrLUxv/Z28tMS01MDB4Mjgx/LnBuZw',width=100)

    vote_2=st.button('Click This Button to Vote Upwork')

if vote_1:
    st.success('Thanks for voting Linked ')
elif vote_2:
    st.success('Thanks for voting Upwork')

name=st.sidebar.text_input('Enter Your Name')
app=st.sidebar.selectbox('Chose Your Platform',['Linkedin','Upwork'])

st.write(f'Welcome {name} here is your feedback {app}')

with st.expander('Here is instructions'): 
    st.write(""" 
             
    1)Posts        
    2)Poll        
    3)Time Pass       
    4)Knowledge 
""")
    
st.markdown('# Welcome To App')
st.markdown('> Blockquote')