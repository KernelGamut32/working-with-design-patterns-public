from abc import ABC, abstractmethod
from typing import Optional
from commands import Command, DepositCommand, WithdrawCommand, TransferCommand, BalanceInquiryCommand

class Handler(ABC):
    """
    Base class for Chain of Responsibility. Each handler can either handle
    a Command or pass it on to the next handler in the chain.
    """
    def __init__(self):
        self._next_handler: Optional["Handler"] = None

    def set_next(self, handler: "Handler") -> "Handler":
        """
        Link this handler to the next one and return the next handler. This allows building a fluent chain.
        """
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, command: Command) -> None:
        """
        Attempt to handle the given command. If this handler cannot process it,
        forward it to the next handler in the chain.
        """
        pass


class TellerHandler(Handler):
    """
    The Teller can process:
      - Deposits of any size
      - Withdrawals up to $500
      - Transfers up to $500
    Anything above $500 must be escalated to AssistantManagerHandler.
    """
    APPROVAL_LIMIT = 500.0

    def handle(self, command: Command) -> None:
        # Check type of command
        if isinstance(command, BalanceInquiryCommand):
            print(f"[Teller] Processing {command}")
            command.execute()
        elif isinstance(command, DepositCommand):
            print(f"[Teller] Processing {command}")
            command.execute()
        elif isinstance(command, WithdrawCommand):
            if command.amount <= self.APPROVAL_LIMIT:
                print(f"[Teller] Processing {command}")
                command.execute()
            else:
                print(f"[Teller] Cannot handle withdrawal of ${command.amount:.2f} — requires manager approval.")
                if self._next_handler:
                    self._next_handler.handle(command)
                else:
                    print("[Teller] No next handler available. Command rejected.")
        elif isinstance(command, TransferCommand):
            if command.amount <= self.APPROVAL_LIMIT:
                print(f"[Teller] Processing {command}")
                command.execute()
            else:
                print(f"[Teller] Cannot handle transfer of ${command.amount:.2f} — requires manager approval.")
                if self._next_handler:
                    self._next_handler.handle(command)
                else:
                    print("[Teller] No next handler available. Command rejected.")
        else:
            # Unrecognized command for this handler
            if self._next_handler:
                self._next_handler.handle(command)
            else:
                print(f"[Teller] Cannot handle command {command}. No next handler.")


class AssistantManagerHandler(Handler):
    APPROVAL_LIMIT = 2_500.0

    def handle(self, command: Command) -> None:
        if isinstance(command, WithdrawCommand):
            if TellerHandler.APPROVAL_LIMIT < command.amount <= self.APPROVAL_LIMIT:
                print(f"[Assistant Manager] Approving and processing {command}")
                command.execute()
            else:
                if self._next_handler:
                    print(f"[Assistant Manager] Cannot handle withdrawal of ${command.amount:.2f}—forwarding.")
                    self._next_handler.handle(command)
                else:
                    print("[Assistant Manager] No next handler. Command rejected.")

        elif isinstance(command, TransferCommand):
            if TellerHandler.APPROVAL_LIMIT < command.amount <= self.APPROVAL_LIMIT:
                print(f"[Assistant Manager] Approving and processing {command}")
                command.execute()
            else:
                if self._next_handler:
                    print(f"[Assistant Manager] Cannot handle transfer of ${command.amount:.2f}—forwarding.")
                    self._next_handler.handle(command)
                else:
                    print("[Assistant Manager] No next handler. Command rejected.")
        else:
            if self._next_handler:
                self._next_handler.handle(command)
            else:
                print(f"[Assistant Manager] Cannot handle command {command}. No next handler.")


class ManagerHandler(Handler):
    """
    The Manager can process:
      - Withdrawals from $2,500.01 up to $10,000
      - Transfers from $2,500.01 up to $10,000
    Otherwise, escalate to DirectorHandler.
    Deposits are always handled by Teller, so Manager does not explicitly handle deposits here.
    """
    APPROVAL_LIMIT = 10_000.0

    def handle(self, command: Command) -> None:
        if isinstance(command, WithdrawCommand):
            if self.APPROVAL_LIMIT >= command.amount > TellerHandler.APPROVAL_LIMIT:
                print(f"[Manager] Approving and processing {command}")
                command.execute()
            else:
                # Not in Manager’s range
                if self._next_handler:
                    print(f"[Manager] Cannot handle withdrawal of ${command.amount:.2f} — forwarding to next.")
                    self._next_handler.handle(command)
                else:
                    print("[Manager] No next handler. Command rejected.")
        elif isinstance(command, TransferCommand):
            if self.APPROVAL_LIMIT >= command.amount > TellerHandler.APPROVAL_LIMIT:
                print(f"[Manager] Approving and processing {command}")
                command.execute()
            else:
                if self._next_handler:
                    print(f"[Manager] Cannot handle transfer of ${command.amount:.2f} — forwarding to next.")
                    self._next_handler.handle(command)
                else:
                    print("[Manager] No next handler. Command rejected.")
        else:
            # Either a deposit or out‐of‐range: forward
            if self._next_handler:
                self._next_handler.handle(command)
            else:
                print(f"[Manager] Cannot handle command {command}. No next handler.")


class DirectorHandler(Handler):
    """
    The Director can process any Withdrawal or Transfer above $10,000.
    Deposits and smaller amounts have already been handled upstream.
    """
    def handle(self, command: Command) -> None:
        if isinstance(command, WithdrawCommand) or isinstance(command, TransferCommand):
            print(f"[Director] Approving and processing {command}")
            command.execute()
        else:
            print(f"[Director] Cannot handle command {command}. No next handler.")
            