class A:
    def func(self):
        print("func() is being called")


def monkey_f(self):
    print("monkey_f() is being called")


obj = A()
obj.func()
A.func = monkey_f

obj = A()
obj.func()
# reference : https://www.geeksforgeeks.org/monkey-patching-in-python-dynamic-behavior/
