import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import streamlit as st
import string as s
from Database import get_connection
from Game import mobile,start

st.set_page_config(page_icon="🎲",page_title="Dice Challenger",layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "Login"

if "name" not in st.session_state:
        st.session_state.name = "RAMA"

with st.sidebar:
    st.title("🎲 Dice Challenger")
    st.divider()

    st.markdown("""<h2 style='color:orange;font-size:14'>Game Instructions </h2><p><b>
            1. if Dice number is 1 your Present Score will be Zero(0)<br> 2. If you want to Pass the Chance use Hold </b></p><p><u> If you Won the Game, you will Recieve <b style='color:Red'>Rs :200/-</b><p>No cheating</p>""",unsafe_allow_html=True)
    
if st.session_state.page == "Login":
    st.markdown("""<h2 style='color:orange;font-size:14'>Login with your Mobile number For Payment purpose </h2><p><b>""",unsafe_allow_html=True)
    st.title("Login Page")
    with st.form("Login"):
        name = st.text_input("Enter your name : ")
        Mobile = st.text_input("Enter your Mobile Number : ")
        submit = st.form_submit_button("Login")
    if submit:
        if Mobile.strip()=="" or name.strip()=="":
            st.toast("❌ No Spaces Allowed Fill the Details")
        elif any(char in s.digits for char in name) or any(char in s.punctuation for char in name):
            st.toast("No Numbers and Symbols allowed in Name")
        else:
            conn = get_connection()
            cur  = conn.cursor()

            cur.execute("""insert or ignore into Won(Name)values(?)""",(name,))
            conn.commit()
            st.checkbox("Name",True)
        if mobile(Mobile) == "You are Registered Successfully..":
            st.checkbox("Mobile Number",True)
            st.session_state.page = "start"
            
elif st.session_state.page == "start":
    st.subheader("Welcome to Dice Challenger")
    st.success("All the Best all my players 👍")
    with st.sidebar:
        if st.button("Play"):
            st.session_state.page = "Play"
            st.rerun()
        else:
            st.link_button("Exit","WWW.Google.com")
            st.rerun()
elif st.session_state.page == "Play":
    start()

