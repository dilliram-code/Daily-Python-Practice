# To Do Manager with JSON
import json

# Data structure
todos = [
    {"id": 1, "task": "Learn JSON", "done": False},
    {"id": 2, "task": "Build project", "done": False}
]


# save tasks to the json file
def save_todos(todos, filename="todos.json"):
    with open(filename, "w") as f:
        json.dump(todos, f, indent=4)


# Load tasks from JSON file
def load_todos(filename="todos.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []



# Add new to do
def add_task(task):
    todos = load_todos()
    new_id = len(todos) + 1
    todos.append({"id": new_id, "task": task, "done": False})
    save_todos(todos)
