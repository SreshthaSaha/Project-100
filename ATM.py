class ATM:
    def __init__(self):
        card_number = input("Please enter your card number: ")
        pin_nmber = input("Enter your pin number: ")
        self.card_number = card_number
        self.pin_nmber = pin_nmber


    def CashWithdrawl(self):
        print("Cash has been withdrawed")
        print("Your card number is : " + self.card_number)
    def BalanceEnquiry(self):
        print("Your balance amount left is: 'xxx'")
        print("Your pin number is: " + self.pin_nmber)

test1 = ATM()
test1.CashWithdrawl()

test2 = ATM()
test2.BalanceEnquiry()
