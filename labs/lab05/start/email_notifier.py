class EmailNotifier:
    """
    Low-level notification class for sending emails.
    """
    def send_email(self, recipient: str, subject: str, body: str):
        # Imagine this actually sends an email via SMTP
        print(f"[EmailNotifier] Sending email to {recipient} | Subject: '{subject}' | Body: '{body}'")
