'''
Python Example of Decorator Pattern
Let's say we have a basic text message class, and we want to add bold and italic features without changing 
the original class.
'''
#Base Component
class TextMessage:
    def render(self):
        return "Hello "
#Decorator
class BoldDecorator:
    def __init__(self,wrapped):
        self.wrapped = wrapped
    
    def render(self):
        return f"<b>{self.wrapped.render()}</b>"
    
class ItalicDecorator:
    def __init__(self,wrapped):
        self.wrapped = wrapped
    def render(self):
        return f"<i>{self.wrapped.render()}</i>"

#Usage
message = TextMessage()
print(message.render())  # Hello, World!

# Add bold
bold_message = BoldDecorator(message)
print(bold_message.render())  # <b>Hello, World!</b>
# Add italic over bold
fancy_message = ItalicDecorator(bold_message)
print(fancy_message.render())  # <i><b>Hello, World!</b></i>

    