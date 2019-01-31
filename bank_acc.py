class BankAccount:
    def __init__(self, name, amount, add, withdraw):
        self.name = name
        self.amount = amount
        self.add = add
        self.withdraw = withdraw

customer1 = BankAccount("john", 200000000, 6000000, 700000)

print(customer1.name)
print(customer1.amount)
print(customer1.add)
print(customer1.withdraw)
