from devices import OldFashionedPrinter
from multi_function_device import Document, MultiFunctionDevice


class OfficeWorkflow:
    """
    Routes tasks to a MultiFunctionDevice.  
    Because the interface includes methods not all devices support,
    the workflow must handle potential NotImplementedError in multiple places.
    """
    def __init__(self, device: MultiFunctionDevice):
        self.device = device

    def perform_print_job(self, doc: Document):
        try:
            self.device.print_document(doc)
        except NotImplementedError as e:
            print(f"[Workflow] ERROR: {e}")

    def perform_scan_job(self, doc: Document):
        try:
            self.device.scan_document(doc)
        except NotImplementedError as e:
            print(f"[Workflow] ERROR: {e}")

    def perform_fax_job(self, doc: Document, fax_number: str):
        try:
            self.device.fax_document(doc, fax_number)
        except NotImplementedError as e:
            print(f"[Workflow] ERROR: {e}")

    def perform_email_job(self, doc: Document, email_address: str):
        try:
            self.device.email_document(doc, email_address)
        except NotImplementedError as e:
            print(f"[Workflow] ERROR: {e}")

            
if __name__ == "__main__":
    doc = Document("Quarterly Report")

    printer = OldFashionedPrinter()
    workflow = OfficeWorkflow(printer)

    workflow.perform_print_job(doc)        # Works
    workflow.perform_scan_job(doc)         # Raises & catches NotImplementedError
    workflow.perform_fax_job(doc, "555-1234")
    workflow.perform_email_job(doc, "alice@example.com")
