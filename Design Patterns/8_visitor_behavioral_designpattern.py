'''
Imagine we have an Animal hierarchy with different types of animals, and we want to perform different operations 
(like feeding or making sounds) on these animals. Using the Visitor Pattern, we can define new operations for 
the animals without modifying their classes.
'''

# Element classes
class Animal:
    def accept(self, visitor):
        pass

class Dog(Animal):
    def accept(self, visitor):
        visitor.visit_dog(self)

class Cat(Animal):
    def accept(self, visitor):
        visitor.visit_cat(self)

class Bird(Animal):
    def accept(self, visitor):
        visitor.visit_bird(self)

# Visitor class
class AnimalActionVisitor:
    def visit_dog(self, dog):
        print("Feeding the dog.")

    def visit_cat(self, cat):
        print("Feeding the cat.")

    def visit_bird(self, bird):
        print("Feeding the bird.")
    
    def visit_sound_dog(self, dog):
        print("The dog says: Woof!")

    def visit_sound_cat(self, cat):
        print("The cat says: Meow!")

    def visit_sound_bird(self, bird):
        print("The bird says: Chirp!")

# Client code
dog = Dog()
cat = Cat()
bird = Bird()

# Creating a visitor that performs actions (like feeding and making sounds)
action_visitor = AnimalActionVisitor()

# Feeding the animals
dog.accept(action_visitor)  # Feeding the dog.
cat.accept(action_visitor)  # Feeding the cat.
bird.accept(action_visitor)  # Feeding the bird.

# Making sounds
action_visitor.visit_sound_dog(dog)  # The dog says: Woof!
action_visitor.visit_sound_cat(cat)  # The cat says: Meow!
action_visitor.visit_sound_bird(bird)  # The bird says: Chirp!

'''
Output:
Feeding the dog.
Feeding the cat.
Feeding the bird.
The dog says: Woof!
The cat says: Meow!
The bird says: Chirp!
'''