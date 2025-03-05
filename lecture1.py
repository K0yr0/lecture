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
     return f"Hello my name is {self.name} and my age is {self.age}" #writing f so it can understand the self.name and self.age

# Example
#assigning the person to p1
p1 = Person("Kayra", 19)
#printing the greetment
print(p1.greet())
