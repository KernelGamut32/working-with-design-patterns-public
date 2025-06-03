from abc import ABC, abstractmethod


class Document:
    def __init__(self, content: str):
        self.content = content

    def __repr__(self):
        return f"<Document content={self.content!r}>"
