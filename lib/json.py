import json


def save_to_json_file(filename, data):
    with open("../data/" + filename + ".json", 'w') as f:
        json.dump(data, f, indent=4)


def read_from_json_file(filename):
    with open("../data/" + filename + ".json", 'r') as f:
        data = json.load(f)
    return data
