import streamlit as st
import pandas as pd
import base64
import os
from io import BytesIO

#PAGE CONFIG
st.set_page_config(page_title="CourseFile app", layout="wide")


def get_download_link(path_to_excel):
    """
    Generate a download link for an Excel file
    """
    # Read the Excel file into a dictionary of DataFrames
    xls = pd.ExcelFile(path_to_excel, engine='openpyxl')
    
    # Save the Excel file to a BytesIO object
    excel_file = BytesIO()
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        for sheet_name in xls.sheet_names:
            xls.parse(sheet_name).to_excel(writer, sheet_name=sheet_name, index=False)
    
    # Seek to the beginning of the BytesIO object
    excel_file.seek(0)
    
    # Encode the BytesIO object to base64
    b64 = base64.b64encode(excel_file.read()).decode()

    # Generate the download link
    download_link = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{path_to_excel.split("/")[-1]}">Format_Excel_Course_Info.xlsx</a>'
    
    return download_link



def append_excel_files(uploaded_files_folder):
    """
    Append uploaded Excel files to an existing folder
    """
    # Create a folder if it doesn't exist
    if not os.path.exists(uploaded_files_folder):
        os.makedirs(uploaded_files_folder)
    
    # Iterate through each uploaded file
    for uploaded_file in st.file_uploader("Upload Excel file(s)", type=["xlsx", "xls"], accept_multiple_files=True):
        if uploaded_file is not None:
            # Get the file name
            file_name = uploaded_file.name
            
            # Construct the file path
            file_path = os.path.join(uploaded_files_folder, file_name)
            
            # Check if the file already exists
            if os.path.exists(file_path):
                st.warning(f"File : '{file_name}' already exists. It will be overwritten.")
            
            # Store the file on disk
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getvalue())
            
            button_clicked = st.button("UPDATE")
            if button_clicked:
                st.success(f"Course File : :green[{file_name}] Updated Successfully!")


def uploadexcelpage():
    
    st.subheader("Download Format excel ➡️ Input data ➡️ Upload to add in Courses")
    with st.container():
        st.markdown("### :gray[NOTE :]")
        st.write(":gray[FOLLOW BELOW STEPS TO DOWNLOAD FORMAT EXCEL AND ENTER USER INPUT IN IT. AFTERWARDS YOU WILL BE GIVEN DATA INPUT IN TABULAR/GRAPHICAL VIEW OF DATA.]")
        
        st.write("---------------------------------------------")
        st.write("STEP 1 : Download the format excel file for input.")
        path_to_excel = "Course_file_format/Format_Excel_Course_Info.xlsx"
        download_link = get_download_link(path_to_excel)
        st.markdown(download_link, unsafe_allow_html=True)
        st.write("---------------------------------------------")
        st.write("STEP 2 : Input data into the downloaded excel in your system.")
        st.write("---------------------------------------------")
        st.write("STEP 3 : Upload the edited file here to add in Courses")

        uploaded_files_folder = "courses_inputs"
        append_excel_files(uploaded_files_folder)
        
        st.write("---------------------------------------------")
        st.subheader("Hit :red[ADD COURSE] to add in Courses List")

        button_clicked = st.button("ADD COURSE")
        if button_clicked :
            st.success("Course Added Successfully!")



uploadexcelpage()