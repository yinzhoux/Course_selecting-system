import json
import streamlit as st
import os

base = os.path.dirname(os.path.abspath(__file__))
student_file = os.path.join(base, "../data/student.jsonl")
online_student_file = os.path.join(base, "../data/online_student.json")
course_data_file = os.path.join(base, "../data/courses.jsonl")

with open(online_student_file, "r") as f:
    online_student = json.load(f)["name"]

st.subheader(f"Selected courses of {online_student}")
with open(student_file, "r") as f:
    for line in f:
        student_tmp = json.loads(line)
        if student_tmp["name"] == online_student:
            st.session_state.selected = student_tmp["selected"]
            break

selected_courses_info = []
with open(course_data_file, "r") as f:
    for line in f:
        courses_tmp = json.loads(line)
        for id_tmp in st.session_state.selected:
            if id_tmp == courses_tmp["id"]:
                selected_courses_info.append(courses_tmp)

st.dataframe(selected_courses_info)
