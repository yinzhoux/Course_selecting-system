import streamlit as st
import json
import os

base = os.path.dirname(os.path.abspath(__file__))
courses_data_path = os.path.join(base, "../data/courses.jsonl")

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
courses = load_data(courses_data_path)

st.write("Please enter the course info here.")

ID = st.text_input("Enter course ID")
name = st.text_input("Enter course name")
teacher = st.text_input("Enter course teacher")
department = st.text_input("Enter course department")

st.write("Select the course time")
day = st.selectbox("", ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
start_time, end_time = st.select_slider("",
                                        options=["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00",
                                                 "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00"],
                                        value=("08:00", "22:00"))
course_info = {"id": ID, "name": name, "teacher": teacher, "department": department, "day": day,
               "start_time": start_time, "end_time": end_time}
if st.button("Add course"):
    flag = 1
    for key, value in course_info.items():
        if value == "":
            st.warning("Please enter course info totally!")
            flag = 0
            break

    for course in courses:
        if course["id"] == ID:
            st.warning("Course already exists!")
            flag = 0
            break

    if flag:
        new_course = {"id": ID, "name": name, "teacher": teacher, "department": department,
                      "time": f"{day} {start_time}-{end_time}"}
        courses.append(new_course)
        save_data(courses_data_path, courses)
        st.success("Course added successfully!")