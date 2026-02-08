class BankAccount:
    def __init__(self, account_number, starting_balance=0):
        self.account_number = account_number
        self.balance = starting_balance

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Rs.{amount} has been debited successfully")
            else:
                print("Error: Insufficient balance")
        else:
            print("The amount entered isn't valid")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs.{amount} has been credited successfully")
        else:
            print("Entered amount is incorrect")

    def check_balance(self):
        print(f"Your current balance is: Rs.{self.balance}")


# Creating an object
account = BankAccount(101, 6000)
account.check_balance()

