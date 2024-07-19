import sys
import functions.ViewSelectedCourse
import functions.SelectCourse
import functions.SaveData
import functions.LoadData


def print_menu():
    print("\n选课系统菜单：")
    print("1. 选课")
    print("2. 查看已选课程")
    print("3. 退出")


def main(student_file, courses_file):
    students = functions.LoadData.load_data(student_file)
    courses = functions.LoadData.load_data(courses_file)

    while True:
        print_menu()
        choice = input("请选择一个操作（1-3）：")

        if choice == '1':
            functions.SelectCourse.select_course(students, courses)
        elif choice == '2':
            functions.ViewSelectedCourse.view_selected_course(students, courses)
        elif choice == '3':
            print("退出系统。")
            break
        else:
            print("无效的输入，请重新选择。")

    # 保存学生数据
    functions.SaveData.save_data(student_file, students)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <student_filepath> <courses_filepath>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
