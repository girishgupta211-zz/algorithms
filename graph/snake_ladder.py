# Python3 program to find minimum number of dice throws required to reach last
# cell from first cell of a given snake and ladder board


class QueueEntry(object):
    def __init__(self, vertex_no=0, dist=0):
        """# An entry in queue used in BFS. This represents distance of current vertex from vertex 0"""
        self.vertex_no = vertex_no
        self.distance = dist


'''This function returns minimum number of dice throws required to. Reach last cell  
from 0'th cell in a snake and ladder game. move[] is an array of size N where N is  
no. of cells on board. If there is no snake or ladder from cell i, then move[i]  
is -1. Otherwise move[i] contains cell to which snake or ladder at i takes to.'''


def get_min_dice_throws(move, N):
    # The graph has N vertices. Mark all the vertices as not visited
    visited = [False] * N

    # Create a queue for BFS 
    queue = []

    # Mark the node 0 as visited and enqueue it 
    visited[0] = True

    # Distance of 0't vertex is also 0. Enqueue 0'th vertex
    queue.append(QueueEntry(0, 0))

    # Do a BFS starting from vertex at index 0 
    while queue:
        qe = queue.pop(0)
        vertex_no = qe.vertex_no  # Vertex no. of queue entry

        # If front vertex is the destination vertex, we are done
        if vertex_no == N - 1:
            break

        # Otherwise dequeue the front vertex and enqueue its adjacent vertices
        # (or cell numbers reachable through a dice throw)
        adjacent_vertex = vertex_no + 1
        while adjacent_vertex <= vertex_no + 6 and adjacent_vertex < N:

            # If this cell is already visited, then ignore
            if visited[adjacent_vertex] is False:
                # Otherwise calculate its distance and mark it as visited
                queue_entry = QueueEntry()
                queue_entry.distance = qe.distance + 1
                visited[adjacent_vertex] = True

                # Check if there a snake or ladder at 'j' then tail of snake or top
                # of ladder become the adjacent of 'i' 
                queue_entry.vertex_no = move[adjacent_vertex] if move[adjacent_vertex] != -1 else adjacent_vertex

                queue.append(queue_entry)

            adjacent_vertex += 1

    # We reach here when 'qe' has last vertex 
    # return the distance of vertex in 'qe 
    return qe.distance


# driver code
N = 30
moves = [-1] * N

# Ladders 
moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28

# Snakes 
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6

print("Min Dice throws required is {0}".
      format(get_min_dice_throws(moves, N)))
