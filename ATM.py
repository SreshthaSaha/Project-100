class ATM:
    def __init__(self,card_number,pin_nmber):
        self.card_number = card_number
        self.pin_nmber = pin_nmber

    def CashWithdrawl(self):
        print("Cash has been withdrawed")
    def BalanceEnquiry(self):
        print("Your balance amount left is: ''")

test1 = ATM(123,456)
test1.CashWithdrawl()

test2 = ATM(789,109)
test2.BalanceEnquiry()