from account import Account
from commands import DepositCommand, WithdrawCommand, TransferCommand, BalanceInquiryCommand
from handlers import TellerHandler, ManagerHandler, DirectorHandler, AssistantManagerHandler

def build_approval_chain() -> TellerHandler:
    """
    Construct and link the chain of responsibility:
      Teller -> Manager -> Director
    Returns the head of the chain (TellerHandler).
    """
    teller = TellerHandler()
    assistant = AssistantManagerHandler()  # Optional, if you want to include an assistant manager
    manager = ManagerHandler()
    director = DirectorHandler()

    teller.set_next(assistant).set_next(manager).set_next(director)
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

    cmd0 = BalanceInquiryCommand(alice_account)
    print(">> Issuing:", cmd0)
    approval_chain.handle(cmd0)

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
