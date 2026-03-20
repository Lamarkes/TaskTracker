import json
from itertools import count
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

FILE = BASE_DIR /"files"/ "tasks.json"

if not FILE.exists():
    FILE.parent.mkdir(parents=True, exist_ok=True)
    FILE.write_text('{"tasks": []}', encoding="utf-8")

counter = count()

def generate_id(data):

    return len(data["tasks"]) +1


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

    task = {'id': int(generate_id(data)),
        'title_task': title,
        'description': description,
        'status': 'TODO',
        'createdAt': str(date.today()),
        'updatedAt': None}
    data["tasks"].append(task)
    save_tasks(data)

    print('Task added!')


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