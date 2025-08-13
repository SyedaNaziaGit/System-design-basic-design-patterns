'''
Let’s take an example of a Remote Control for different types of Devices (e.g., TV, Radio). 
We want to be able to change the device (TV or Radio) without changing the remote control interface. 
The Bridge pattern helps us achieve this by separating the remote control abstraction from the device implementation.
'''

# Implementor - defines the device interface
class Device:
    def power_on(self):
        pass
    def power_off(self):
        pass
    def volume_on(self):
        pass
    def volume_off(self):
        pass
# Concrete Implementors - implementing the device interface for TV and Radio
class TV(Device):
    def power_on(self):
        print("TV is On")
    def power_off(self):
        print("TV is Off")
    def volume_up(self):
        print("TV Volume Up")
    def volume_down(self):
        print("TV Volume Down")

class Radio(Device):
    def power_on(self):
        print("Radio is On")
    def power_off(self):
        print("Radio is Off")
    def volume_up(self):
        print("Radio Volume Up")
    def volume_down(self):
        print("Radio Volume Down")

# Abstraction - defines the remote control interface
class RemoteControl:
    def __init__(self,device:Device):
        self.device = device
    def power(self):
        raise NotImplementedError
    def volume_up(self):
        raise NotImplementedError
    def volume_down(self):
        raise NotImplementedError

# Refined Abstraction - TVRemoteControl and RadioRemoteControl are specialized remote controls
class TVRemoteControl(RemoteControl):
    def power(self):
        self.device.power_on()
    def volume_up(self):
        self.device.volume_up()
    def volume_down(self):
        self.device.volume_down()

class RadioRemoteControl(RemoteControl):
    def power(self):
        self.device.power_on()
    def volume_up(self):
        self.device.volume_up()
    def volume_down(self):
        self.device.volume_down()
# Client Code
tv = TV()
radio = Radio()
tv_remote = TVRemoteControl(tv)
radio_remote = RadioRemoteControl(radio)

# Using the TV remote control
tv_remote.power()  # TV is On
tv_remote.volume_up()  # TV Volume Up

# Using the Radio remote control
radio_remote.power()  # Radio is On
radio_remote.volume_up()  # Radio Volume Up

'''
Output:
TV is On
TV Volume Up
Radio is On
Radio Volume Up
'''