from collections import defaultdict
import queue


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        print("Appending edge from {} to {}".format(u, v))
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self, vertex):
        visited, distances = dict(), dict()
        for key in self.graph.keys():
            visited[key] = False

        q = queue.Queue()
        q.put(vertex)
        visited[vertex] = True

        while not q.empty():
            elm = q.get()
            for neighbour in self.graph[elm]:
                if not visited[neighbour]:
                    q.put(neighbour)
                    visited[neighbour] = True
        print(visited)

    def generate_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                edges.append((vertex, neighbour))
                # print("{} -> {}".format(vertex, neighbour))
        print(edges)
        return edges

    def find_distance(self, vertex, destination):
        visited, distances = dict(), dict()
        for key in self.graph.keys():
            visited[key] = False
            distances[key] = -1

        q = queue.Queue()
        q.put(vertex)
        visited[vertex] = True
        distances[vertex] = 0

        while not q.empty():
            elm = q.get()
            for neighbour in self.graph[elm]:
                if not visited[neighbour]:
                    distances[neighbour] = distances[elm] + 1
                    q.put(neighbour)
                    visited[neighbour] = True
        print(distances[destination])


graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(4, 5)
graph.BFS(0)
graph.generate_edges()
graph.find_distance(1, 4)
