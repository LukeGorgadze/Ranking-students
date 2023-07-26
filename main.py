import streamlit as st
import numpy as np

# CALCULATE FROBENIUS NORM
def fro(Matrix, rowNum, colNum):
    frobenius = 0
    for i in range(rowNum):
        for j in range(colNum):
            frobenius += abs(Matrix[i][j]) ** (2)
    frobenius **= (1. / 2)
    return frobenius

# Streamlit app header and description
st.title("Ranking students for fellowship applications")
st.subheader("Author: Luka Gorgadze")
st.write("This app generates random student matrices and calculates their Frobenius norms.")

# Streamlit parameters to adjust the matrix size and number of students
rowNum = st.slider("Number of Rows:", 1, 10, 4)
colNum = st.slider("Number of Columns:", 1, 10, 5)
num_students = st.slider("Number of Students:", 1, 100, 20)

# Function to generate student data
def generate_student_list(num_students, rowNum, colNum):
    studentList = {}
    for i in range(num_students):
        student = np.random.randint(50, size=(rowNum, colNum))
        studentList.update({i: (student, fro(student, rowNum, colNum))})
    return studentList

# Calculate student rankings
def rank_student(studentList):
    return dict(sorted(studentList.items(), key=lambda item: item[1][1]))

# Generate student data
studentList = generate_student_list(num_students, rowNum, colNum)

# Calculate student rankings
res = rank_student(studentList)

# Display the results
st.header("Student Rankings based on Frobenius Norm")
for key, value in res.items():
    st.subheader(f"Student ID: {key}")
    st.write("Matrix:")
    st.write(value[0])
    st.write("Frobenius Norm:", value[1])
    st.write("------------------")

