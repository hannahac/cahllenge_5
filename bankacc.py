class BankAccount:
    def __init__(self, name):
        self.name = name
        self.is_open = False
        self.balance = 0

    def open(self):
        self.is_open = True

    def close_acc(self):
        self.is_open = False

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError("Account is closed")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError("Account is closed")
        
        if abs(amount) > self.balance:
            raise ValueError("Account balance is too low")

        self.balance -= abs(amount)
        return self.balance 

    def get_balance(self):
        if not self.is_open:
            raise ValueError("Account is closed")

        return self.balance        

if __name__ == "__main__":
    owner1 = BankAccount("Hannah")
    print(owner1.is_open)
    print(owner1.balance)

    owner1.open()
    print (owner1.is_open)
    owner1.balance = 2000
    print(owner1.balance)
    owner1.deposit(15000)
    print(owner1.balance)
    owner1.withdraw(500)
    print(owner1.balance)