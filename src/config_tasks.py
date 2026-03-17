import json
from create_json_file import json_file_config
from datetime import date


def add_tasks(tasks):
    json_file_config()
    try:
        with open('files/tasks.json', 'r', encoding="utf-8") as file:
           data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {'tasks': []}

    data["tasks"].append(tasks)

    with open('files/tasks.json', 'w', encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def mark_a_task_as_done(id_task):

    with open('files/tasks.json', 'r', encoding="utf-8") as file:
        data = json.load(file)

        for task in data['tasks']:
            print(task['id'])
            if task['id'] == id_task:
                task['status'] = 'DONE'
                task['updatedAt'] = str(date.today())
                print("Task complete: ", task["title_task"])

    with open('files/tasks.json', 'w', encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)