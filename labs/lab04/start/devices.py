from multi_function_device import Document, MultiFunctionDevice


class OldFashionedPrinter(MultiFunctionDevice):
    """A printer that can only print; scanning/faxing/emailing aren’t supported."""
    def print_document(self, document: Document) -> None:
        print(f"[Printer] Printing document: {document.content!r}")

    def scan_document(self, document: Document) -> None:
        raise NotImplementedError("OldFashionedPrinter cannot scan.")

    def fax_document(self, document: Document, fax_number: str) -> None:
        raise NotImplementedError("OldFashionedPrinter cannot fax.")

    def email_document(self, document: Document, email_address: str) -> None:
        raise NotImplementedError("OldFashionedPrinter cannot email.")


class LegacyScanner(MultiFunctionDevice):
    """A scanner that can only scan; printing/faxing/emailing aren’t supported."""
    def print_document(self, document: Document) -> None:
        raise NotImplementedError("LegacyScanner cannot print.")

    def scan_document(self, document: Document) -> None:
        print(f"[Scanner] Scanning document: {document.content!r}")

    def fax_document(self, document: Document, fax_number: str) -> None:
        raise NotImplementedError("LegacyScanner cannot fax.")

    def email_document(self, document: Document, email_address: str) -> None:
        raise NotImplementedError("LegacyScanner cannot email.")


class BasicFaxMachine(MultiFunctionDevice):
    """A fax device that can only fax; printing/scanning/emailing aren’t supported."""
    def print_document(self, document: Document) -> None:
        raise NotImplementedError("BasicFaxMachine cannot print.")

    def scan_document(self, document: Document) -> None:
        raise NotImplementedError("BasicFaxMachine cannot scan.")

    def fax_document(self, document: Document, fax_number: str) -> None:
        print(f"[Fax] Faxing document {document.content!r} to {fax_number}")

    def email_document(self, document: Document, email_address: str) -> None:
        raise NotImplementedError("BasicFaxMachine cannot email.")
