#!/usr/bin/python3
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # متغير خاص (Private)

    # 1. Getter: دالة لقراءة الرصيد
    @property
    def balance(self):
        return self.__balance

    # 2. Setter: دالة لتعديل الرصيد (نضع شروطنا هنا)
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Error: Cannot deposit a negative amount!")
        else:
            self.__balance = amount
            print("Deposit successful!")

my_account = BankAccount("Ahmed", 5000)

print(my_account.balance)
my_account.balance = -100
my_account.balance = 6000
