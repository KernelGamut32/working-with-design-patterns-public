from abc import ABC, abstractmethod
from document import Document


class Printable(ABC):
    @abstractmethod
    def print_document(self, document: Document) -> None:
        """Print the given document."""
        pass


class Scannable(ABC):
    @abstractmethod
    def scan_document(self, document: Document) -> None:
        """Scan the given document."""
        pass


class Faxable(ABC):
    @abstractmethod
    def fax_document(self, document: Document, fax_number: str) -> None:
        """Fax the given document to fax_number."""
        pass


class Emailable(ABC):
    @abstractmethod
    def email_document(self, document: Document, email_address: str) -> None:
        """Email the given document to email_address."""
        pass
