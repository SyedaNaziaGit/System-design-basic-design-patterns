'''
Let’s create a simple example of a Cooking Process where the template method defines the general steps of
cooking, and the subclasses implement specific details.
'''
# Base class: Defines the template method and common steps
class Cooking:
    def cook(self):
        self.prepare_ingredients()
        self.cook_food()
        self.serve_food()
        
    # Steps that are the same for all cooking processes
    def prepare_ingredients(self):
        print("Preparing ingredients")
        
    def serve_food(self):
        print("Serving Food")
    
    # Abstract method to be implemented by subclasses
    def cook_food(self):
        pass

# Subclass 1: Implements a specific cooking process (e.g., making a soup)
class SoupCooking(Cooking):
    def cook_food(self):
        print("Cooking soup.")

# Subclass 2: Implements a specific cooking process (e.g., making a salad)
class SaladCooking(Cooking):
    def cook_food(self):
        print("Making a salad.")

# Client code
soup = SoupCooking()
soup.cook()
salad = SaladCooking()
salad.cook()
'''
Output:
Preparing ingredients.
Cooking soup.
Serving the food.

Preparing ingredients.
Making a salad.
Serving the food.

'''