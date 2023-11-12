import streamlit as st
import streamlit_authenticator as stauth
import pandas as pdpip
import numpy as np
from widgets import Forms

from yaml.loader import SafeLoader

st.set_page_config(page_title='Student Analysis', page_icon ='favicon.png')

st.title('Silver Hills Public School')

student_col, admin_col = st.columns(2)
with student_col:
    st.header('Student Login')
with admin_col:
    st.header('Administrator Login')
    login_button = Forms.login('This login is for site administrators and teachers.')
    
    
if login_button:
    st.write('login functionality yet to be created. _authentication to do_.')