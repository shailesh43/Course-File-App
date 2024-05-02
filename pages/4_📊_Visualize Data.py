import streamlit as st
import os
import plotly.express as px
import pandas as pd
#PAGE CONFIG
st.set_page_config(page_title="CourseFile app", layout="wide")

# READ EXCEL WITH PLOTTING
def plot_excel_sheet_attainment(directory):
    """
    Plot bar chart and line chart for the 'CO Attainment' and 'PO_PSO_Attainment' sheets from an Excel file
    """
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter only Excel files
    excel_files = [file for file in files if file.endswith('.xlsx') or file.endswith('.xls')]
    
    # Create a dropdown menu to select Excel files
    selected_excel_file = st.selectbox("SELECT COURSE :", excel_files, key="plot_attainment")

    if selected_excel_file:
        file_path = os.path.join(directory, selected_excel_file)
        
        try:
            with st.expander("CO Attainment"):
                # Read the data from "CO Attainment" sheet, skipping the target column
                df_co = pd.read_excel(file_path, sheet_name="CO Attainment", usecols=lambda x: x != 'Target', index_col=0)
                
                #Plots subheader
                st.subheader("Plots for CO Attainment")
                left, right = st.columns(2, gap="large")
                # Plot bar chart for "Attainment" and "Gap" column
                with left :
                    fig_bar_co = px.bar(df_co, x=df_co.index, y=['Attainment', 'Gap'], barmode='group', labels={'x': 'Index'}, title='Barchart 📊')
                    st.plotly_chart(fig_bar_co)
                # st.write("---")
                # Plot line chart for "Attainment" and "Gap" columns
                with right:
                    fig_line_co = px.line(df_co, x=df_co.index, y=['Attainment', 'Gap'], labels={'x': 'Index'}, title='Linechart 📈')
                    st.plotly_chart(fig_line_co)
            with st.expander("PO-PSO Attainment"):
                # Read the data from "PO_PSO_Attainment" sheet, skipping the target column
                df_po_pso = pd.read_excel(file_path, sheet_name="PO_PSO_Attainment", usecols=lambda x: x != 'Target', index_col=0)
                
                #Plots subheader
                st.subheader("Plots for PO-PSO Attainment")
                left1, right1 = st.columns(2)
                # Plot bar chart for "Attainment" and "Gap" column
                with left1:
                    fig_bar_po_pso = px.bar(df_po_pso, x=df_po_pso.index, y=['Attainment', 'Gap'], barmode='group', labels={'x': 'Index'}, title='Barchart 📊')
                    st.plotly_chart(fig_bar_po_pso)
                # st.write("---")
                # Plot line chart for "Attainment" and "Gap" columns
                with right1:
                    fig_line_po_pso = px.line(df_po_pso, x=df_po_pso.index, y=['Attainment', 'Gap'], labels={'x': 'Index'}, title='Linechart 📈')
                    st.plotly_chart(fig_line_po_pso)
            with st.expander("UT Marks"):
                # Read the data from the Excel file
                df_ut = pd.read_excel(file_path, sheet_name="UTMarks")
                
                # Plots subheader
                st.subheader("Student Marks Visualization")
                st.write("---")
                # Option to choose between bar plot or line plot
                left, right = st.columns(2, gap="large")
                with left:
                    plot_bar_chart(df_ut)
                with right:
                    st.write(df_ut)
            
    
        except Exception as e:
            st.error(f"An error occurred while plotting sheets from file {selected_excel_file}: {e}")


import plotly.graph_objs as go


def plot_bar_chart(df):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['Student Name'], y=df['UT1'], name='UT1'))
    fig.add_trace(go.Bar(x=df['Student Name'], y=df['UT2'], name='UT2'))
    fig.add_trace(go.Bar(x=df['Student Name'], y=df['UT AVG'], name='UT AVG'))
    fig.update_layout(barmode='group', title='Student Marks in UT1, UT2, and UT AVG', xaxis_title='Student Name', yaxis_title='Marks')
    st.plotly_chart(fig)



def formspage():
    directory = "courses_inputs"

    st.header("📊 Visulaize Data")
    st.write(":gray[HERE YOU CAN VIEW ANY COURSE'S DATA VISUALIZATION]")
    st.write("---")

    st.subheader(''':blue[Visualize] Course File as plots / charts / graphs''')
    st.write("---")
    plot_excel_sheet_attainment(directory)
    st.write("---")
    

formspage()