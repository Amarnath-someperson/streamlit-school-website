import streamlit as st

class Forms:
    def __init__(self) -> None:
        pass
    
    def login(message: str):
        st.write(message)
        with st.form("login_widget"):
            username= st.text_input('Username').lower()
            password = st.text_input('Password', type="password")
            # ask for input
            login_button = st.form_submit_button("Login")
            return login_button