import json

def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


print(load_data("../functions/data/courses.jsonl"))