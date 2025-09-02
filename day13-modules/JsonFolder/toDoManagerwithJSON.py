# To Do Manager with JSON


# Data structure
todos = [
    {"id": 1, "task": "Learn JSON", "done": False},
    {"id": 2, "task": "Build project", "done": False}
]


# save tasks to the json file
def save_todos(todos, filename="todos.json"):
    with open(filename, "w") as f:
        json.dump(todos, f, indent=4)
