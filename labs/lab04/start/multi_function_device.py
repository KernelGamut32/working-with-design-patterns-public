from abc import ABC, abstractmethod


class Document:
    def __init__(self, content: str):
        self.content = content

    def __repr__(self):
        return f"<Document content={self.content!r}>"


class MultiFunctionDevice(ABC):
    """
    A catch‐all “interface” that declares printing, scanning, faxing, emailing.
    Violates ISP because implementers are forced to define methods they might not need.
    """
    @abstractmethod
    def print_document(self, document: Document) -> None:
        """Print the given document."""
        pass

    @abstractmethod
    def scan_document(self, document: Document) -> None:
        """Scan the given document."""
        pass

    @abstractmethod
    def fax_document(self, document: Document, fax_number: str) -> None:
        """Fax the given document to fax_number."""
        pass

    @abstractmethod
    def email_document(self, document: Document, email_address: str) -> None:
        """Email the given document to email_address."""
        pass
