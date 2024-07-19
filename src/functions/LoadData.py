import json


def load_data(filepath):
    with open(filepath, "r",encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def load_students():
    with open("/home/joe/PycharmProjects/Course_selecting-system/src/data/student.json", "r",encoding="utf-8") as f:
        return [json.loads(line) for line in f]



def load_courses():
    with open("/home/joe/PycharmProjects/Course_selecting-system/src/data/courses.jsonl", "r",encoding="utf-8") as f:
        return [json.loads(line) for line in f]
