'''
Python Example
Let’s create a simple example of a TextEditor where we can keep track of the changes to the text, and we want to
be able to undo (restore the previous state).
'''
# Memento class: Stores the state of the object
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


# Originator class: The object whose state we want to save and restore
class TextEditor:
    def __init__(self):
        self.text = ""

    def set_text(self, text):
        print(f"Text set to: {text}")
        self.text = text

    def get_text(self):
        return self.text

    def save_state(self):
        return Memento(self.text)

    def restore_state(self, memento):
        self.text = memento.get_state()
        print(f"Text restored to: {self.text}")


# Caretaker class: Manages the mementos (states)
class History:
    def __init__(self):
        self._history = []

    def add_memento(self, memento):
        self._history.append(memento)

    def get_memento(self, index):
        return self._history[index]


# Client code
editor = TextEditor()
history = History()

# Set some text
editor.set_text("Hello, World!")
history.add_memento(editor.save_state())

# Modify the text
editor.set_text("Hello, Design Patterns!")
history.add_memento(editor.save_state())

# Modify the text again
editor.set_text("Hello, Memento Pattern!")

# Restore to previous state
editor.restore_state(history.get_memento(1))

# Restore to the first saved state
editor.restore_state(history.get_memento(0))


'''
Output:
Text set to: Hello, World!
Text set to: Hello, Design Patterns!
Text set to: Hello, Memento Pattern!
Text restored to: Hello, Design Patterns!
Text restored to: Hello, World!
'''