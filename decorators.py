from functools import wraps


def validate_args(*expected_args):
    def docorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("expected params: {}".format(expected_args))
            print("args: {}".format(args))
            print("kwargs: {}".format(kwargs))
            return func(*args, **kwargs)

        return wrapper

    return docorator


def first_decorator(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        print("Before first decorated function")
        r = f(*args, **kwargs)
        print("After second decorated function")
        return r

    return wrapped


@first_decorator
@validate_args('test param1', 'test param2')
def sum_two_numbers(a, b):
    print("Inside the sum_two_numbers function")
    return a + b


sum_two_numbers(2, 7)
