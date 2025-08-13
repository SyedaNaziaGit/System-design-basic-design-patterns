'''
Let’s say we have a DatabaseConnection class, and we want to make sure there is only one connection to the
database throughout the application. We can use the Singleton pattern to ensure this.
'''
class DatabaseConnection:
    _instance = None #this will hold the single instance
    def __new__(cls):
        if cls._instance is None: #if no instance exists create one
            print("Creating  a new database connection ...")
            cls._instance = super().__new__(cls)
        return cls._instance
    def connect(self):
        return "Connecting  to the database"

#Client code
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1.connect())  # Output: Connecting to the database...
print(db2.connect())  # Output: Connecting to the database...
print(db1 is db2)  # Output: True (Both variables refer to the same instance)
'''
Output:
Creating a new database connection...
Connecting to the database...
Connecting to the database...
True
'''