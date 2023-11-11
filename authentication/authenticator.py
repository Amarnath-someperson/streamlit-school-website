import jwt
import bcrypt
import streamlit as st
import extra_streamlit_components as stx

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
        
    def teacher_login():
        