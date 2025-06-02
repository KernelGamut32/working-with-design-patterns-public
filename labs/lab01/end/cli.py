# cli.py
import sys
from task_repository import TaskRepository
from task_service import TaskService
from task_model import Task

class CLI:
    """Handles all command‐line user interaction; calls into TaskService."""
    def __init__(self):
        repo = TaskRepository()          # Persistence layer
        self.service = TaskService(repo) # Business layer

    def run(self):
        print("Welcome to TaskManager (SRP‐Compliant Version)!")
        while True:
            self._print_menu()
            choice = input("Enter choice [1-4]: ").strip()

            if choice == "1":
                self._handle_list()
            elif choice == "2":
                self._handle_add()
            elif choice == "3":
                self._handle_remove()
            elif choice == "4":
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice—please select 1, 2, 3, or 4.")

    def _print_menu(self):
        print("\nSelect an option:")
        print(" 1. List tasks")
        print(" 2. Add a task")
        print(" 3. Remove a task")
        print(" 4. Quit")

    def _handle_list(self):
        tasks = self.service.list_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            for t in tasks:
                print(f"  [{t.id}] {t.description}")

    def _handle_add(self):
        desc = input("Enter task description: ").strip()
        try:
            new_task = self.service.add_task(desc)
            print(f"Task added: [{new_task.id}] {new_task.description}")
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_remove(self):
        tid_str = input("Enter ID of task to remove: ").strip()
        try:
            task_id = int(tid_str)
            self.service.remove_task(task_id)
            print("Task removed.")
        except ValueError:
            print("Error: ID must be an integer.")
        except KeyError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    CLI().run()
