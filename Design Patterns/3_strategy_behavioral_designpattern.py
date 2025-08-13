'''
Real-World Scenario
Scenario: You’re building a payment system that can support different payment methods like credit card, PayPal,
and cryptocurrency. Instead of hardcoding payment logic or using big conditionals, you use the strategy pattern to
encapsulate the behavior of each payment method.
'''

from abc import ABC , abstractmethod

#Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
#Concrete strategies
#Concrete strategy 1
class CreditCardPayment(PaymentStrategy):
    def __init__(self,card_number):
        self.credit_number = card_number
    
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card ending in {self.card_number[-4:]}")
        
#Concerete strategy2
class PayPalPayment(PaymentStrategy):
    def __init__(self,email):
        self.email = email
    def pay(self,amount):
        print(f"Paid ${amount} using PayPal account {self.email}")

#Concrete strategy 3
class CryptoPayment(PaymentStrategy):
    def __init__(self,wallet_address):
        self.wallet_address = wallet_address
    def pay(self,amount):
        print(f"Paid ${amount} using Crypto wallet {self.wallet_address[:6]}...")
        
#Context class
class ShoppingCart:
    def __init__(self,payment_strategy:PaymentStrategy):
        self.payment_strategy = payment_strategy
        self.items = []
        
    def add_item(self, item,price):
        self.items.append((item,price))
    
    def checkout(self):
        total = sum(price for _, price in self.items)
        print(f"Total: ${total}")
        self.payment_strategy.pay(total)

#Usge Client
cart = ShoppingCart(CreditCardPayment("1234-5678-9012-3456"))
cart.add_item("Book", 29.99)
cart.add_item("Pen", 3.50)
cart.checkout()
 
# Change strategy at runtime
cart.payment_strategy = PayPalPayment("user@example.com")
cart.checkout()
