import streamlit as st
import streamlit_authenticator as stauth
import pandas as pdpip
import numpy as np
import yaml
from yaml.loader import SafeLoader

st.set_page_config(page_title='Student Analysis', page_icon = 'https://images.app.goo.gl/46ngdkqwdCEaQoWb9')

with open('./config.yaml') as file:
    CONFIG = yaml.load(file, Loader=SafeLoader)

st.title('Silver Hills Public School')

student_col, teacher_col = st.columns(2)
with student_col:
    st.header('Login as Student')
with teacher_col:
    st.header('Login as Teacher')
    with st.form("login_widget"):
        username= st.text_input('Username').lower()
        password = st.text_input('Password')
        # ask for input
        login_button = st.form_submit_button("Login")
    
if login_button:
    st.write('login functionality yet to be created. _authentication to do_.')