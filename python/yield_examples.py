print("simple_generator_fun")


def simple_generator_fun():
    yield 1
    yield 2
    yield 3


for value in simple_generator_fun():
    print(value)

print("next_square")


def next_square():
    i = 1

    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes
        # from this point


for square in next_square():
    if square > 100:
        break
    print(square)

print("print_even_numbers")


def print_even_numbers(arr_list):
    for num in arr_list:
        if num % 2 == 0:
            yield num


num_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 78, 43, 32]
for num in print_even_numbers(num_list):
    print(num)

print("get_next_delivery")


def get_next_delivery():
    over = 0
    deliveries = range(1, 7)
    current_delivery = -1

    while over < 100:
        current_delivery += 1
        current_delivery %= 6

        if current_delivery == 0:
            over += 1

        yield '{}{}'.format(over, deliveries[current_delivery])


# for deliver in get_next_delivery():
#     print(deliver)

it = get_next_delivery()

for i in range(1, 10):
    print(next(it))

print("get_next_ball")


def get_next_ball():
    over = 0
    delivery = 1
    while over <= 20:
        yield "{}{}".format(over, delivery)
        delivery += 1
        if delivery % 7 == 0:
            delivery = 1
            over += 1


for over in get_next_ball():
    print(over)
