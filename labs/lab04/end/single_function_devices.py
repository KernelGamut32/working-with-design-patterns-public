from functions import Printable, Scannable, Faxable, Emailable
from document import Document


class SophisticatedPrinter(Printable):
    """A printer that only supports printing."""
    def print_document(self, document: Document) -> None:
        print(f"[Printer] SophisticatedPrinter is printing: {document.content!r}")


class OfficeScanner(Scannable):
    """A scanner that only supports scanning."""
    def scan_document(self, document: Document) -> None:
        print(f"[Scanner] OfficeScanner is scanning: {document.content!r}")


class FaxMachine(Faxable):
    """A fax device that only supports faxing."""
    def fax_document(self, document: Document, fax_number: str) -> None:
        print(f"[Fax] FaxMachine is faxing '{document.content!r}' to {fax_number}")


class EmailServer(Emailable):
    """A service that only supports emailing documents."""
    def email_document(self, document: Document, email_address: str) -> None:
        print(f"[Email] EmailServer is emailing '{document.content!r}' to {email_address}")
