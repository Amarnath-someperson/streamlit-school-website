import jwt
import bcrypt
import streamlit as st
import extra_streamlit_components as stx
import yaml

with open('./config.yaml') as file:
    CONFIG = yaml.load(file, Loader=SafeLoader)

class Authenticate:
    def __init__(self, creds: dict) -> None:
        self.creds = creds
        if 'name' not in st.session_state:
            st.session_state['name'] = None
        if 'authentication_status' not in st.session_state:
            st.session_state['authentication_status'] = None
        if 'username' not in st.session_state:
            st.session_state['username'] = None
        if 'logout' not in st.session_state:
            st.session_state['logout'] = None
        
    def admin_login():
        