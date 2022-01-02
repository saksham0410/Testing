
# Class concept purpose file, update this file for all class concept logics

class Parent:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def print_value(self):
        print(f"My name is {self.a} and age is {self.b}")

    def work(self):
        print("This is a work function")


obj = Parent("Saksham",30)
obj.print_value()
