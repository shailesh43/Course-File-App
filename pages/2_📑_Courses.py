import streamlit as st
import os
import pandas as pd

#PAGE CONFIG
st.set_page_config(page_title="CourseFile app", layout="wide")




# READ EXCEL WITHOUT PLOTTING



def read_excel_files(directory):
    """
    Read all Excel files in a directory and display their sheet contents in a dropdown menu
    """
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter only Excel files
    excel_files = [file for file in files if file.endswith('.xlsx') or file.endswith('.xls')]
    
    # Create a dropdown menu to select Excel files
    selected_excel_file = st.selectbox("Select Excel files", excel_files, key="read_course_excel")
    
    if selected_excel_file:
        st.write(f"Reading Excel file: {selected_excel_file}")
        file_path = os.path.join(directory, selected_excel_file)
        
        # Read all sheets in the selected Excel file
        sheets = pd.read_excel(file_path, sheet_name=None, engine='openpyxl')
        
        # Create a dropdown menu to select sheets
        selected_sheets = st.multiselect("Select sheets", list(sheets.keys()), key="read_course_sheets")
        
        for selected_sheet in selected_sheets:
            st.write(f"\nSheet Name: {selected_sheet}")
            st.write(sheets[selected_sheet])
            st.write("---------------------------------------------")





#DELETE FUNCTION FROM DIRECTORY = course_inputs

def delete_excel_file(file_path):
    """
    Delete a specific Excel file
    """
    try:
        os.remove(file_path)
        st.success(f"File '{file_path}' deleted successfully.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def display_and_delete_excel_files(directory):
    """
    Display all Excel files in a directory in a dropdown menu and provide a button to delete the selected file
    """
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter only Excel files
    excel_files = [file for file in files if file.endswith('.xlsx') or file.endswith('.xls')]
    
    # Create a dropdown menu to select an Excel file
    selected_excel_file = st.selectbox("Select an Excel file to delete", excel_files, key="delete_course_excel")
    
    if selected_excel_file:
        file_path = os.path.join(directory, selected_excel_file)
        
        # Provide a button to delete the selected file
        if st.button(f"Delete {selected_excel_file}"):
            delete_excel_file(file_path)





#? main function
def coursespage():
    st.header("📑 Courses")
    st.write("---")

    directory = "courses_inputs"
    st.subheader("READ COURSES")
    with st.expander("Read a Course File"):
        st.subheader("")
        read_excel_files(directory)
    st.write("---")
    
    st.subheader("DELETE COURSES")
    with st.expander("Delte a Course File"):
        st.subheader("")
        display_and_delete_excel_files(directory)
    st.write("---")
    
    

  

coursespage()