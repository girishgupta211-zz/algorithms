prime = [True] * 10000


def generate_prime_numbers():
    p = 2
    while p * p <= 9999:
        if prime[p]:
            i = p * p
            while i <= 9999:
                prime[i] = False
                i = i + p
        p = p + 1
    print(prime)


def generate_all_4_digit_prime_numbers():
    result = []
    for i in range(1000, 9999 + 1):
        if prime[i]:
            result.append(i)
    print(result)


generate_prime_numbers()
generate_all_4_digit_prime_numbers()
