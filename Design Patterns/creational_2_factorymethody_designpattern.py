'''
Scenario: You’re building a notification system. Depending on the platform (Email, SMS, Push), you want to send a 
different kind of notification. Instead of using conditionals everywhere, use a Factory Method.
'''
from abc import ABC ,abstractmethod
## Step 1: Define a common interface
class Notification(ABC):
    @abstractmethod
    def notify(self):
        pass
#Step2 - create concrete  implementations
class EmailNotification(Notification):
    def notify(self,message):
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def notify(self,message):
        print(f"Sending SMS: {message}")

class PushNotification(Notification):
    def notify(self,message):
        print(f"Sending Push Notification: {message}")

#Step3 - Factory Method Creator
class NotifyFactory:
    @staticmethod
    def create_notification(channel):
        if channel == "email":
            return EmailNotification()
        elif channel == "sms":
            return SMSNotification()
        elif channel == "push":
            return PushNotification()
        else:
            raise ValueError("Invalid notification channel")
#step4 - use factory
channel = "email"
notifier = NotifyFactory.create_notification(channel)
notifier.notify("You have a new message!")