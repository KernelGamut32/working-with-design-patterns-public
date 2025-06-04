from abc import ABC, abstractmethod
from typing import Optional
from account import Account

class Command(ABC):
    """
    The 'Command' interface. Any banking operation will implement execute().
    """
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Return a human‐readable description of this command.
        """
        pass


class DepositCommand(Command):
    """
    Concrete Command to perform a deposit.
    """
    def __init__(self, account: Account, amount: float):
        self.account = account
        self.amount = amount

    def execute(self) -> None:
        self.account.deposit(self.amount)

    def __str__(self) -> str:
        return f"DepositCommand(account={self.account.owner}, amount=${self.amount:.2f})"


class WithdrawCommand(Command):
    """
    Concrete Command to perform a withdrawal.
    """
    def __init__(self, account: Account, amount: float):
        self.account = account
        self.amount = amount

    def execute(self) -> None:
        self.account.withdraw(self.amount)

    def __str__(self) -> str:
        return f"WithdrawCommand(account={self.account.owner}, amount=${self.amount:.2f})"


class TransferCommand(Command):
    """
    Concrete Command to perform a transfer between two accounts.
    """
    def __init__(self, source_account: Account, target_account: Account, amount: float):
        self.source_account = source_account
        self.target_account = target_account
        self.amount = amount

    def execute(self) -> None:
        self.source_account.transfer(self.target_account, self.amount)

    def __str__(self) -> str:
        return (f"TransferCommand(from={self.source_account.owner}, "
                f"to={self.target_account.owner}, amount=${self.amount:.2f})")


class BalanceInquiryCommand(Command):
    """
    Concrete Command to request and display the current account balance.
    Always handled at the Teller level (no approval thresholds).
    """
    def __init__(self, account: Account):
        self.account = account

    def execute(self) -> None:
        print(f"[{self.account.owner}] Current balance: ${self.account.balance:.2f}")

    def __str__(self) -> str:
        return f"BalanceInquiryCommand(account={self.account.owner})"
