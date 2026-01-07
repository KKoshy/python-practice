"""
This file holds the practice on encapsulation types
"""
class User:
    def __init__(self, name, email_id, emp_id) -> None:
        self.name = name
        self._email_id = email_id
        self.__emp_id = emp_id

    def get_user_details(self):
        print(f"Name: {self.name}")
        print(f"e-mail id: {self._email_id}")
        print(f"Employee id: {self.__emp_id}")

    @property
    def emp_id(self):
        print("Getter for emp_id")
        return self.__emp_id

    @emp_id.setter
    def emp_id(self, emp_id):
        print("Setter for emp_id")
        if isinstance(emp_id, str):
            self.__emp_id = emp_id
            print("Employee id has been updated")
        else:
            raise ValueError(f"Invalid emp id: {emp_id}")


user = User("Al", "al@adfa.com", "123UEXH")
print("Accessing user details")
user.get_user_details()
print("Accessing public attribute")
print(user.name)
print("Accessing protected attribute")
print(user._email_id)
# Causes AttributeError
# print("Accessing private attribute")
# print(user.__emp_id)
print(user.emp_id)
user.emp_id = "123MXUV"
print(user.emp_id)
