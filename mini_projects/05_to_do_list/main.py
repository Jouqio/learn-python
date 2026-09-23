"""Mini Project 05: To-Do List"""
import json
import os

DATA_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, description):
    tasks.append({"description": description, "done": False})


def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True


def main():
    tasks = load_tasks()
    add_task(tasks, "Learn Python file handling")
    add_task(tasks, "Build a mini project")
    complete_task(tasks, 0)
    save_tasks(tasks)
    for i, task in enumerate(tasks):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{status} {i}: {task['description']}")


if __name__ == "__main__":
    main()
