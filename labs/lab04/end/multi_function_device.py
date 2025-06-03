from functions import Printable, Scannable, Faxable, Emailable
from document import Document


class MultiFunctionPrinter(Printable, Scannable, Faxable):
    """
    Combines printing, scanning, and faxing.  
    Because it explicitly inherits only the needed smaller interfaces, 
    there’s no pollution from unsupported methods.
    """
    def print_document(self, document: Document) -> None:
        print(f"[MFP] Printing: {document.content!r}")

    def scan_document(self, document: Document) -> None:
        print(f"[MFP] Scanning: {document.content!r}")

    def fax_document(self, document: Document, fax_number: str) -> None:
        print(f"[MFP] Faxing '{document.content!r}' to {fax_number}")
