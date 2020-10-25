class Account():
    def __init__(self, account_holder, amount):
        self.__account_holder = input("Enter an account holder: \n")
        self.__amount = float(input("Enter an amount: \n"))
        
            
    @property
    def account_holder(self):
        return self.__account_holder
    

    @property
    def amount(self):
        return self.__amount
    

    @account_holder.setter
    def name(self, account_holder):
        self.__account_holder = account_holder
    

    @amount.setter
    def amount(self, amount):
        
        if amount < 0:
            print("I think, you are entering negative numbers.")
        else:
            self.__amount = amount
    

    def deposit(self, deposit):
        deposit = float(input("How much do you want to deposit? \n"))
        if deposit < 0:
            print(f"{deposit} is an incorrent amount. ")
        else:
            self.__amount += deposit
            print(f"You have deposited {deposit}")


    def withdraw(self, amount):
        withdraw = float(input("How much do you want to withdraw? \n"))
        if withdraw > self.__amount:
            print("You cannot withdraw that amount of money.")
        else:
            self.__amount -= amount
            print(f"You have withdrawn {withdraw} ")


class Executable(Account):
    print("\n")
    title = " New account information "
    print(title.center(40, "*"))

    print("\n")
    account = Account(Account.account_holder, Account.amount)

    print("\n")
    print(account.deposit(0))
    
    print("\n")
    print(account.withdraw(0))
    





    