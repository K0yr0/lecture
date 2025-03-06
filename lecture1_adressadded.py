class Person:
    # writing information of the person
    def __init__(self, name, age, adress):
        # we assign the name
        self.name = name
        # and assign the age
        self.age = age
        # assign adress
        self.adress = adress

    # for greeting
    def greet(self):
        return f"Hello my name is {self.name} and my age is {self.age} and I am from {self.adress}"

# Example
# assigning the person to p1
p1 = Person("Kayra", 19, "Eskişehir")
# printing the greeting
print(p1.greet())
