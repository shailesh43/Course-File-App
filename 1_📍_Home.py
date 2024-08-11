import streamlit as st
from streamlit_lottie import st_lottie
import json
from PIL import Image


#PAGE CONFIG
st.set_page_config(page_title="CourseFile app",page_icon="cfa_logo.svg", layout="wide")

#LOAD LOTTIE FILES
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)



#home main
def homepage():
    # Use local CSS

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # local_css("styles\style.css")
    # ---- LOAD ASSETS ----
    lottie_coding = load_lottiefile("images/coding.json")
    lottie_excelgif = load_lottiefile("images/excel_gif.json")

    # ---- HEADER SECTION ----
    with st.container():
        st.title("Welcome to CourseFileAPP")
        st.write(":gray[PYTHON BASED MINIMAL COURSE MANAGEMENT APP]")
        
    
    # ---- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What will this app do?")
            st.write("##")
            st.write(
                """
                CourseFileapp is a comprehensive web application designed to streamline the management of teaching subjects within colleges. It provides a centralized platform for organizing and accessing vital information such as syllabus, learning outcomes, and academic performance metrics for individual classes. By leveraging advanced data management and visualization techniques, CourseFileapp empowers educators and administrators to efficiently monitor and analyze academic progress, facilitating informed decision-making and enhancing overall educational outcomes.
                """
            )
        with right_column:
            st_lottie(lottie_excelgif, height=300, key="coding")

    st.write("---")
    with st.container():
        st.subheader(":green[CRUD] Operations in excel file  ")
        st.write("---")
        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.image("images/read_course.png")
            with right_column:
                st.image("images/updation.png")
            st. write("---")
        st.subheader(":blue[Data visualize] its contents")
        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.image("images/data_visualise.png")
            with right_column:
                st.image("images/marks_visualize.png")
        

    st.markdown("© 2024 Course File APP. All rights reserved. Created with python by :blue[shailesh]")   
    




homepage()