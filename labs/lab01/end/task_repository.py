# task_repository.py
import json
import os
from typing import List

from task_model import Task

class TaskRepository:
    """
    Responsible solely for persisting and retrieving Task data to/from a JSON file.
    """
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def load_all(self) -> List[Task]:
        """Load tasks from a JSON file; return a list of Task objects."""
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, "r") as f:
                raw = json.load(f)
                return [Task(id=item["id"], description=item["description"]) for item in raw]
        except (IOError, json.JSONDecodeError):
            # On failure, return empty list (could also raise a custom exception)
            return []

    def save_all(self, tasks: List[Task]) -> None:
        """Serialize a list of Task objects to JSON and write to disk."""
        try:
            with open(self.filename, "w") as f:
                json.dump(
                    [{"id": t.id, "description": t.description} for t in tasks],
                    f,
                    indent=4
                )
        except IOError:
            raise IOError("Failed to save tasks to disk.")
