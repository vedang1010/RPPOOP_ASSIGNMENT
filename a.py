#  Define a class to represent a bank account. Include the following details like name of 
# the depositor, account number, type of account, balance amount in the account. Write 
# methods to assign initial values, to deposit an amount, withdraw an amount after 
# checking the balance, to display name, account number, account type and balance.
#  You have to write menu driven program for this problem statement
from random import randint
class bank_account:
    def __init__(self,name,num,acc_type):
        self.username=name
        self.account_num=num
        self.acc_type=acc_type
        self.__balance=self.initialBal()
    def initialBal(self):
        self.__balance=0
        return self.__balance
    def deposit(self):
        amount =int(input("Enter amount to be deposited:\n"))
        self.__balance=self.__balance+amount
        return self.__balance
    def withdraw(self):
        amt=int(input("Enter amount to be withdrawn:\n"))
        if self.__balance-amt>0:
            self.__balance=self.__balance-amt
            return self.__balance
        else:
            print("Insufficient Balance")
    def getBalance(self):
        return self.__balance
    def setName(self):
        self.username=input("Enter your name:\n")
    def getInfo(self):
        print("Account Holder:\t",self.username)
        print("Account Number:\t",self.account_num)
        print("Account Type:\t",self.acc_type)

# class child(bank_account):
#     def __init__(self,price):
#         self.p=price
#     def get(self):
#         return self.username
#     def getBal(self):
#         return self.__balance
print("\t\t\t\t\t--------------------------------------------------------\n\t\t\t\t\t|\tEnter 1 to  Create Bank Account\t\t\t|\n\t\t\t\t\t|\tEnter 2 to deposit\t\t\t\t|\n\t\t\t\t\t|\tEnter 3 to withdraw\t\t\t\t|\n\t\t\t\t\t|\tEnter 4 to checkBalance\t\t\t\t|\n\t\t\t\t\t|\tEnter 5 to get account info\t\t\t|\n\t\t\t\t\t|\tEnter 6 to change Account Holder Name\t\t|\n\t\t\t\t\t|\tEnter 7 to exit\t\t\t\t\t|\n\t\t\t\t\t--------------------------------------------------------")
choice=int(input())
while(choice!=7):
    if(choice==1):
        name = input("Enter your name:\n")
        num=randint(1000000000, 9999999999)
        type=int(input("Enter your account type:\n\t1 Savings Account\n\t2 Current\n\t3 FD\n"))
        if(type==1):
            account_type="Savings Account"
        if(type==2):
            account_type="Current Account"
        if(type==3):
            account_type="FD Account"
        b1=bank_account(name,num,account_type)
    if (choice==2):
        b1.deposit()
    if (choice==3):
        b1.withdraw()
    if(choice==4):
        print("Your account balance is : ",b1.getBalance())
    if(choice==5):
        b1.getInfo()
    if(choice==6):
        b1.setName()
    print("\t\t\t\t\t--------------------------------------------------------\n\t\t\t\t\t|\tEnter 1 to  Create Bank Account\t\t\t|\n\t\t\t\t\t|\tEnter 2 to deposit\t\t\t\t|\n\t\t\t\t\t|\tEnter 3 to withdraw\t\t\t\t|\n\t\t\t\t\t|\tEnter 4 to checkBalance\t\t\t\t|\n\t\t\t\t\t|\tEnter 5 to get account info\t\t\t|\n\t\t\t\t\t|\tEnter 6 to change Account Holder Name\t\t|\n\t\t\t\t\t|\tEnter 7 to exit\t\t\t\t\t|\n\t\t\t\t\t--------------------------------------------------------")
    choice=int(input())