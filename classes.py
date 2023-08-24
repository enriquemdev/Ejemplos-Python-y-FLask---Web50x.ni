# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p = Point(3, 5)
# print(p.x)
# print(p.y)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
vasquez = Person("Vasquez", 25)
Samuel = Person("Samuel", 30)
print(vasquez.age)
Samuel.say_hello()

# class Person:
#     def __init__(vasquez, name, age):
#         vasquez.name = name
#         vasquez.age = age


