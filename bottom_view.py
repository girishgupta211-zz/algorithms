class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.horizontal_distance = 0


def bottom_view(root):
    if not root:
        return

    root.horizontal_distance = 0
    queue = [root]
    bottom_view_map = dict()

    while queue:
        temp_node = queue.pop(0)
        horizontal_distance = temp_node.horizontal_distance

        print("data:{}  horizontal_distance: {}".format(temp_node.data,
                                                        horizontal_distance))

        bottom_view_map[horizontal_distance] = temp_node.data

        if temp_node.left is not None:
            temp_node.left.horizontal_distance = horizontal_distance - 1
            queue.append(temp_node.left)

        if temp_node.right is not None:
            temp_node.right.horizontal_distance = horizontal_distance + 1
            queue.append(temp_node.right)
    return bottom_view_map


tree = Node(2)
tree.left = Node(7)
tree.right = Node(5)
tree.left.left = Node(2)
tree.left.right = Node(6)
tree.right.right = Node(9)
tree.left.right.left = Node(5)
tree.left.right.right = Node(11)
tree.right.right.left = Node(4)

result = bottom_view(tree)
print(result)
