'''
Example: Arithmetic Expression Interpreter
Let’s use the Interpreter Pattern to evaluate simple arithmetic expressions like addition and subtraction.

'''

#Abstract expression
class Expression:
    def interpret(self):
        pass
# Terminal Expressions (representing numbers)
class Number(Expression):
    def __init__(self,number):
        self.number = number
    
    def interpret(self,context):
        return self.number
    
# Non-terminal Expressions (representing addition and subtraction)
class Add(Expression):
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def interpret(self,context):
        return self.left.interpret(context) + self.right.interpret(context)

class Subtraction(Expression):
    def __init__(self,left,right):
        self.left = left
        self.right = right
    def interpret(self,context):
        return self.left.interpret(context) - self.right.interpret(context)
    
#Client Code
def main():
    # Building an expression: (5 + 3) - 2
    five = Number(5)

    three = Number(3)
    two = Number(2)

    # Creating an addition expression (5 + 3)
    addition = Add(five, three)

    # Creating a subtraction expression: (5 + 3) - 2
    expression = Subtraction(addition, two)

    # Evaluating the expression
    result = expression.interpret(None)  # No context is needed for this simple example
    print(f"Result: {result}")  # Output should be 6: (5 + 3) - 2 = 6

if __name__ == "__main__":
    main()

    