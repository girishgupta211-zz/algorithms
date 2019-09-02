# Not Working
def chocolates_from_wrappers_recursion(chocolates, wrap, total_chocolates):
    if chocolates < wrap:
        return total_chocolates

    new_chocolates = chocolates // wrap
    total_chocolates = total_chocolates + new_chocolates
    return chocolates_from_wrappers_recursion(new_chocolates + chocolates % wrap, wrap, total_chocolates)


def count_max_chocolate(money, price, wrap):
    chocolates = money // price
    # 7
    new_chocolates = chocolates_from_wrappers_recursion(chocolates, wrap, 0)
    return chocolates + new_chocolates


money = 21
price = 3
wrap = 3

result = count_max_chocolate(money, price, wrap)
print(result)


# Working
def count_max_chocolate(money, price, wrap):
    total_chocolates = 0
    chocolates = money // price

    while wrap <= chocolates:
        total_chocolates += chocolates

        new_chocolates = chocolates // wrap
        chocolates = new_chocolates + chocolates % wrap

    return total_chocolates


money = 21
price = 3
wrap = 3

result = count_max_chocolate(money, price, wrap)
print(result)
