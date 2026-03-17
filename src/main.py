import config_tasks
import uuid
from datetime import date



tasks = {}


title = 'Task Tracker CLI'
rep = len(title)


print('-'*rep)
print(title)
print('-'*rep)
msg = ('''Hello! Welcome to Task Tracker CLI, select the option: \n
        1 - Add a task
        2 - Mark a task as DONE
        3 - Mark a task as PROGRESS
        4 - List all tasks
        5 - Update a task 
        6 - List all tasks that are done
        7 - List all tasks that are not done
        8 - List all tasks that are in progress
        9 - Delete a task
        0 - Exit
''')

option = -1

while option != 0:
    print(msg)

    option = int(input('Select the option: '))
    match option:
        case 1:
            task_name = input('Input the name of the task: ')
            description_task = input('Input the description of the task: ')
            tasks = {'id': str(uuid.uuid4()),'title_task': task_name, 'Description': description_task, 'status': 'TODO',
                                'createdAt': str(date.today()), 'updatedAt': None}

            config_tasks.add_tasks(tasks)

        case 2:
            config_tasks.mark_a_task_as_done("0c56940e-a620-4660-8970-7162baaec993")
