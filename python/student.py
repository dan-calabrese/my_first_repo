# Declare the class BankAccount
# Python convention is to capitalize first letter in each word of class name
class Student:
    def __init__(self, fname, lname, id, energy_level = 10):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.energy_level = energy_level

    def __str__(self):
        return f"{self.lname}: {self.id}"

    def greeting(self):
        print("Hello, how are you?")

    def take_exam(self):
        self.energy_level = self.energy_level - 1

    def get_energy_level(self):
        return f"{self.fname}'s energy level is {self.energy_level}."
    