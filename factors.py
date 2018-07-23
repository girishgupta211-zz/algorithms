def factors(n):
    l1, l2 = [], []
    square_root = int(n ** 0.5)
    for i in range(1, square_root + 1):
        quotient, reminder = n // i, n % i  # Alter: divmod() fn can be used.
        if reminder == 0:
            l1.append(i)
            # Check if both quotient and i are not equal to avoid duplicate numbers
            if i != quotient:
                l2.append(quotient)  # quotients obtained are decreasing.
    l2.reverse()
    return l1 + l2


facts = factors(10)
print(facts)
