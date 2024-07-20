import streamlit as st
import json
import path
import sys


dir = path.Path(__file__).abspath()
sys.path.append(str(dir.parent.parent))
st.subheader('Add Student')


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def save_data(filepath, data):
    with open(filepath, "w") as f:
        for line in data:
            f.write(json.dumps(line) + "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# load courses data
student_data_path = "data/student.jsonl"
students = load_data(student_data_path)

st.write("Please enter the student info here.")

ID = st.text_input("Enter course ID")
name = st.text_input("Enter course name")

new_student = {"id": ID, "name": name, "selected": []}
if st.button("Add student"):
    flag = 1
    for key, value in new_student.items():
        if value == "":
            st.warning("Please enter student info totally!")
            flag = 0
            break

    for student in students:
        if student["id"] == ID:
            if student["name"] == name:
                st.warning("This student has already existed!")
                flag = 0
                break
            else:
                st.warning("Check the id!")
                flag = 0
                break
        elif student["name"] == name:
            st.warning("Check the name!")
            flag = 0
            break

    if flag:
        students.append(new_student)
        save_data(student_data_path, students)
        st.success("Student added successfully!")
