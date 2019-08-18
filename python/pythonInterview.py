l = [1, 2, 3]


def sum(l):
    # l = [1, 2, 3, 4]
    l.append(4)

print(l)


class A:
    b = 10
    def __init__(self, a):
        self.a = a
    #
    # def __setattr__(self, key, value):
    #     pass

    @staticmethod
    def my_print():
        print("upload")

    @classmethod
    def my_print(cls):
        print("upload")
        print(b)


a = A(10)
print(a.a)
a.b = 21
print(a.b)
b = A(20)
# print(b.b)
# Monkey patching
A.my_print()
a.my_print()

# difference between staticmethod and classmethod
# How to get count for number of instances a class have at a particular time
# How to make a class immutable
# How to access a variable created just outside my class before __init__ without self
# in python how variables are passed? pass by value or pass by reference
# Write our own context manager
# What is closure and hoisting in java script


def append_one(li):
    li.append(1)
x = [0]
append_one(x)
print(x)

l = [1, 2, 3]
def sum(l):
    # l = [1, 2, 3, 4]
    l.append(4)
sum(l)
print(l)

def append_one(li):
    # li = [0, 1]
    li.append(2)
x = [0]
append_one(x)
print(x)

str = "hello"
print(str*2)


class Test(object):
    def __getitem__(self, items):
        pass
        print('%-15s  %s' % (type(items), items))

t = Test()
t[1]
t['hello world']
t[1, 'b', 3.0]
t[5:200:10]
t['a':'z':3]
t[object()]

print(t.__getitem__((1, 'b', 3.0)))

#
class Test(object):
    def __call__(self, *args, **kwargs):
        print (args)
        print (kwargs)
        print ('-'*80)

t = Test()
t(1, 2, 3)
t(a=1, b=2, c=3)
t(4, 5, 6, d=4, e=5, f=6)


class Test(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
    #
    def __getattr__(self, name):
        return 123456

t = Test()
print ('object variables: %r' % t.__dict__.keys())
print(t.a)
print(t.b)
print(t.c)
print (getattr(t, 'd'))
print (hasattr(t, 'x'))

# object variables: dict_keys(['a', 'b'])
# a
# b
# 123456
# 123456
# True



class Test(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __setattr__(self, name, value):
        print ('set %s to %s' % (name, repr(value)))

        if name in ('a', 'b'):
            object.__setattr__(self, name, value)

t = Test()
t.c = 'z'
setattr(t, 'd', '888')
# set a to 'a'
# set b to 'b'
# set c to 'z'
# set d to '888'

class Example:
    name = "Example"

    @staticmethod
    def static():
        print ("%s static() called" % Example.name)

class Offspring1(Example):
    name = "Offspring1"

class Offspring2(Example):
    name = "Offspring2"

    @staticmethod
    def static():
        print ("%s static() called" % Offspring2.name)

Example.static() # prints Example
Offspring1.static() # prints Example
Offspring2.static() # prints Offspring2
# Example static() called
# Example static() called
# Offspring2 static() called

class Example:
    name = "Example"

    @classmethod
    def static(cls2):
        print("%s static() called" % cls2.name)


class Offspring1(Example):
    name = "Offspring1"
    pass


class Offspring2(Example):
    name = "Offspring2"

    @classmethod
    def static(cls):
        print("%s static() called" % cls.name)


Example.static()  # prints Example
Offspring1.static()  # prints Offspring1
Offspring2.static()  # prints Offspring2
# Example static() called
# Offspring1 static() called
# Offspring2 static() called


class CSStudent:
    stream = 'cse'  # Class Variable

    def __init__(self, name, roll):
        self.name = name  # Instance Variable
        self.roll = roll  # Instance Variable


# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.name)  # prints "Geek"
print(b.name)  # prints "Nerd"
print(a.roll)  # prints "1"
print(b.roll)  # prints "2"

# Class variables can be accessed using class
# name also
print(CSStudent.stream)  # prints "cse"
print(a.__dict__)
