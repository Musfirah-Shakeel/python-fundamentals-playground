

class Person:
     def __init__(self,age,age1):
          self.age=age
          self.age1=age1


     def greet(self):
         return f"Hello, my name is {self.age} and I am {self.age1} years old."
person1 = Person("Alice", 25)
print(person1.greet())































