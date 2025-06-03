from functions import Printable, Scannable, Faxable, Emailable
from document import Document


class PrintWorkflow:
    """Routes only print jobs—depends only on Printable."""
    def __init__(self, printer: Printable):
        self.printer = printer

    def perform_print_job(self, doc: Document):
        self.printer.print_document(doc)


class ScanWorkflow:
    """Routes only scan jobs—depends only on Scannable."""
    def __init__(self, scanner: Scannable):
        self.scanner = scanner

    def perform_scan_job(self, doc: Document):
        self.scanner.scan_document(doc)


class FaxWorkflow:
    """Routes only fax jobs—depends only on Faxable."""
    def __init__(self, fax_device: Faxable):
        self.fax_device = fax_device

    def perform_fax_job(self, doc: Document, fax_number: str):
        self.fax_device.fax_document(doc, fax_number)


class EmailWorkflow:
    """Routes only email jobs—depends only on Emailable."""
    def __init__(self, email_service: Emailable):
        self.email_service = email_service

    def perform_email_job(self, doc: Document, email_address: str):
        self.email_service.email_document(doc, email_address)
