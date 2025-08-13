'''
Let’s say we want to create a Pizza. A pizza can have multiple ingredients like sauce, cheese, toppings, etc.
We can use the Builder pattern to make the creation process more flexible.
'''
# Product: Pizza
class Pizza:
    def __init__(self,crust,sauce,cheese, toppings):
        self.crust =  crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings
    def __str__(self):
        return f"Pizza with {self.crust} crust, {self.sauce} sauce, {self.cheese} cheese, topped with {', '.join(self.toppings)}."

#Builder : Pizza builder
class PizzaBuilder:
    def __init__(self):
        self.crust = "Thin"
        self.sauce = "Tomato"
        self.cheese = "Mozilla"
        self.toppings = []
    def set_crust(self, crust):
        self.crust = crust
        return self  # Return self to allow method chaining
    def set_sauce(self, sauce):
        self.sauce = sauce
        return self
    def set_cheese(self, cheese):
        self.cheese = cheese
        return self
    def add_topping(self, topping):
        self.toppings.append(topping)
        return self
    def build(self):
        return Pizza(self.crust, self.sauce, self.cheese, self.toppings)
# Director: PizzaDirector
class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder
    def make_vegetarian_pizza(self):
        return (self.builder.set_crust("Thick")
                .set_sauce("Pesto")
                .set_cheese("Cheddar")
                .add_topping("Olives")
                .add_topping("Mushrooms")
                .add_topping("Peppers")
                .build())
    def make_meat_pizza(self):
        return (self.builder.set_crust("Stuffed")
                .set_sauce("Tomato")
                .set_cheese("Mozzarella")
                .add_topping("Pepperoni")
                .add_topping("Sausage")
                .add_topping("Bacon")
                .build())
# Client code
builder = PizzaBuilder()
director = PizzaDirector(builder)
# Making a vegetarian pizza
veg_pizza = director.make_vegetarian_pizza()
print(veg_pizza)  # Output: Pizza with Thick crust, Pesto sauce, Cheddar cheese, topped with Olives, Mushrooms, Peppers.
# Making a meat pizza
meat_pizza = director.make_meat_pizza()
print(meat_pizza)  # Output: Pizza with Stuffed crust, Tomato sauce, Mozzarella cheese, topped with Pepperoni, Sausage, Bacon.


'''
Output:
Pizza with Thick crust, Pesto sauce, Cheddar cheese, topped with Olives, Mushrooms, Peppers.
Pizza with Stuffed crust, Tomato sauce, Mozzarella cheese, topped with Pepperoni, Sausage, Bacon.
'''