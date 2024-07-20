#In this We will learn about the basic concept  regarding oop i.e what are classes and what is object.
'''
Class: it is like a blueprint of a program means what actually the structure of a program is 
Object : it is nothng but the instance of a class
To get dive into it we will learn it with the real time application
'''

'''
Statement : We are going to generate a atm machine 
'''
class Atm:# The name of the class must be always in pascal case:
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()
    #whatever varibles we want to declare, we will declare them in the init method. Now the question comes in mind why i am calling it as an method why not function because whatever funxtion we will declare insisde the class it is called as a method. the __init__ it a constructor that means it will gete executed automatically whenever we create the object of class 

    def menu(self):
        user_input=int(input(""""
        Hello how would you like to proceed?
        1.Enter 1 to create pin
        2.Enter 2 to deposit
        3.Enter 3 to withdraw
        4.Enter 4 to check balance 
        5.Enter 5 to exit
        """))

        if(user_input==1):
            self.create_pin()
        elif(user_input==2):
            self.deposit()
        elif(user_input==3):
            self.withdraw()
        elif(user_input==4):
            self.check_balance()
        else:
            exit

        #let's create a metho to enter the pin
    def create_pin(self):
        self.pin= input("Enter the Pin")
        print("Pin set succefully")
        self.menu()
        
    
    #Let's make another method to deposit the amount
    def deposit(self):
        temp=(input("Enter the pin:"))
        if temp == self.pin:
            deposit=int(input("Enter the amount:"))
            self.balance=self.balance + deposit
            print("Amount Deposit successfully")
        else:
            print("Enter the wrong pin")
        self.menu()

    def withdraw(self):
        temp= (input("Enter the pin:"))
        
        if(temp==self.pin):
            withdraw= int(input("Enter the amount to be withdraw:"))
            if(withdraw < self.balance):
                self.balance=self.balance-withdraw
                print("Withdraw Successfully")
            else:
                print("Amount is greater than the bank balance")
        else:
            print("Balance is insufficient to withdraw")
        self.menu()
    
    def check_balance(self):
        temp= (input("Enter the Pin:"))
        if(temp==self.pin):
            print("The Total balance is:",self.balance)
        else:
            print("Wrong password")
        self.menu()
            
sbi = Atm()#creating the object of class

