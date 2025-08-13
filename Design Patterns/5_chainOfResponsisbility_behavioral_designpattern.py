'''
Let's imagine a Logging System that processes different types of log messages (INFO, WARNING, and ERROR). 
The chain of responsibility will allow different handlers to process the log messages depending on their
severity.
'''
# Handler interface: Defines the method to process requests and the link to the next handler
class Logger:
    def __init__(self,next_logger = None):
        self.next_logger = next_logger
    def log(self,message,level):
        pass

# Concrete Handler 1: Handles INFO level logs
class InfoLogger(Logger):
    def log(self,message,level):
        if level == "INFO":
            print(f"INFO: {message}")
        elif self.next_logger:
            self.next_logger.log(message,level)
            
#Concerete handler 2 : Handles WARNING level logs
class WarningLogger(Logger):
    def log(self,message,level):
        if level == "WARNING":
            print(f"WARNING: {message}")
        elif self.next_logger:
            self.next_logger.log(message,level)
            
#Concerete Handler 3 : handles ERROR level logs
class ErrorLogger(Logger):
    def log(self,message,level):
        if level == "ERROR":
            print(f"ERROR: {message}")
        elif self.next_logger:
            self.next_logger.log(message,level)

#Client Code:
error_logger = ErrorLogger()
warning_logger = WarningLogger(error_logger)
info_logger = InfoLogger(warning_logger)

#Testing the chain of responsibility
info_logger.log("This is an info message.", "INFO")
info_logger.log("This is a warning message.", "WARNING")
info_logger.log("This is an error message.", "ERROR")

