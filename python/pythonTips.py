# # Mutation
foo = ['hi']
print(foo)
# Output: ['hi']

bar = foo
bar += ['bye']
print(foo)
print(bar)


# Output: ['hi', 'bye']

def add_to(num, target=[]):
    target.append(num)
    return target


print(add_to(1))
# Output: [1]

print(add_to(2))

# Output: [1, 2]

print(add_to(3))


# Output: [1, 2, 3]

# Well again it is the mutability of lists which causes this pain.
# In Python the default arguments are evaluated once when the function
# is defined, not each time the function is called.
# You should never define default arguments of mutable type unless
# you know what you are doing. You should do something like this:
def add_to_immutable(num, target=None):
    if target is None:
        target = []
    target.append(num)
    return target


print(add_to_immutable(1))
# Output: [1]
print(add_to_immutable(2))
# Output: [2]
print(add_to_immutable(3))
# Output: [3]

from functools import reduce

res = reduce((lambda x, y: x + y), [1, 2, 3, 4])
print(res)

func = lambda x: x * x
print(func(9))


# MRO
class A(object):
    def dothis(self):
        print('I am from A class')


class B1(A):
    def dothis(self):
        print('I am from B1 class')
    # pass


class B2(object):
    def dothis(self):
        print('I am from B2 class')
    # pass


class B3(A):
    def dothis(self):
        print('I am from B3 class')


# Diamond inheritance
class D1(B1, B3):
    pass


class D2(B1, B2):
    pass


d1_instance = D1()
d1_instance.dothis()
# I am from B1 class
print(D1.__mro__)
# (<class '__main__.D1'>, <class '__main__.B1'>, <class '__main__.B3'>, <class '__main__.A'>, <class 'object'>)


d2_instance = D2()
d2_instance.dothis()
# I am from B1 class
print(D2.__mro__)
# (<class '__main__.D2'>, <class '__main__.B1'>, <class '__main__.A'>, <class '__main__.B2'>, <class 'object'>)
