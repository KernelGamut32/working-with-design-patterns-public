import json
import os
import sys

class TaskManager:
    """Manages tasks: data storage, persistence, and user interaction—ALL in one class."""
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self._load_tasks()

    def _load_tasks(self):
        """Load tasks from a JSON file on disk."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    self.tasks = json.load(f)
            except (IOError, json.JSONDecodeError):
                print("Warning: Could not load tasks file. Starting with empty list.")
                self.tasks = []
        else:
            self.tasks = []

    def _save_tasks(self):
        """Save current tasks to the JSON file."""
        try:
            with open(self.filename, "w") as f:
                json.dump(self.tasks, f, indent=4)
        except IOError:
            print("Error: Unable to write tasks to file.")

    def add_task(self, description):
        """Add a task to the in‐memory list."""
        if not description.strip():
            raise ValueError("Description cannot be empty.")
        new_id = (max((task["id"] for task in self.tasks), default=0) + 1)
        self.tasks.append({"id": new_id, "description": description})
        self._save_tasks()

    def remove_task(self, task_id):
        """Remove a task (by ID) from the in‐memory list."""
        before_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        if len(self.tasks) == before_count:
            raise KeyError(f"No task found with id {task_id}")
        self._save_tasks()

    def list_tasks(self):
        """Return a copy of the current task list."""
        return list(self.tasks)

    def run_cli(self):
        """Simple CLI loop for interacting with tasks."""
        print("Welcome to TaskManager!")
        while True:
            print("\nSelect an option:")
            print(" 1. List tasks")
            print(" 2. Add a task")
            print(" 3. Remove a task")
            print(" 4. Quit")
            choice = input("Enter choice [1-4]: ").strip()

            if choice == "1":
                tasks = self.list_tasks()
                if not tasks:
                    print("No tasks found.")
                else:
                    for t in tasks:
                        print(f"  [{t['id']}] {t['description']}")
            elif choice == "2":
                desc = input("Enter task description: ").strip()
                try:
                    self.add_task(desc)
                    print("Task added.")
                except ValueError as e:
                    print(f"Error: {e}")
            elif choice == "3":
                try:
                    tid = int(input("Enter ID of task to remove: ").strip())
                    self.remove_task(tid)
                    print("Task removed.")
                except (ValueError, KeyError) as e:
                    print(f"Error: {e}")
            elif choice == "4":
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice—please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    tm = TaskManager()
    tm.run_cli()
