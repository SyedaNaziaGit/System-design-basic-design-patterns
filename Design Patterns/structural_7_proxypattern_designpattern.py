'''
Scenario: You have a huge image file. Instead of loading it right away, you create a proxy image that loads the 
real one only when needed (lazy loading). Great for memory-saving in UIs or games.
Python Example: Virtual Proxy (Lazy Loading)
'''
from abc import ABC ,abstractmethod
#Subject Interface
class Image(ABC):
    @abstractmethod
    def display(self):
        pass
#Real Object
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image_from_disk()
    def load_image_from_disk(self):
        print(f"Loading image from {self.filename}...")
    def display(self):
        print(f"Displaying {self.filename}")

#Proxy object
class ProxyImage(Image):
    def __init__(self,filename):
        self.filename = filename
        self.real_image = None
    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)# Lazy loading
        self.real_image.display()

#Client code
image = ProxyImage("cat.png")
print("First call to display:")
image.display()# Loads and displays
print("\nSecond call to display:")
image.display()  # Just displays (already loaded)

'''
Output:
First call to display:
Loading image from cat.png...
Displaying cat.png
Second call to display:
Displaying cat.png
'''