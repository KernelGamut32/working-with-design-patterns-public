from document import Document
from single_function_devices import SophisticatedPrinter, OfficeScanner, FaxMachine, EmailServer
from multi_function_device import MultiFunctionPrinter
from workflows import PrintWorkflow, ScanWorkflow, FaxWorkflow, EmailWorkflow


if __name__ == "__main__":
    doc = Document("Sales Figures")

    # 1) A pure printer:
    printer = SophisticatedPrinter()
    print_workflow = PrintWorkflow(printer)
    print_workflow.perform_print_job(doc)  # OK

    # 2) A multi‐function printer:
    mfp = MultiFunctionPrinter()
    fax_workflow = FaxWorkflow(mfp)
    fax_workflow.perform_fax_job(doc, "555-9876")  # OK
    scan_workflow = ScanWorkflow(mfp)
    scan_workflow.perform_scan_job(doc)            # OK
    # (No NotImplementedError anywhere)

    # 3) A simple fax-only machine:
    fax_machine = FaxMachine()
    fax_only_workflow = FaxWorkflow(fax_machine)
    fax_only_workflow.perform_fax_job(doc, "555-0000")  # OK

    # 4) Trying to use a scanner in a print workflow is now a type error at compile-time
    #    (or at least a design‐time mismatch), not a runtime stub.
    # scan_workflow_bad = ScanWorkflow(printer)  # <-- Linter/IDE can alert: printer is not Scannable.
