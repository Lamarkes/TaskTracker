import json
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

FILE = BASE_DIR /"files"/ "tasks.json"

if not FILE.exists():
    FILE.parent.mkdir(parents=True, exist_ok=True)
    FILE.write_text('{"tasks": []}', encoding="utf-8")



def generate_id(data):
    if not data["tasks"]:
        return 1

    return max(task["id"] for task in data["tasks"]) + 1


def load_tasks():

    with open(FILE, 'r', encoding="utf-8") as file:
        return json.load(file)


def save_tasks(data):
    with open(FILE, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def add_tasks(title, description):

    data = load_tasks()

    task = {'id': generate_id(data),
        'title_task': title,
        'description': description,
        'status': 'TODO',
        'createdAt': str(date.today()),
        'updatedAt': None}
    data["tasks"].append(task)
    save_tasks(data)

    print('Task added!')


def update_a_task(id_task, new_title):

    data = load_tasks()

    for task in data['tasks']:
        if id_task == task['id']:
            task['title_task'] = new_title
            task['updatedAt'] = str(date.today())
            print('The task has been updated!')

    save_tasks(data)

def mark_a_task_as_done(id_task):

    data = load_tasks()

    for task in data['tasks']:
        if task['id'] == id_task:
            task['status'] = 'DONE'
            task['updatedAt'] = str(date.today())
            print("Task complete: ", task["title_task"])

    save_tasks(data)

def mark_a_task_as_progress(id_task):
    data = load_tasks()

    for task in data['tasks']:
        if task['id'] == id_task:
            task['status'] = 'PROGRESS'
            task['updatedAt'] = str(date.today())
            print('Your task is in Progress.', task["title_task"])

    save_tasks(data)


def list_all_tasks():
    data = load_tasks()

    for task in data['tasks']:
        print('-' * 8)
        print('Task: ', task['title_task'])
        print('Description: ', task['description'])
        print('Status: ', task['status'])
        print('Created At: ', task['createdAt'])

def delete_task(task_id):
    data = load_tasks()


    for task in data['tasks']:
        if task['id'] == task_id:
            data['tasks'].remove(task)

    save_tasks(data)
