'''
Let's consider an example where we have a ChatRoom acting as the Mediator. Users in the chat room (colleagues)
can send messages, but instead of directly interacting with each other, they send their messages to the ChatRoom 
mediator, which then forwards the messages to the appropriate participants.
'''

#Mediator Class - ClassRoom

class ChatRoom:
    def __init__(self):
        self.users = []
    def add_user(self,user):
        self.users.append(user)
    def send_message(self, sender,receiver, message):
        receiver.receive_message(sender,message)
    def broadcast_message(self,sender,message):
        for user in self.users:
            if user!= sender:
                user.receive_message(sender,message)

#Colleague Class - User
class  User:
    def __init__(self,name,chat_room):
        self.name = name
        self.chat_room = chat_room
        chat_room.add_user (self)
        
    def send_message(self,receiver,message):
        print(f"{self.name} sends message to {receiver.name}: {message}")
        self.chat_room.send_message(self,receiver,message)
        
    def send_broadcast(self,message):
        print(f"{self.name} sends broadcast: {message}")
        self.chat_room.broadcast_message(self,message)
    
    def receive_message(self,sender,message):
        print(f"{self.name} receives message from {sender.name}: {message}")

#Client Code
chat_room = ChatRoom()
user1 = User("Alice", chat_room)
user2 = User("Bob", chat_room)
user3 = User("Charlie", chat_room)

# Users sending messages
user1.send_message(user2, "Hello Bob!")
user2.send_message(user1, "Hi Alice, how are you?")
user1.send_broadcast("Hello everyone!")
user3.send_message(user1, "Hi Alice, I missed your broadcast.")

'''
Output:
Alice sends message to Bob: Hello Bob!
Bob receives message from Alice: Hello Bob!
Bob sends message to Alice: Hi Alice, how are you?
Alice receives message from Bob: Hi Alice, how are you?
Alice sends broadcast: Hello everyone!
Alice receives message from Alice: Hello everyone!
Bob receives message from Alice: Hello everyone!
Charlie receives message from Alice: Hello everyone!
Charlie sends message to Alice: Hi Alice, I missed your broadcast.
Alice receives message from Charlie: Hi Alice, I missed your broadcast.
'''