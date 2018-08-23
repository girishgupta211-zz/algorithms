# Lembda function
MU = 8
a = lambda x, y: (x * MU) / y
print(a(2, 3))
# 5.333333333333333

# # Shallow copy
import copy


class A(object):
    pass


a = A()
a.lst = [1, 2, 3]
a.str = 'cats and dogs'
b = copy.copy(a)  # Here string will be pointing to new location as this is immutable
# b = a # here both will point to same object
# a.lst = [1, 2, 3, 4]
a.lst.append(100)
a.str = 'cats and mice'
print(b.lst)
print(b.str)


# [1, 2, 3, 100]
# cats and dogs


class A(object):
    def __repr__(self):
        return 'instance of A'

    pass


a = A()
b = a

del a
print(b)
# instance of A


import datetime


class Human(object):
    name = None
    gender = None
    birthdate = None

    def __getattr__(self, item):
        if item == 'age':
            return datetime.datetime.now() - self.birthdate
        else:
            return None

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)


h = Human()
h.birthdate = datetime.datetime(1994, 8, 20)
h.age = 28
print(h.age)
# 28
print(h.__dict__)


# {'birthdate': datetime.datetime(1994, 8, 20, 0, 0), 'age': 28}

class Org(object):
    __employees = []
    _employees = []


# Org.__employees.append('Eric')  # This will throw an exception 'AttributeError: type object 'Org'
# # has no attribute '__employees'  but still accessible through Org._Org__employees

Org._Org__employees.append('Eric')
print(Org._Org__employees)
print(Org._employees)
print(dir(Org))


# ['Eric']
# []
# ['_Org__employees', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_employees']


class Gog(Org):
    __employees = []


print(Org._Org__employees)
print(Org._employees)
print(dir(Gog))
# ['Eric']
# []
# ['_Gog__employees', '_Org__employees', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_employees']


import datetime


class Human(object):
    name = None
    g = None
    bd = None

    def __getattr__(self, item):
        # self.__dict__['age'] = item
        if item == 'age':
            return datetime.datetime.now() - self.bd
        else:
            return None

    def __getattribute__(self, item):
        # This will cause infinite recursion
        # return self.__dict__[item]
        return super(Human, self).__getattribute__(item)
        # return object.__getattribute__(self, item)
    #


h = Human()
h.bd = datetime.datetime(1994, 8, 20)
h.age = 28
print(h.age)
print(h.__dict__)


class A:
    brothers = []

    def __init__(self, name):
        self.name = name


a = A('Richard')
b = A('Elly')
a.brothers.append('John')
print(a.name, a.brothers, b.name, b.brothers)
# Richard ['John'] Elly ['John']

a = ['orange', 'apple', 'banana']
b = a
a = ['tomato', 'cucumber', 'carrot']
print(b)


# ['orange', 'apple', 'banana']


# https://stackoverflow.com/questions/51887076/infinite-recursion-when-overriding-setattr/51887126#51887126
# infinite recursion
class Human(object):
    def __setattr__(self, name, value):
        if name == 'gender':
            if value in ('male', 'female'):
                # it calls __setattr__ in an infinite loop
                # self.gender = value
                super().__setattr__(name, value)

            else:
                # super(Human, self).__setattr__(name, value)
                raise AttributeError('Gender can only be "male" or "female"')
        else:
            super().__setattr__(name, value)


h = Human()
h.name = 'Sweety'
# This will cause infinite recursion
h.gender = 'female'
print(h.name)
print(h.gender)


# Sweety
# female

#
class A:
    pass


class B:
    pass


a = A()
b = B()
print(type(a) == type(b), type(a), type(b))
# False <class '__main__.A'> <class '__main__.B'>


lst = ['I', 'am', 'Python', 'programmer']

s1 = ""
for x in lst:
    s1 += x
print(s1)
# IamPythonprogrammer

# More efficient
s2 = "".join(lst)
print(s2)
# IamPythonprogrammer
