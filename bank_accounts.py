
class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, balance, amount):
        if amount > balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance


caren = BankAccount("Caren", "Segura", 123456, "Checking", 1234, 1000)

caren.deposit(96)
print(caren.balance)

caren.withdraw(caren.balance, 25)
print(caren.balance)


caren.get_balance()
print(caren.balance)
