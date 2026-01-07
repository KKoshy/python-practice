"""
This file holds the practice on creating instances with class method
"""
from datetime import date

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_license_eligibility(self):
        if self.age>=18:
            print(f"{self.name} is eligible")
        else:
            print(f"{self.name} is not eligible")
    
    @staticmethod
    def calculate_age(year):
        as_of = date.today()
        current_year = as_of.year
        return current_year - year
    
    @classmethod
    def form_instance(cls, email, year):
        name = email.split("@")[0]
        age = cls.calculate_age(year)
        return cls(name, age)
    
print("Case-01: Alice")
alice = User("alice", 40)
alice.check_license_eligibility()

print("Case-02: Just a generic check")
print(User.calculate_age(1997))

bob = alice.form_instance("bob@gmail.com", 1991)
bob.check_license_eligibility()
