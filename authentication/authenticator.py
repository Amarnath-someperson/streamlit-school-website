import jwt
import bcrypt
import streamlit as st
import extra_streamlit_components as stx
import yaml
from yaml.loader import SafeLoader


with open('./config.yaml') as file:
    CONFIG = yaml.load(file, Loader=SafeLoader)

class Authenticate:
    def __init__(self) -> None:
        self.creds = CONFIG['credentials']
        self.creds['usernames'] = {key.lower(): value for key, value in CONFIG['credentials']['usernames'].items()}
        if 'name' not in st.session_state:
            st.session_state['name'] = None
        if 'authentication_status' not in st.session_state:
            st.session_state['authentication_status'] = None
        if 'username' not in st.session_state:
            st.session_state['username'] = None
        if 'logout' not in st.session_state:
            st.session_state['logout'] = None
        
    def login(self, message: str):
        if not st.session_state['authentication_status']:
            st.write(message)
            with st.form("login_widget"):
                self.username= st.text_input('Username').lower()
                self.password = st.text_input('Password', type="password")
                st.session_state['username'] = self.username
                st.session_state['password'] = self.password
                # ask for input
                if st.form_submit_button("Login"):
                    pass                
        return True