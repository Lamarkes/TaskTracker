import argparse
from todo import config_tasks


def main():
    parser = argparse.ArgumentParser(prog="todo")
    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser("add")
    add.add_argument("title")
    add.add_argument("description")


    subparsers.add_parser("list")


    done = subparsers.add_parser("done")
    done.add_argument("id")

    delete = subparsers.add_parser("del")
    delete.add_argument("id")

    args = parser.parse_args()

    if args.command == "add":
        config_tasks.add_tasks(args.title, args.description)

    elif args.command == "done":
        config_tasks.mark_a_task_as_done(args.id)
