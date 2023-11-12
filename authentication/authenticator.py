import jwt
import bcrypt
import streamlit as st
import extra_streamlit_components as stx
from yaml.loader import SafeLoader


with open('./config.yaml') as file:
    CONFIG = yaml.load(file, Loader=SafeLoader)

class Authenticate:
    def __init__(self) -> None:
        self.creds = CONFIG
        self.creds['usernames'] = {key.lower(): value for key, value in CONFIG['usernames'].items()}
        if 'name' not in st.session_state:
            st.session_state['name'] = None
        if 'authentication_status' not in st.session_state:
            st.session_state['authentication_status'] = None
        if 'username' not in st.session_state:
            st.session_state['username'] = None
        if 'logout' not in st.session_state:
            st.session_state['logout'] = None
        
    def login(message: str):
        st.write(message)
        with st.form("login_widget"):
            username= st.text_input('Username').lower()
            password = st.text_input('Password', type="password")
            # ask for input
            login_button = st.form_submit_button("Login")
            return login_button