import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import streamlit as st
import random as r
from PIL import Image
import time
from Database import get_connection
from datetime import datetime as dt

def start():

    if "target" not in st.session_state:
        st.session_state.target = 399

    if "p1" not in st.session_state:
        st.session_state.p1 = 0

    if "p2" not in st.session_state:
        st.session_state.p2 = 0

    if "Player" not in st.session_state:
        st.session_state.Player = 1

    if "game_over" not in st.session_state:
        st.session_state.game_over = False

    if "image" not in st.session_state:
        st.session_state.image = 0

    if "image1" not in  st.session_state:
        st.session_state.image1 = 0

    st.title("Dice Challenger by Developer SriRam..")

    st.subheader(f"Your Target : {st.session_state.target}")

    n=399
    def Person_1():
        st.session_state.image = n
        if n>1:
            st.session_state.p1 +=n
        if st.session_state.p1 >= st.session_state.target:
            st.session_state.p1 = st.session_state.target
            st.set_page_config(layout="centered")
            st.success(f"{st.session_state.name} you Won the Match..")
            st.session_state.game_over=True
            st.balloons()
        if n==1:
            st.session_state.p1 *=0
        st.session_state.image = n

    def Person_2():
        st.session_state.image1 = n
        if n>1:
            st.session_state.p2 +=n
        if st.session_state.p2 >= st.session_state.target:
            st.session_state.p2 = st.session_state.target
            st.set_page_config(layout="centered")
            st.success("Player_2 you Won the Match..")
            st.session_state.game_over = True
            st.balloons()
        if n==1:
            st.session_state.p2 *=0
        
        
    col1, col2, col3, col4 = st.columns(4)



    with col1:
        if st.button("🎲 Roll",disabled=(st.session_state.game_over)):
            st.session_state.Player = 1
            st.rerun()

    with col2:
        if st.button("🤚 Hold",disabled=(st.session_state.game_over)):
            if st.session_state.Player == 1:
                st.session_state.Player = 2
            st.rerun()

    if st.session_state.Player == 1:
            Person_1()
    elif st.session_state.Player == 2:
            Person_2()

    col1,col2 = st.columns(2)

    with col1:
        if st.session_state.image == 1:
            img = Image.open("dice_1.png")
            st.image(img, caption="Dice 1",width=250)
        if st.session_state.image ==2:
            img1 = Image.open("dice_2.png")
            st.image(img1, caption="Dice 2",width=250)
        if st.session_state.image ==3:
            img1 = Image.open("dice_3.png")
            st.image(img1, caption="Dice 3",width=250)
        if st.session_state.image ==4:
            img1 = Image.open("dice_4.png")
            st.image(img1, caption="Dice 4",width=250)
        if st.session_state.image ==5:
            img1 = Image.open("dice_5.png")
            st.image(img1, caption="Dice 5",width=250)
        if st.session_state.image ==6:
            img1 = Image.open("dice_6.png")
            st.image(img1, caption="Dice 6",width=250)
        
            

    with col2:
        st.subheader(f"Your skipped Score : 1")
    col1, col2 = st.columns(2)

    with col1:
        st.number_input("Player Score",value = st.session_state.p1, disabled=True)
def mobile(Mobile):
    import re
    now = dt.now().strftime("%y-%m-%D %H-%M-%S")
    if not re.search(r'^[6-9]\d{9}$',Mobile):
        return "Mobile number starts with 6,7,8,9 only and contains be 10 digits"
    else:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""Insert or Ignore into Won(
                    mobile,status,created_at
                    )values(?,?,?)""",(Mobile,False,now))
        conn.commit()
        cur.execute("select Name from Won where Mobile = ?",(Mobile,))
        f=cur.fetchone()
        if f:
            st.session_state.name = f[0]
        st.write(st.session_state.name)
        conn.close()
        return "You are Registered Successfully.."
    
