#Creating a class
class Person:
    #writing information of the person
    def __init__(self, name, age):
        #we assign the name
        self.name = name
        #and assign the age
        self.age = age
#for greeting
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Example
p1 = Person("Alice", 30)
print(p1.greet())
