from pathlib import Path

def json_file_config():
    file = Path('files/tasks.json')

    if not file.is_file():

        with open('files/tasks.json', 'w'):
            print('The tasks can be created!')
    else:
        print('Your tasks list already exists!')
