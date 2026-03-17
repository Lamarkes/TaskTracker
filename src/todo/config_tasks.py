import json
import uuid
from datetime import date

FILE = "files/tasks.json"


def load_tasks():
    try:
        with open(FILE, 'r', encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'tasks': []}

def save_tasks(data):
    with open(FILE, 'w', encoding="utf-8") as file:
        json.dump(data, file,indent=4, ensure_ascii=False)

def add_tasks(title, description):

    data = load_tasks()
    task = {'id': str(uuid.uuid4()),
        'title_task': title,
        'Description': description,
        'status': 'TODO',
        'createdAt': str(date.today()),
        'updatedAt': None}
    data["tasks"].append(task)
    save_tasks(data)

    print('Task added!')


def mark_a_task_as_done(id_task):

    data = load_tasks()

    for task in data['tasks']:
        print(task['id'])
        if task['id'] == id_task:
            task['status'] = 'DONE'
            task['updatedAt'] = str(date.today())
            print("Task complete: ", task["title_task"])

    save_tasks(data)
    print('Task complete!')



    # TODO -> IMPLEMENTAR NOVAS FEATURES