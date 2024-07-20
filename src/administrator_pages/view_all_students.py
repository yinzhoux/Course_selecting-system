import streamlit as st
import json

st.title('Student List')
with open("data/student.jsonl", "r") as f:
    data = [json.loads(line) for line in f]

edited_info = st.data_editor(data)

if st.button("Save Change"):
    with open("data/student.jsonl", "w") as f:
        for student in edited_info:
            f.write(json.dumps(student) + "\n")
    st.success("Saved successfully!")