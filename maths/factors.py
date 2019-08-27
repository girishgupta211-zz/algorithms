from functools import reduce


def factors(n):
    l1, l2 = [], []
    square_root = int(n ** 0.5)
    for i in range(1, square_root + 1):
        quotient, reminder = n // i, n % i  # Alter: divmod() fn can be used.
        if reminder == 0:
            l1.append(i)
            l2.append(quotient)

    # Check if both quotient and reminder are equal to avoid duplicate numbers
    if l1[-1] == l2[-1]:
        l1.pop()

    # quotients obtained are in decreasing order.
    l2.reverse()
    return l1 + l2


facts = factors(15)
print(facts)


# Using list comprehensions
def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                      ([i, n // i] for i in
                       range(1, int(pow(n, 0.5) + 1), step) if
                       n % i == 0)))


print(factors(15))
# https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
