class Transaction:
 def __init__(self, transaction_id, account, transaction_type, amount):
  self.transaction_id = transaction_id
  self.account = account
  self.transaction_type = transaction_type
  self.amount = amount

from .transaction import Transaction

class TransactionProcessor:
 def process_transaction(transaction):
  if transaction.transaction_type == "deposit":
   transaction.account.deposit(transaction.amount)
  elif transaction.transaction_type == "withdraw":
   transaction.account.withdraw(transaction.amount)
  else:
   print("Invalid transaction type.")