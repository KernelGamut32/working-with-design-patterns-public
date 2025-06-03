from abstractions.notifier import Notifier


class SmsNotifier(Notifier):
    """
    Concrete implementation of INotifier for sending SMS messages.
    """
    def send(self, recipient: str, subject: str, body: str) -> None:
        print(f"[SmsNotifier] Sending SMS to {recipient} | Msg: '{subject} - {body}'")
