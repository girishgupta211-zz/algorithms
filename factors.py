# def factors(n):    
#     return reduce(list.__add__, 
#                 ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))


def factors(n):    
    l1, l2 = [], []
    for i in range(1, int(n ** 0.5) + 1):
    	print i
        q,r = n//i, n%i     # Alter: divmod() fn can be used.
        if r == 0:
            l1.append(i) 
            l2.append(q)    # q's obtained are decreasing.
    if l1[-1] == l2[-1]:    # To avoid duplication of the possible factor sqrt(n)
        l1.pop()
    l2.reverse()
    return l1 + l2


facts = factors(10)

if(len(facts) <= 3):
	print facts[0]
else:
	print 0
