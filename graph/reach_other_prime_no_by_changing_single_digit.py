import queue


# Class to represent a graph
class Graph:
    def __init__(self, V):
        self.V = V  # No. of vertices
        self.prime_list = [[] for i in range(V)]

    # function to add an edge to graph
    def addedge(self, V1, V2):
        self.prime_list[V1].append(V2)
        self.prime_list[V2].append(V1)

    def bfs(self, in1, in2):
        visited = [0] * self.V
        que = queue.Queue()
        visited[in1] = 1
        que.put(in1)
        while not que.empty():
            prime_index = que.get()
            i = 0
            while i < len(self.prime_list[prime_index]):
                if not visited[self.prime_list[prime_index][i]]:
                    visited[self.prime_list[prime_index][i]] = visited[prime_index] + 1
                    que.put(self.prime_list[prime_index][i])
                if self.prime_list[prime_index][i] == in2:
                    return visited[self.prime_list[prime_index][i]] - 1
                i += 1


# // Finding all 4 digit prime numbers
def SieveOfEratosthenes(v):
    # Create a boolean array "prime[0..n]" and initialize all entries it as true. A value in prime[i] will be
    # finally be false if i is Not a prime, else true.
    n = 9999
    prime = [True] * (n + 1)
    p = 2
    while p * p <= 9999:
        if prime[p]:
            i = p * p
            while i <= 9999:
                prime[i] = False
                i = i + p
        p = p + 1
    # v = []
    for i in range(1000, n + 1):
        if prime[i]:
            v.append(i)
    return v


def compare(num1, num2):
    # To compare the digits
    s1 = str(num1)
    s2 = str(num2)
    c = 0
    if s1[0] != s2[0]:
        c += 1
    if s1[1] != s2[1]:
        c += 1
    if s1[2] != s2[2]:
        c += 1
    if s1[3] != s2[3]:
        c += 1
        # If the numbers differ only by a single # digit return true else false
    return c == 1


def shortestPath(num1, num2):
    # Generate all 4 digit
    pset = []
    SieveOfEratosthenes(pset)
    # Create a graph where node numbers # are indexes in pset[] and there is
    # an edge between two nodes only if # they differ by single digit.
    g = Graph(len(pset))
    for i in range(len(pset)):
        for j in range(i + 1, len(pset)):
            if compare(pset[i], pset[j]):
                g.addedge(i, j)
    # Since graph nodes represent indexes # of numbers in pset[], we find indexes
    # of num1 and num2.
    in1, in2 = None, None
    for j in range(len(pset)):
        if pset[j] == num1:
            in1 = j
    for j in range(len(pset)):
        if pset[j] == num2:
            in2 = j
    return g.bfs(in1, in2)


# Driver code
if __name__ == '__main__':
    num1 = 1033
    num2 = 8179
    print(shortestPath(num1, num2))
