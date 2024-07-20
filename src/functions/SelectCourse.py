def list_all_courses(courses):
    print(
        "---------------------------------------------------------------------------------------------------------------course info---------------------------------------------------------------------------------------------------------------\n",
        "          Id                                                  Name                                                                       Teacher                                                          Department                                                  Time             ")
    tqlk = "{: ^10}\t{: ^50}\t{: ^40}\t{: ^40}\t{: ^40}"
    for course in courses:
        print(tqlk.format(course["id"], course["name"], course["teacher"], course["department"], course["time"]))
    return


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


def select_course(student, courses):
    list_all_courses(courses)
    print("Please enter the course id you want to selected:")
    course_id = input()
    if course_id in student[0]["selected"]:
        print("The course has been already selected")
        return
    for course in courses:
        if course["id"] == course_id:
            for selected_course_id in student[0]["selected"]:
                for course_selected in courses:
                    if course_selected["id"] == selected_course_id:
                        if time_conflict_judge(course_selected["time"], course["time"]):
                            print("Time conflicting!")
                            return
            print("Course selected successfully!")
            student[0]["selected"].append(course["id"])
            return
