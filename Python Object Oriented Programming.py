# class - 'class' is tool used to create new objects.
# Classes can generate objects (isntances).
# Classes have their own attribute and methods.
# Generated objects can use their 'class' functions to do things.
# PascalCase is the nomenclature to make a class
# ex of nomenclature: LinearRegression

"""
class Person:
    def name(self):
        return Person


p1 = Person()
print(p1.name)


class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


p1 = Person('Arthur', 'Lima')

print(p1.name)
print(p1.last_name)
"""

from classes import *

f1 = Camera('Sony')
f2 = Camera('GoPro')

print(f1.tofilm())
print(f1.filming)
print(f2.tofilm())
print(f2.filming)
print(f2.photograph())
print(f2.stopfilm())
print(f2.photograph())
print()
print()

s1 = SaveFile({'name': 'Arthur', 'age': 19}, {'name': 'Alan', 'age': 17})

s1.savefile()
s1.readfile()
print()
print()

print(LearningMethods.ano)
wo = LearningMethods.classmethod('Hello')

print(wo.word)
print()
print()


c1 = Connections()
c1.set_user('Arthur')
c1.set_password(12131)
print(c1.user)
print(c1.password)
print()
print()


print(Connections.create_with_auth('Alan', 446).user)
print(Connections.create_with_auth('Alan', 446).password)
print()
print(Connections.sum(6, 3))
print()
print()


print(Pen('Azul').get_color())
print()
print()


print("@property > GETTER: ", Pencil('White').color)

Pencil.color = 'Purple'
print("@color.setter > SETTER: ", Pencil.color)
