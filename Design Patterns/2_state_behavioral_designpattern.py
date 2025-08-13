'''
Example: Vending Machine
Let’s create a simple example of a Vending Machine that behaves differently based on the current state, 
such as when the machine is waiting for coins or when it’s dispensing a product.

'''
#State Interface : Defines methods that all states must be implemented
class VendingMachineState:
    def insert_coin(self, machine):
        pass
    
    def select_product(self,machine):
        pass
    
    def dispense_product(self, machine):
        pass
    
    
#Concrete State Definition:

#Concrete state 1: No coin inserted:
class NoCoinState(VendingMachineState):
    def insert_coin(self, machine):
        print("Coin inserted. You can now select a product.")
        machine.set_state(machine.has_coin_state)
    
    def select_product(self, machine):
        print("Please insert a coin first.")
    
    def dispense_product(self, machine):
        print("Please insert a coin first.")
        
#Concrete state 2 : coin inserted
class HasCoinState(VendingMachineState):
    def insert_coin(self, machine):
        print("Coin already inserted. Please select a product.")
    def select_product(self, machine):
        print("Product selected. Dispensing now.")
        machine.set_state(machine.sold_state)
    def dispense_product(self, machine):
        print("Please select a product first.")

#Concrete state 3 :  Product dispensed:
class SoldState(VendingMachineState):
    def insert_coin(self, machine):
        print("Please wait, product is being dispensed.")
    def select_product(self, machine):
        print("Please wait, product is being dispensed.")
    def dispense_product(self, machine):
        print("Product dispensed. Thank you for your purchase!")
        machine.set_state(machine.no_coin_state)
        
# Context class 
class VendingMachine:
    def __init__(self):
        self.no_coin_state = NoCoinState()
        self.has_coin_state =  HasCoinState()
        self.sold_state = SoldState()
        self.state = self.no_coin_state #initial state
    
    def set_state(self,state):
        self.state = state
        
    #methods to interact with vending machine
    def  insert_coin(self):
        self.state.insert_coin(self)
        
    def select_product(self):
        self.state.select_product(self)
        
    def dispense_product(self):
        self.state.dispense_product()
        
        
#Client Code
machine = VendingMachine()

#Scenario 1:  No coin inserted
machine.select_product()# Error, no coin inserted
machine.insert_coin()  # Coin inserted
machine.select_product()  # Product selected
machine.dispense_product()  # Dispensing product

# Scenario 2: Product dispensed, state reset
machine.insert_coin()  # Coin inserted
machine.select_product()  # Product selected
machine.dispense_product()  # Dispensing product
