import streamlit as st
from authentication.authenticator import Authenticate

st.set_page_config(page_title='Administrator', page_icon =':warning:')

authenticate = Authenticate()

st.title('Administration and CSV Upload')
st.write('This page is meant for use by **_site admins_** and **_teachers_**.')
page = st.empty()
with page:
    login_button = authenticate.login()
        
if login_button:
    page.empty()
    if st.session_state['authentication_status']:
        st.header(f'Welcome, {st.session_state["name"]}')
            