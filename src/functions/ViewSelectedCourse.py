def view_selected_course(student,courses):
    print(
        "-----------------------------------------------------------------------------------------course info---------------------------------------------------------------------------------------\n",
        "Id                                                  Name                                                                          Teacher                                                          Department                                                  Time             ")
    tqlk = "{: ^10}\t{: ^50}\t{: ^40}\t{: ^40}\t{: ^40}"
    for selected_course_id in student[0]["selected"]:
        for course in courses:
            if selected_course_id == course["id"]:
                print(tqlk.format(course["id"],course["name"],course["teacher"],course["department"],course["time"]))
    return



