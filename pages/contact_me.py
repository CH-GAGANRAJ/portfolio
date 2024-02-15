import streamlit as st
import pandas as pd

ch = ["phone","email"]
with st.form("form"):
    option = st.selectbox("select one option to contact",ch,index=None)
    st.form_submit_button("submit")

if option == "phone":
    st.info("7093437327")
elif option == "email":
    st.info("227r1a7314@cmrtc.ac.in")
    st.info('chinkagaganraj@gmail.com')
else:
    st.write("noting selected")

