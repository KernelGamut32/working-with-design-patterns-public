from abstractions.notifier import Notifier


class EmailNotifier(Notifier):
    """
    Concrete implementation of INotifier for sending emails.
    """
    def send(self, recipient: str, subject: str, body: str) -> None:
        print(f"[EmailNotifier] Sending email to {recipient} | Subject: '{subject}' | Body: '{body}'")
