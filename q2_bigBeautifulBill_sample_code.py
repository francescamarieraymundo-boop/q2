class Bill:
    def __init__(self, amount):
        self.amount = amount
        #methods for payment
    def pay(self, payment):
        self.amount -= payment.amount
        print("Payment made using", payment.mode)
        print("Remaining bill:", self.amount)

class Payment:
    mode = "Cash"
    def __init__(self, amount):
        self.amount = amount

class Ewallet(Payment):
    def __init__(self, name, amount):
        self.mode = name
        self.amount = amount
        
bigBeautifulBill = Bill(1000)
payment = Payment(900)
bigBeautifulBill.pay(payment)
gcash = Ewallet("Gcash", 100)
bigBeautifulBill.pay(gcash)
