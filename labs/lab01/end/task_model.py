# task_model.py
from dataclasses import dataclass

@dataclass
class Task:
    """Simple model representing a single task."""
    id: int
    description: str
