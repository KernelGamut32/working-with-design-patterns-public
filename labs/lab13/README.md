# Lab 13 - Chain of Responsibility & Command Patterns

## Overview

In this lab, you’ll explore how to combine two classic object-oriented design patterns—Command and Chain of Responsibility—to build a small “banking” application. Each banking operation (deposit, withdrawal, transfer) is encapsulated as a Command object. Approval and execution of these operations are handled by a chain of “handlers” (Teller → Manager → Director), each of which may execute or forward a request based on business rules.

---

## Learning Objectives

By the end of this lab, you should be able to:

1. Identify how the Command pattern decouples the invocation of an action from its implementation.
2. Explain how the Chain of Responsibility pattern can route requests through a series of handlers until one can process it.
3. Walk through and run the provided Python code, tracing how commands flow through the handler chain.
4. Modify approval thresholds in the handler classes and observe effects on execution.
5. Add a new command type or handler into the chain.
6. Reflect on real-world scenarios where these patterns simplify design and maintenance.

---

## Prerequisites

Before you begin, ensure the following:

1. Python 3.8+ installed - Confirm by running `python --version` in your terminal.
2. An editor or IDE capable of editing multiple `.py` files (e.g., VS Code, PyCharm, Sublime Text).
3. Familiarity with basic OOP in Python - You should know what classes, methods, and imports/modules are.
4. Basic comfort with the command line - You’ll navigate directories and launch Python scripts.

---

## File Structure

Create a new folder on your local machine (e.g., `bank_app/`) which will contain the following structure:

```text
bank_app/
├── account.py
├── commands.py
├── handlers.py
└── main.py
```

---

## Examine the Code

account.py

```python
class Account:
    """
    A simple bank account with deposit, withdraw, and transfer functionality.
    """
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Deposit a positive amount into the account.
        """
        if amount <= 0:
            raise ValueError(f"Deposit amount must be positive. Tried to deposit: {amount}")
        self.balance += amount
        print(f"[{self.owner}] Deposit: ${amount:.2f} (New balance: ${self.balance:.2f})")

    def withdraw(self, amount: float) -> None:
        """
        Withdraw a positive amount from the account, if sufficient funds exist.
        """
        if amount <= 0:
            raise ValueError(f"Withdrawal amount must be positive. Tried to withdraw: {amount}")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds for withdrawal. "
                             f"Requested: ${amount:.2f}, Available: ${self.balance:.2f}")
        self.balance -= amount
        print(f"[{self.owner}] Withdraw: ${amount:.2f} (New balance: ${self.balance:.2f})")

    def transfer(self, target_account: "Account", amount: float) -> None:
        """
        Transfer funds from this account to another account.
        """
        if amount <= 0:
            raise ValueError(f"Transfer amount must be positive. Tried to transfer: {amount}")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds for transfer. "
                             f"Requested: ${amount:.2f}, Available: ${self.balance:.2f}")
        self.balance -= amount
        target_account.balance += amount
        print(f"[{self.owner}] Transfer: ${amount:.2f} to [{target_account.owner}] "
              f"(Your new balance: ${self.balance:.2f}; {target_account.owner} new balance: "
              f"${target_account.balance:.2f})")
```

commands.py

```python
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
```

handlers.py

```python
from abc import ABC, abstractmethod
from typing import Optional
from commands import Command, DepositCommand, WithdrawCommand, TransferCommand

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
      - Withdrawals up to $1,000
      - Transfers up to $1,000
    Anything above $1,000 must be escalated to ManagerHandler.
    """
    APPROVAL_LIMIT = 1_000.0

    def handle(self, command: Command) -> None:
        # Check type of command
        if isinstance(command, DepositCommand):
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


class ManagerHandler(Handler):
    """
    The Manager can process:
      - Withdrawals from $1,000.01 up to $10,000
      - Transfers from $1,000.01 up to $10,000
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
```

main.py

```python
from account import Account
from commands import DepositCommand, WithdrawCommand, TransferCommand
from handlers import TellerHandler, ManagerHandler, DirectorHandler

def build_approval_chain() -> TellerHandler:
    """
    Construct and link the chain of responsibility:
      Teller -> Manager -> Director
    Returns the head of the chain (TellerHandler).
    """
    teller = TellerHandler()
    manager = ManagerHandler()
    director = DirectorHandler()

    teller.set_next(manager).set_next(director)
    return teller

def run_demo():
    """
    Demonstrates various commands flowing through the chain.
    """
    # Create a few accounts
    alice_account = Account("Alice", balance=40_000.00)
    bob_account   = Account("Bob", balance=10_000.00)

    # Build our chain: Teller -> Manager -> Director
    approval_chain = build_approval_chain()

    print("\n=== DEMO START ===\n")

    # 1) Deposit $2,000 into Alice’s account (Teller can handle deposits of any size)
    cmd1 = DepositCommand(alice_account, 2_000.00)
    print(">> Issuing:", cmd1)
    approval_chain.handle(cmd1)

    # 2) Withdraw $800 from Bob’s account (Teller can handle)
    cmd2 = WithdrawCommand(bob_account, 800.00)
    print("\n>> Issuing:", cmd2)
    approval_chain.handle(cmd2)

    # 3) Withdraw $5,000 from Bob’s account (Manager must approve)
    cmd3 = WithdrawCommand(bob_account, 5_000.00)
    print("\n>> Issuing:", cmd3)
    approval_chain.handle(cmd3)

    # 4) Transfer $12,000 from Alice to Bob (Director must approve)
    cmd4 = TransferCommand(alice_account, bob_account, 12_000.00)
    print("\n>> Issuing:", cmd4)
    approval_chain.handle(cmd4)

    # 5) Transfer $700 from Alice to Bob (Teller can handle small transfers)
    cmd5 = TransferCommand(alice_account, bob_account, 700.00)
    print("\n>> Issuing:", cmd5)
    approval_chain.handle(cmd5)

    # 6) Withdraw $20,000 from Alice’s account (Director must approve)
    cmd6 = WithdrawCommand(alice_account, 20_000.00)
    print("\n>> Issuing:", cmd6)
    approval_chain.handle(cmd6)

    print("\n=== DEMO END ===\n")

if __name__ == "__main__":
    run_demo()
```

To execute/test, run `python main.py`

---

## Additional Exercises (Time Permitting)

### Exercise 1: Add a New Handler Level (Assistant Manager)

Suppose in an effort to more efficiently process bank transactions, the bank introduces an "Assistant Manager" role which can approve/handle withdrawals/transfers between $500.01 and $2,500. Incorporate the new approval level into the application and adjust the limits to match up with the following flow:

- Teller can approve withdrawals and transfers up to $500.00
- Assistant Manager can approve withdrawals and transfers between $500.01 and $2,500.00, inclusive
- Manager approval is required for withdrawals and transfers between $2,500.01 and $10,000, inclusive
- Anything above $10,000 for withdrawals or transfers requires Director approval

Verify that the new approval flow is reflected in the set of existing transactions and/or incorporate new transactions to demonstrate and confirm.

### Exercise 2: Add a New Command Type

Scenario. The bank wants to log a “Balance Inquiry” request. This command simply prints the current balance in an account. Because it does not modify anything, any handler is allowed to service it (including Teller). You’ll create a new `BalanceInquiryCommand` class.
