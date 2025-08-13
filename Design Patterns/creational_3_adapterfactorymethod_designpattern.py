'''
Scenario: You’re designing a cross-platform GUI library. On Windows, buttons look different than on macOS. 
So, you want a system that can return a consistent UI kit depending on the OS.
'''
from abc import ABC, abstractmethod
# --- Abstract Products ---
class Button(ABC):
    @abstractmethod
    def render(self):
        pass
class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass
# --- Concrete Products for Windows ---
class WindowsButton(Button):
    def render(self):
        return "Windows-style Button"
class WindowsCheckbox(Checkbox):
    def render(self):
        return "Windows-style Checkbox"
# --- Concrete Products for Mac ---
class MacButton(Button):
    def render(self):
        return "Mac-style Button"
class MacCheckbox(Checkbox):
    def render(self):
        return "Mac-style Checkbox"
# --- Abstract Factory ---
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass
# --- Concrete Factories ---
class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()
    def create_checkbox(self):
        return WindowsCheckbox()
class MacFactory(UIFactory):
    def create_button(self):
        return MacButton()
    def create_checkbox(self):
        return MacCheckbox()
# --- Client Code ---
def create_ui(factory: UIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())
# Choose factory based on platform
platform = "mac"
if platform == "windows":
    factory = WindowsFactory()
else:
    factory = MacFactory()
create_ui(factory)
'''
🖥️ Output (if platform is "mac"):
Mac-style Button
Mac-style Checkbox
'''