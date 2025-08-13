'''
Let’s say we have a TextCharacter class, and we need to represent a large number of characters in a document. 
Many characters in the document might share common properties (e.g., the same font and size). 
Instead of creating separate instances for each character, we can use the Flyweight pattern to share common 
properties.
'''
class Character:
    def __init__(self,font,size):
        self.font = font
        self.size = size
    def __str__(self):
        return f"Character(font={self.font}, size={self.size})"
    
# Flyweight Factory: This class creates and manages shared characters.
class CharacterFactory:
    def __init__(self):
        self._fly_weights = {}
    def get_character(self,font,size):
        key = (font,size)
        if key not in self._fly_weights:
            self._fly_weights[key] = Character(font,size)
            print(f"Creating new character with font: {font} and size: {size}")
        return self._fly_weights[key]

#Client Code
factory = CharacterFactory()
# Using the Flyweight pattern to create characters
char1 = factory.get_character("Arial", 12)
char2 = factory.get_character("Arial", 12)
char3 = factory.get_character("Times New Roman", 14)
print(char1)  # Output: Character(font=Arial, size=12)
print(char2)  # Output: Character(font=Arial, size=12)
print(char3)  # Output: Character(font=Times New Roman, size=14)
# Checking if char1 and char2 share the same object
print(char1 is char2)  # Output: True (Both refer to the same object)
