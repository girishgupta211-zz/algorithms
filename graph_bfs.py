from collections import defaultdict
import queue


class Graph:
    """
    Graph traversal algorithm using BFS
    """

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
                print("{} -> {}".format(vertex, neighbour))
        # print(edges)
        return edges

    def find_distance(self, vertex):
        visited, distances, nodes = dict(), dict(), dict()
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
                    nodes[neighbour] = elm
        return distances, nodes

    # TODO this is not gining the shortest path
    def find_path(self, start, end, path=[]):
        path = path + [start]
        # path = path.append([start])
        if start == end:
            return path
        for node in self.graph[start]:
            if node not in path:
                new_path = self.find_path(node, end, path)
                if new_path:
                    return new_path
                return None


if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(4, 5)
    graph.BFS(0)
    graph.generate_edges()
    start_node = 1
    destination_node = 4
    distances_from_start, parent_nodes = graph.find_distance(start_node)
    # shortest_path = graph.find_path(1, 4)
    min_distance = distances_from_start[destination_node]
    print("minimum distance between {} and {}: {}".
          format(start_node, destination_node, min_distance))

    crawl = destination_node
    shortest_path = [destination_node]
    while crawl != start_node:
        parent = parent_nodes[crawl]
        shortest_path.insert(0, parent)
        crawl = parent
    print("shortest path between {} and {}: {}".
          format(start_node, destination_node,
                 "->".join(map(str, shortest_path))))
