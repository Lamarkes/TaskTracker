import argparse
from todo import config_tasks


def main():
    parser = argparse.ArgumentParser(prog="todo")
    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser("add")
    add.add_argument("title")
    add.add_argument("description")


    subparsers.add_parser("list")

    update = subparsers.add_parser("update")
    update.add_argument("id", type=int)
    update.add_argument("new_title")

    done = subparsers.add_parser("mark-done")
    done.add_argument("id", type=int)

    progress = subparsers.add_parser("mark-in-progress")
    progress.add_argument("id", type=int)

    delete = subparsers.add_parser("del")
    delete.add_argument("id", type=int)

    args = parser.parse_args()

    if args.command == "add":
        config_tasks.add_tasks(args.title, args.description)

    elif args.command == "mark-done":
        config_tasks.mark_a_task_as_done(args.id)

    elif args.command == "mark-in-progress":
        config_tasks.mark_a_task_as_progress(args.id)

    elif args.command == "list":
        config_tasks.list_all_tasks()

    elif args.command == "update":
        config_tasks.update_a_task(args.id, args.new_title)
