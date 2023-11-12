import jwt
import bcrypt
import streamlit as st
import extra_streamlit_components as stx
import yaml
from yaml.loader import SafeLoader


with open('./config.yaml') as file:
    CONFIG = yaml.load(file, Loader = SafeLoader)

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
            st.session_state['logout'] = None # Streamlit blog
        
    def login(self, message: str = '') -> None:
        if not st.session_state['authentication_status']:
            st.write(message)
            with st.form("login_widget"):
                self.username = st.text_input('Username').lower()
                self.password = st.text_input('Password', type="password")
                st.session_state['username'] = self.username
                st.session_state['password'] = self.password
                # ask for input
                if st.form_submit_button("Login"):
                    self._cred_check()
                    return st.session_state['name'], st.session_state['authentication_status'], st.session_state['username']

        
    def _check_pw(self):
        encoded_pw = self.password.encode('utf-8')
        
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(encoded_pw, salt)
                
        return bcrypt.checkpw(self.creds['usernames'][self.username]['password'].encode('utf-8'), hashed_pw)
    
    def _cred_check(self) -> None:
        if self.username in self.creds['usernames']:
            try:
                if self._check_pw():
                    st.session_state['name'] =self.creds['usernames'][self.username]['name']
                    st.session_state['authentication_status'] = True
                else:
                    st.session_state['authentication_status'] = False
            except Exception as e:
                st.write(e)
        else:
            st.session_state['authentication_status']  = False