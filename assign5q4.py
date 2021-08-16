# Ques 4. Define a class, which have a class parameter and have a same instance parameter.¶
# Hint : Define an instance parameter, need add it in init method.You can init an object with construct parameter or set the value later

class Person:
    name = "Name:"
    def __init__(self, name = None):
      
        self.name = name

dhoni = Person("dhoni")
print(Person.name, dhoni.name)

Python = Person()
Python.name = "Python"
print(Person.name, Python.name)