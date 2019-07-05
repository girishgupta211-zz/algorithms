# Program to print BFS traversal from a given source
# vertex. BFS(int s) traverses vertices reachable
# from s.
from collections import defaultdict


# This class represents a directed graph using adjacency
# list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def add_edge(self, u, v):
        print("Appending edge from {} to {}".format(u, v))
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, vertex):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
        print(visited)

        # Create a queue for BFS
        queue = list

        # Mark the source node as visited and enqueue it
        queue.append(vertex)
        visited[vertex] = True
        print(visited)

        while queue:
            # Dequeue a vertex from queue and print it
            # print(queue)
            vertex = queue.pop(0)
            # print(vertex, )
            # print("queue" + str(queue))

            # Get all adjacent vertices of the dequeued
            # vertex s. If a adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[vertex]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        print(visited)


# Driver code
# Create a graph given in the above diagram
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
print("Following is Breadth First Traversal (starting from vertex 2)")
g.BFS(2)
print(g.graph)


def generate_edges(graph):
    edges = []
    # for each node in graph
    for node in graph:
        # print(node)
        # for each neighbour node of a single node
        for neighbour in graph[node]:
            # if edge exists then append
            edges.append((node, neighbour))
    return edges


print(generate_edges(g.graph))


# function to find path
def find_path(graph, start, end, path=[]):
    path = path + [start]
    # path = path.append([start])
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path
            return None


# Driver function call to print the path
print(find_path(g.graph, 0, 3))
print(find_path(g.graph, 0, 3))
