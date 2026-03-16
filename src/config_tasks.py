import json
from create_json_file import json_file_config


tasks = {'task_name':{}}

str_json = json.dumps(tasks, indent=4)

def add_tasks():
    json_file_config()
    try:
        with open('files/tasks.json', 'r', encoding="utf-8") as file:
           data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {'tasks': []}

    data["tasks"].append(tasks)

    with open('files/tasks.json', 'w', encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

