import streamlit as st
import json
import os

base = os.path.dirname(os.path.abspath(__file__))
student_data_path = os.path.join(base, "../data/student.jsonl")

st.title('Student List')
with open(student_data_path, "r") as f:
    data = [json.loads(line) for line in f]

edited_info = st.data_editor(data)

if st.button("Save Change"):
    with open(student_data_path, "w") as f:
        for student in edited_info:
            f.write(json.dumps(student) + "\n")
    st.success("Saved successfully!")