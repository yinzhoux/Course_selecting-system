import json
import streamlit as st
import os

base = os.path.dirname(os.path.abspath(__file__))
student_file = os.path.join(base, "../data/student.jsonl")
online_student_file = os.path.join(base, "../data/online_student.json")
course_data_file = os.path.join(base, "../data/courses.jsonl")


def time_conflict_judge(selected_course_time, to_select_course_time):
    t1 = selected_course_time
    t2 = to_select_course_time
    if not t1[:3] == t2[:3]:
        return False
    elif t1[4:6] > t2[10:12]:
        return False
    elif t1[10:12] < t2[4:6]:
        return False
    else:
        return True


with open(online_student_file, "r") as f:
    online_student = json.load(f)["name"]

st.subheader(f"Select courses for {online_student}")
with open(student_file, "r") as f:
    for line in f:
        student_tmp = json.loads(line)
        if student_tmp["name"] == online_student:
            st.session_state.selected_courses = student_tmp["selected"]
            break

selected_courses_info = []
all_courses = []
with open(course_data_file, "r") as f:
    for line in f:
        courses_tmp = json.loads(line)
        all_courses.append(courses_tmp)
        for id_tmp in st.session_state.selected_courses:
            if id_tmp == courses_tmp["id"]:
                selected_courses_info.append(courses_tmp)

st.dataframe(all_courses)

to_select = st.selectbox("Select a course", [course["id"] for course in all_courses])

if st.button("Select course"):
    if to_select in st.session_state.selected_courses:
        st.warning(f"Course already selected: {to_select}.")
    else:
        time_conflict_flag = False
        course_to_select = [course for course in all_courses if course["id"] == to_select]
        for course_selected_id in st.session_state.selected_courses:
            course_selected = [course for course in all_courses if course["id"] == course_selected_id]
            if time_conflict_judge(course_selected[0]["time"], course_to_select[0]["time"]):
                st.warning("Time conflicting!")
                time_conflict_flag = True
                break

        if not time_conflict_flag:
            st.success(f"Course selected successfully: {to_select}")
            with open(student_file, "r") as f:
                all_student = [json.loads(line) for line in f]
            for student in all_student:
                if student["name"] == online_student:
                    student["selected"].append(to_select)
                    break
            with open(student_file, "w") as f:
                for student in all_student:
                    f.write(json.dumps(student) + "\n")