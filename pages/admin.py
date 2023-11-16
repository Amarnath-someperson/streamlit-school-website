import streamlit as st
from utils.auth import Authenticate


st.set_page_config(page_title='Administrator', page_icon =':warning:')

authenticate = Authenticate()
st.title('Administration and CSV Upload')
st.write('This page is meant for use by **_site admins_** and **_teachers_**.')
page = st.empty()
with page:
    login_button = authenticate.login()
        

if st.session_state['authentication_status']:
    page.empty()
    st.header(f'Welcome, {st.session_state["name"]}')
    st.subheader('Marksheet upload (csv)')
    
    st.markdown('An uploaded csv must follow a format, as defined by the following rules:')
    
    st.markdown('- The file must have a name consisting of only lowercase letters, digits and underscores.')
    
    st.markdown('- The name of the csv must be such that it represents `class<xx>_q<z><yy>` in form, where `xx` is a number like 10, 12, 01 etc., `z` is the quarter of the year (possible values are 1 and 2), and `yy` is the year. For example, a valid name would be `class10_q223`.  ')
    uploaded_files = st.file_uploader("Upload csv files here.", accept_multiple_files=True)
        