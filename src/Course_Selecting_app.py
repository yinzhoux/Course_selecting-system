import json
import streamlit as st

import os

base = os.path.dirname(os.path.abspath(__file__))
student_file = os.path.join(base, "data/student.jsonl")
online_student_file = os.path.join(base, "data/online_student.json")

#administrator
add_course_file = os.path.join(base, "administrator_pages/add_course.py")
add_student_file = os.path.join(base, "administrator_pages/add_student.py")
ad_default_file = os.path.join(base, "administrator_pages/default.py")
view_all_course_file = os.path.join(base, "administrator_pages/view_all_courses.py")
view_all_student_file = os.path.join(base, "administrator_pages/view_all_students.py")

#student
st_default_file = os.path.join(base, "student_pages/default.py")
selecting_course_file = os.path.join(base, "student_pages/Selecting_Course.py")
view_selected_course_file = os.path.join(base, "student_pages/View_Selected_Courses.py")

st.header("Course selection System")

if "role" not in st.session_state:
    st.session_state.role = "None"

ROLES = [None, "Student", "Administrator"]

with open(student_file, "r") as f:
    students = [json.loads(line) for line in f]
    student_list = [student["name"] for student in students]


def login():
    st.header("Welcome to Course Selection System. Please log in first")
    role = st.selectbox("You are:", ROLES)

    if role == "Student":
        student_identity = st.selectbox("Identity:", student_list)
        online_student = {'name': student_identity}
        with open(online_student_file, "w") as f:
            f.write(json.dumps(online_student))
    if role == "Administrator":
        st.session_state.password = st.text_input("Please enter password:")

    if st.button("Log in"):
        if (role == "Administrator" and st.session_state.password == "11111111") or role == "Student":
            st.session_state.role = role
            st.rerun()
        else:
            st.warning("Wrong password")


def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role

logout_page = st.Page(logout, title="Log out")
add_course = st.Page(add_course_file, title="Add Course")
add_student = st.Page(add_student_file, title="Add Student")
administrator_default_page = st.Page(ad_default_file, title="Hello, Administrator!",
                                     default=(role == "Administrator"))
view_courses = st.Page(view_all_course_file, title="Course List")
view_students = st.Page(view_all_student_file, title="Student List")

select_course = st.Page(selecting_course_file, title="Select Course")
view_selected_courses = st.Page(view_selected_course_file, title="View Selected Courses")
student_default_page = st.Page(st_default_file, title="Hello, Student!", default=(role == "Student"))

accout_pages = [logout_page]
student_pages = [select_course, view_selected_courses]
administrator_pages = [add_course, add_student, view_courses, view_students]

page_dict = {}
if st.session_state.role == "Administrator":
    page_dict["Hello"] = [administrator_default_page]
    page_dict["Operation"] = administrator_pages
if st.session_state.role == "Student":
    page_dict["Hello"] = [student_default_page]
    page_dict["Operation"] = student_pages

if len(page_dict) > 0:
    pg = st.navigation({"Accout": accout_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()
