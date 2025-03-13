from account_management.account import Account
from account_management.customer import Customer
from transaction_processing.transaction import Transaction
from transaction_processing.transaction_processor import TransactionProcessor

# Create customers
customer1 = Customer("C001", "Abhang Karode")
customer2 = Customer("C002", "Pooja Suravar")
# Create accounts
account1 = Account("A001", customer1)
account2 = Account("A002", customer2, balance=500.0)

# Display initial balances
print(f"{customer1.name}'s Balance: {account1.get_balance()}")
print(f"{customer2.name}'s Balance: {account2.get_balance()}")
# Perform transactions
transaction1 = Transaction("T001", account1, "deposit", 1000.0)
transaction2 = Transaction("T002", account2, "withdraw", 150.0)
TransactionProcessor.process_transaction(transaction1)
TransactionProcessor.process_transaction(transaction2)
# Display updated balances
print(f"{customer1.name}'s Updated Balance: {account1.get_balance()}")
print(f"{customer2.name}'s Updated Balance: {account2.get_balance()}")