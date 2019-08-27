# There are ( N+1 ) people in a party, they might or might not know each others names.
# There is one celebrity in the group (total N + 1 people),
# celebrity does not know any of N peoples by name and all N people know celebrity by name.
# You are given the list of people’s names (N + 1), You can ask only one question from the people.
# Do you know this name? How many maximum number of questions you need to ask to know the celebrity name?
# ~~~~Asked in: Google, Flipkart, Amazon, Microsoft


N = 8

# Person with 2 is celebrity
MATRIX = [[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0]
          ]


def knows(a, b):
    return MATRIX[a][b]


#  Returns id of celebrity
def findCelebrity(n):
    # Initialize two pointers as two corners
    a = 0
    b = n - 1

    # Keep moving while the two pointers  don't become same.
    # while a<b:
    #     pass

    #
    # while  a<b:
    #     pass

    while a < b:
        if knows(a, b):
            a += 1
        else:
            b -= 1

    # Check if a is actually a celebrity or not
    for i in range(0, n):
        # If any person doesn't know 'a' or 'a' doesn't know any person, return -1
        if i != a and (knows(a, i) or not knows(i, a)):
            return -1

    return a

n = 4
id = findCelebrity(n)
if id != -1:
    print("Celebrity ID ", id)
else:
    print("No celebrity")
