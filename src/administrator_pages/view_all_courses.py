import streamlit as st
import json
import os

base = os.path.dirname(os.path.abspath(__file__))
courses_data_path = os.path.join(base, "../data/courses.jsonl")

with open(courses_data_path, "r") as f:
    data = [json.loads(line) for line in f]

edited_info = st.data_editor(data)

if st.button("Save Change"):
    with open(courses_data_path, "w") as f:
        for line in edited_info:
            f.write(json.dumps(line) + "\n")
    st.success("Saved successfully!")