"""
This file holds the practice on Abstract classes
"""
from abc import ABC, abstractmethod

class Session(ABC):
    @abstractmethod
    def generate_token(self):
        pass

    @abstractmethod
    def logout(self):
        pass


class AppSession(Session):
    def generate_token(self):
        print("Client token generated: aosindfasodnfaosind")
    
    def logout(self):
        print("Performing logout")

class UISession(Session):
    def generate_token(self):
        print("Client token generated: aosindfasodnfaosind")

    def logout(self):
        print("Performing logout")
    

app_session = AppSession()
app_session.generate_token()
# abstract classes do not have instances
# causes TypeError
# TypeError: Can't instantiate abstract class Session without an implementation for abstract methods 'generate_token', 'logout'
# session = Session()
