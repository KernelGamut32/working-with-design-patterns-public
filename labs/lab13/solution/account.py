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
        