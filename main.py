import streamlit as st
from authentication.authenticator import Authenticate
from st_pages import Page, show_pages, add_page_title

st.set_page_config(page_title='Student Analysis', page_icon ='favicon.png')

hide_st_style = """
    <style>#MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
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
student_col, admin_col = st.columns(2)


with student_col:
    st.header('Student Login')
    
with admin_col:
    st.header('Administrator Login')
    login_button = authenticate.login('This login is for site administrators and teachers.')
    
if login_button:
    if st.session_state['authentication_status']:
        st.write(f"""Login Complete 
                 
            Welcome {st.session_state['name']}""")