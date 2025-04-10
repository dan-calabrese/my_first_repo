from bank_account import BankAccount

account1 = BankAccount("1234",1000)
print(account1)
account1.deposit(1000)
print(account1)

account2 = BankAccount("369",2500)
print(account2)
account2.withdraw(500)
print(account2)

balance = account2.get_balance()
print(balance)

