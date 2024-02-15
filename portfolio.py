import streamlit as st

co1,co2=st.columns(2)
with co1:
    st.title("Hello I'm CH.GAGAN RAJ\n")
with co2:
    st.info("Hello every one my self CH.GAGAN RAJ Iam presenting you my portfolio "
            "web page bulid by python."
            "Iam doing my Btech in CMR THENCAL CAMPUS in the department AIML."
            "Iam a student and my passout year is 2026"
            "Iam very much passionate about learning new technologies" 
            "you can know my projects down the page")
st.subheader("ABOUT ME")
img=[('image/pro.jpg','translation bot using python'),('image/web.png','Redircting urls using c'),('image/todo.jpg','todo using python')]
tab1,tab2=st.tabs(['myprojects','my skills'])
with tab1:
    st.subheader('My Projects')
    co3,co4=st.columns(2)
    with co3:
        for i,j in img:
            st.image(i,caption=j,width=200)
    with co4:
        st.info("This project is about the translation bot using python and streamlit module.This project work on a webpage in local address.This webpage is not depolyed.In this we used google tras moudule to translate the given content.")
        for i in range(7):
            st.write('\n')
        st.info("This project is a command prompt based project.This helps to redirect to the desired urls by users command.This project is done in the language c.")
        for i in range(7):
            st.write('\n')
        st.info('This project is about making our own Todo list.This project helps users to list out their daily activities,This project is done in pyhton in two different ways.one is in command prompt and another one is in web page')
lan=['c language','python language']
with tab2:
    st.subheader('Languages known')
    for i in lan:
        st.write(i,'\n')
    st.subheader("certification")
    st.write('Completion of C Training from spoken english IIT bombay')
    st.write('completion certificate of basics of python by infosys spring board')
    st.subheader("Achivements")
    st.write("3 stars in problem solving - hackerrank")
    st.write("4 stars in c language - hackerrank")
    st.write('58442 Global rank - codechef')
    st.write('19,17,513 Global rank - Leetcode')

