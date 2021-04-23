'''
This program contains a class that can be used to make a credit card object with properties like: card_number, pin_number, balance, mobile
The class contains getter and setter functions for various properties of the class
'''


class atm(object):
    # creating the constructor
    def __init__(self, card_number, pin_number, balance, mobile):
        self.card_number = card_number
        self.pin_number = pin_number
        self.balance = balance
        self.mobile = mobile
# creating a function to withdraw cash from the card

    def CashWithdrawl(self):
        amount = int(input("Please enter the amount you want to withdraw: "))
        if(amount<=self.balance):
            self.balance = self.balance-amount
            print("Your new balance is: ", self.balance)
            print("_____________________________________")
        else:
            print("Insufficient funds")    
# creating a function to print the user's current balance

    def BalanceEnquiry(self):
        print("Your current balance is: ", self.balance)
        print("_____________________________________")
# creating a function to add cash to the card

    def AddCash(self):
        amount = int(input("Please enter the amount you want to add: "))
        self.balance = self.balance+amount
        print("Your new balance is: ", self.balance)
        print("_____________________________________")
# creating a function to change the user's pin

    def ChangePin(self):
        pin = int(input("Please enter the new pin: "))
        self.pin_number = pin
        print("The new pin is: ", self.pin_number)
        print("_____________________________________")
# creating a function to print the user's pin

    def getPin(self):
        print("The pin is: ", self.pin_number)
        print("_____________________________________")
# creating a function to print the user's mobile number

    def GetMobile(self):
        print("Your registered mobile number is: ", self.mobile)
        print("_____________________________________")
# creating a function to change the mobile number

    def changeMobile(self):
        number = int(input("Please enter the new mobile number to be registered: "))
        self.mobile = number
        print("Your registered mobile number is: ", self.mobile)
        print("_____________________________________")
# creating a function print the information about user's card

    def printInfo(self):
        print("Your card number is: ", self.card_number)
        print("Your pin is: ", self.pin_number)
        print("Your current balance is: ", self.balance)
        print("Your registered mobile number is: ", self.mobile)


# creating a new atm object
myCard = atm(123456, 800, 25000, 8822882267)
myCard.CashWithdrawl()
myCard.BalanceEnquiry()
myCard.AddCash()
myCard.ChangePin()
myCard.GetMobile()
myCard.changeMobile()
myCard.printInfo()
