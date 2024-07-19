import json


def save_data(filepath, data):
    with open(filepath, "w") as f:
        for line in data:
            f.write(json.dumps(line) + "\n")
