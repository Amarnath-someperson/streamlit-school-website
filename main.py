import streamlit as st
from authentication.authenticator import Authenticate
from st_pages import Page, show_pages, add_page_title


st.set_page_config(page_title='Student Analysis', page_icon ='favicon.png')


hide_st_style = """
    <style>
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

st.sidebar.title('Constructing...')
st.sidebar.write('something will be here soon...')

show_pages(
    [
        Page("main.py", "Home", "🏠"),
        Page("pages/admin.py", "Site Administration", ":warning:"),
    ]
)

st.title('Silver Hills Public School')
authenticate = Authenticate()

st.header('Student Portal')