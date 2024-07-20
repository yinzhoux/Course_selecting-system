import json
import streamlit as st
import path
import sys


dir = path.Path(__file__).abspath()
sys.path.append(str(dir.parent.parent))

with open("data/online_student.json", "r") as f:
    online_student = json.load(f)["name"]

st.subheader(f"Selected courses of {online_student}")
with open("data/student.jsonl", "r") as f:
    for line in f:
        student_tmp = json.loads(line)
        if student_tmp["name"] == online_student:
            st.session_state.selected = student_tmp["selected"]
            break

selected_courses_info = []
with open("data/courses.jsonl", "r") as f:
    for line in f:
        courses_tmp = json.loads(line)
        for id_tmp in st.session_state.selected:
            if id_tmp == courses_tmp["id"]:
                selected_courses_info.append(courses_tmp)

st.dataframe(selected_courses_info)
