'''
Let's say we have a RemoteControl that can turn on and off various devices (like a Light and a Fan). 
Using the Command pattern, we can encapsulate the "turn on" or "turn off" actions into command objects, and 
then execute them via the remote control.
'''

#Receiver  Classes [the objects that perform  the actual actions]

class  Light:
    def turn_on(self):
        print("The light is ON.")
    def turn_off(self):
        print("The light is OFF.")

class Fan:
    def turn_on(self):
        print("The fan is ON.")
    def turn_off(self):
        print("The fan is OFF.")
        
#Command Interface - abstract class  for all commands
class Command:
    def execute(self):
        pass

#Concrete Command class
class LightOnCommand(Command):
    def __init__(self,light):
        self.light = light
    def execute(self):
        self.light.turn_on()
        
class LightOffCommand(Command):
    def __init__(self,light):
        self.light = light
    def execute(self):
        self.light.turn_off()

class FanOnCommand(Command):
    def __init__(self,fan):
        self.fan = fan
    def execute(self):
        self.fan.turn_on()

class FanOffCommand(Command):
    def __init__(self,fan):
        self.fan = fan
    def execute(self):
        self.fan.turn_off()
        
#Invoker Class - The Remote Control
class RemoteControl:
    def __init__(self):
        self.command = None
    def set_command(self,command):
        self.command = command
    def press_button(self):
        if self.command:
            self.command.execute()
            
#Client Mode:
light = Light()
fan = Fan()

#Creating  Command Objects
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)
fan_on = FanOnCommand(fan)
fan_off = FanOffCommand(fan)

#Using Remote Control
remote = RemoteControl()

#Turning light on
remote.set_command(light_on)
remote.press_button()# Output: The light is ON.

#Turning  fan on
remote.set_command(fan_on)
remote.press_button()# Output: The fan is ON.

# Turning the light off
remote.set_command(light_off)
remote.press_button()  # Output: The light is OFF.
 
# Turning the fan off
remote.set_command(fan_off)
remote.press_button()  # Output: The fan is OFF.
