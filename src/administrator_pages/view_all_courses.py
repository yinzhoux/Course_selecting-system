import streamlit as st
import json
import path
import sys


dir = path.Path(__file__).abspath()
sys.path.append(str(dir.parent.parent))
st.title("Course List")

with open("data/courses.jsonl", "r") as f:
    data = [json.loads(line) for line in f]

edited_info = st.data_editor(data)

if st.button("Save Change"):
    with open("data/courses.jsonl", "w") as f:
        for line in edited_info:
            f.write(json.dumps(line) + "\n")
    st.success("Saved successfully!")