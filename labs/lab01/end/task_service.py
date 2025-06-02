# task_service.py
from typing import List
from task_model import Task
from task_repository import TaskRepository

class TaskService:
    """
    Business‐logic layer: manages in‐memory Task objects.
    Does NOT deal with JSON, files, or user interaction.
    """
    def __init__(self, repo: TaskRepository):
        self.repo = repo
        # Load existing tasks into memory once at startup
        self._tasks: List[Task] = self.repo.load_all()

    def list_tasks(self) -> List[Task]:
        """Return a copy of all tasks."""
        return list(self._tasks)

    def add_task(self, description: str) -> Task:
        """
        Add a new Task to in‐memory list, assign a unique ID,
        then persist via repository.
        """
        desc = description.strip()
        if not desc:
            raise ValueError("Description cannot be empty.")

        max_id = max((t.id for t in self._tasks), default=0)
        new_task = Task(id=max_id + 1, description=desc)
        self._tasks.append(new_task)
        self.repo.save_all(self._tasks)
        return new_task

    def remove_task(self, task_id: int) -> None:
        """
        Remove the Task with the given ID from in‐memory list,
        then persist changes. Raises KeyError if ID not found.
        """
        original_len = len(self._tasks)
        self._tasks = [t for t in self._tasks if t.id != task_id]
        if len(self._tasks) == original_len:
            raise KeyError(f"No task found with id {task_id}")

        self.repo.save_all(self._tasks)
