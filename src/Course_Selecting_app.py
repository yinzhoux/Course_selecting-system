import json

import streamlit as st

st.header("Course selection System")

if "role" not in st.session_state:
    st.session_state.role = "None"

ROLES = [None, "Student", "Administrator"]

with open("data/student.jsonl", "r") as f:
    students = [json.loads(line) for line in f]
    student_list = [student["name"] for student in students]


def login():
    st.header("Welcome to Course Selection System. Please log in first")
    role = st.selectbox("You are:", ROLES)

    if role == "Student":
        student_identity = st.selectbox("Identity:", student_list)
        online_student = {'name': student_identity}
        with open("data/online_student.json", "w") as f:
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
add_course = st.Page("./administrator_pages/add_course.py", title="Add Course")
add_student = st.Page("./administrator_pages/add_student.py", title="Add Student")
administrator_default_page = st.Page("./administrator_pages/default.py", title="Hello, Administrator!",
                                     default=(role == "Administrator"))
view_courses = st.Page("./administrator_pages/view_all_courses.py", title="Course List")
view_students = st.Page("./administrator_pages/view_all_students.py", title="Student List")

select_course = st.Page("./student_pages/Selecting_Course.py", title="Select Course")
view_selected_courses = st.Page("./student_pages/View_Selected_Courses.py", title="View Selected Courses")
student_default_page = st.Page("./student_pages/default.py", title="Hello, Student!", default=(role == "Student"))

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
