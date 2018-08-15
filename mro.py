# Base class
class A(object):
    def do_this(self):
        print('I am from A class')


class B1(A):
    def do_this(self):
        print('I am from B1 class')
    # pass


class B2(object):
    def do_this(self):
        print('I am from B2 class')
    # pass


class B3(A):
    def do_this(self):
        print('I am from B3 class')


# Diamond inheritance
class D1(B1, B3):
    pass


class D2(B1, B2):
    pass


d1_instance = D1()
d1_instance.do_this()
# I am from B1 class
print(D1.__mro__)
# (<class '__main__.D1'>, <class '__main__.B1'>, <class '__main__.B3'>, <class '__main__.A'>, <class 'object'>)


d2_instance = D2()
d2_instance.do_this()
# I am from B1 class
print(D2.__mro__)
# (<class '__main__.D2'>, <class '__main__.B1'>, <class '__main__.A'>, <class '__main__.B2'>, <class 'object'>)
