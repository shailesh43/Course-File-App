import streamlit as st
import os
import plotly.express as px
import pandas as pd
#PAGE CONFIG
st.set_page_config(page_title="CourseFile app", layout="wide")




# READ EXCEL WITH PLOTTING


# # CO Attainment

# def plot_excel_sheet_CO_Attainment(directory):
#     """
#     Plot bar chart and line chart for the 'CO Attainment' sheet from an Excel file
#     """
#     # List all files in the directory
#     files = os.listdir(directory)
    
#     # Filter only Excel files
#     excel_files = [file for file in files if file.endswith('.xlsx') or file.endswith('.xls')]
    
#     # Create a dropdown menu to select Excel files
#     selected_excel_file = st.selectbox("SELECT COURSE :", excel_files, key="plot_co_attainment")

#     if selected_excel_file:
#         file_path = os.path.join(directory, selected_excel_file)
        
#         try:
#             # Read the data from "CO Attainment" sheet, skipping the target column
#             df = pd.read_excel(file_path, sheet_name="CO Attainment", usecols=lambda x: x != 'Target', index_col=0)
            
#             #Plots subheader
#             st.subheader("Plots for CO Attainment")

#              # Plot bar chart for "Attainment" and "Gap" column
#             fig_bar = px.bar(df, x=df.index, y=['Attainment', 'Gap'], barmode='group', labels={'x': 'Index'}, title='Barchart 📊')
#             st.plotly_chart(fig_bar)
#             st.write("---")
#             # Plot line chart for "Attainment" and "Gap" columns
#             fig_line = px.line(df, x=df.index, y=['Attainment', 'Gap'], labels={'x': 'Index'}, title='Linechart 📈')
#             st.plotly_chart(fig_line)
            
#         except Exception as e:
#             st.error(f"An error occurred while plotting 'CO Attainment' sheet from file {selected_excel_file}: {e}")
# # CO Attainment
# def plot_excel_sheet_PO_PSO_Attainment(directory):
#     """
#     Plot bar chart and line chart for the 'PO_PSO_Attainment' sheet from an Excel file
#     """
#     # List all files in the directory
#     files = os.listdir(directory)
    
#     # Filter only Excel files
#     excel_files = [file for file in files if file.endswith('.xlsx') or file.endswith('.xls')]
    
#     # Create a dropdown menu to select Excel files
#     selected_excel_file = st.selectbox("SELECT COURSE :", excel_files, key="plot_po_pso_attainment")

#     if selected_excel_file:
#         file_path = os.path.join(directory, selected_excel_file)
        
#         try:
#             # Read the data from "PO_PSO_Attainment" sheet, skipping the target column
#             df = pd.read_excel(file_path, sheet_name="PO_PSO_Attainment", usecols=lambda x: x != 'Target', index_col=0)
            
#             #Plots subheader
#             st.subheader("Plots for PO_PSO_Attainment")

#              # Plot bar chart for "Attainment" and "Gap" column
#             fig_bar = px.bar(df, x=df.index, y=['Attainment', 'Gap'], barmode='group', labels={'x': 'Index'}, title='Barchart 📊')
#             st.plotly_chart(fig_bar)
#             st.write("---")
#             # Plot line chart for "Attainment" and "Gap" columns
#             fig_line = px.line(df, x=df.index, y=['Attainment', 'Gap'], labels={'x': 'Index'}, title='Linechart 📈')
#             st.plotly_chart(fig_line)
            
#         except Exception as e:
#             st.error(f"An error occurred while plotting 'PO_PSO_Attainment' sheet from file {selected_excel_file}: {e}")


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








# def visualize_student_marks(directory):
#     """
#     Visualize student marks data from an Excel file using various Plotly Express visualization figures
#     """
#     # List all files in the directory
#     files = os.listdir(directory)
    
#     # Filter only Excel files
#     excel_files = [file for file in files if file.endswith('.xlsx') or file.endswith('.xls')]
    
#     # Create a dropdown menu to select Excel files
#     selected_excel_file = st.selectbox("SELECT FILE :", excel_files, key="visualize_student_marks")

#     if selected_excel_file:
#         file_path = os.path.join(directory, selected_excel_file)
        
#         try:
#             # Read the data from the Excel file
#             df = pd.read_excel(file_path)
            
#             # Plots subheader
#             st.subheader("Student Marks Visualization")
            
#             # Plot box plot for distribution of UT1, UT2, UT AVG marks
#             fig_box = go.Figure()
#             fig_box.add_trace(go.Box(y=df['UT1'], name='UT1'))
#             fig_box.add_trace(go.Box(y=df['UT2'], name='UT2'))
#             fig_box.add_trace(go.Box(y=df['UT AVG'], name='UT AVG'))
#             fig_box.update_layout(title="Distribution of Unit Test Marks", xaxis_title="Unit Test", yaxis_title="Marks")
#             st.plotly_chart(fig_box)
#             st.write("---")
            
#             # Plot scatter plot for UT1 vs UT2 marks
#             fig_scatter = px.scatter(df, x='UT1', y='UT2', hover_name='Student Name', labels={'x': 'UT1', 'y': 'UT2'}, title='UT1 vs UT2 Marks')
#             st.plotly_chart(fig_scatter)
            
#         except Exception as e:
#             st.error(f"An error occurred while visualizing student marks data from file {selected_excel_file}: {e}")



import plotly.graph_objs as go

# # def plot_line_chart(df):
#     fig = go.Figure()
#     for index, row in df.iterrows():
#         fig.add_trace(go.Line(x=['UT1', 'UT2', 'UT AVG'], y=row[['UT1', 'UT2', 'UT AVG']], name=row['Student Name']))
#     fig.update_layout(title='Student Marks Trends', xaxis_title='Unit Tests', yaxis_title='Marks')
#     st.plotly_chart(fig)

def plot_bar_chart(df):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['Student Name'], y=df['UT1'], name='UT1'))
    fig.add_trace(go.Bar(x=df['Student Name'], y=df['UT2'], name='UT2'))
    fig.add_trace(go.Bar(x=df['Student Name'], y=df['UT AVG'], name='UT AVG'))
    fig.update_layout(barmode='group', title='Student Marks in UT1, UT2, and UT AVG', xaxis_title='Student Name', yaxis_title='Marks')
    st.plotly_chart(fig)
def plot_student_marks(directory):
    """
    Plot student marks from an Excel file using either a bar plot or a line plot
    """
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter only Excel files
    excel_files = [file for file in files if file.endswith('.xlsx') or file.endswith('.xls')]
    
    # Create a dropdown menu to select Excel files
    selected_excel_file = st.selectbox("SELECT COURSE", excel_files, key="plot_student_marks")

    if selected_excel_file:
        file_path = os.path.join(directory, selected_excel_file)
        
        try:
            with st.expander("UT Marks"):
                # Read the data from the Excel file
                df = pd.read_excel(file_path, sheet_name="UTMarks")
                
                # Plots subheader
                st.subheader("Student Marks Visualization")
                st.write("---")
                # Option to choose between bar plot or line plot
                left, right = st.columns(2, gap="large")
                with left:
                    plot_bar_chart(df)
                with right:
                    st.write(df)  # Display table of the dataframe instead of line chart
                
        except Exception as e:
            st.error(f"An error occurred while plotting student marks data from file {selected_excel_file}: {e}")



# def plot_student_marks1(directory):
#     """
#     Plot student marks from an Excel file using a box plot
#     """
#     # List all files in the directory
#     files = os.listdir(directory)
    
#     # Filter only Excel files
#     excel_files = [file for file in files if file.endswith('.xlsx') or file.endswith('.xls')]
    
#     # Create a dropdown menu to select Excel files
#     selected_excel_file = st.selectbox("Select Excel file", excel_files, key="plot_student_marks")

#     if selected_excel_file:
#         file_path = os.path.join(directory, selected_excel_file)
        
#         try:
#             # Read the data from the Excel file
#             df = pd.read_excel(file_path, sheet_name="UTMarks")
            
#             # Plots subheader
#             st.subheader("Student Marks Visualization")
            
#             # Plot the box plot for student marks
#             plot_student_marks_boxplot(df)
                
#         except Exception as e:
#             st.error(f"An error occurred while plotting student marks data from file {selected_excel_file}: {e}")
# def plot_student_marks_boxplot(df):
#     """
#     Plot student marks using a box plot
#     """
#     # Check if the DataFrame contains the expected columns
#     expected_columns = ['Roll_no', 'Student_Name', 'UT1', 'UT2', 'UT_AVG']
#     if not all(col in df.columns for col in expected_columns):
#         st.error("Expected columns not found in DataFrame.")
#         return
    
#     # Rename columns if needed
#     df.rename(columns={'UT AVG': 'UT_AVG'}, inplace=True)
    
#     # Melt the DataFrame to have a tidy format for Plotly Express
#     melted_df = df.melt(id_vars=['Roll_no', 'Student_Name'], var_name='Unit_Test', value_name='Marks')
    
#     # Plot the box plot
#     fig = px.box(melted_df, x='Unit_Test', y='Marks', color='Unit_Test', points="all", hover_data=['Student_Name'])
#     fig.update_layout(title='Box Plot of Student Marks for Each Unit Test', xaxis_title='Unit Test', yaxis_title='Marks')
#     st.plotly_chart(fig)










def formspage():
    directory = "courses_inputs"


    st.header("📊 Visulaize Data")
    st.write(":gray[HERE YOU CAN VIEW ANY COURSE'S DATA VISUALIZATION]")
    st.write("---")

    st.subheader(''':blue[Visualize] Course File as plots / charts / graphs''')
    st.write("---")
    plot_excel_sheet_attainment(directory)
    st.write("---")
    # plot_student_marks(directory)
    # st.write("---")

formspage()