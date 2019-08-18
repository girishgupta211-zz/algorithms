from collections import defaultdict


class Tree:
    def __init__(self, item):
        self.value = item
        self.left = None
        self.right = None


def pre_order(node):
    if node is None:
        return
    print(node.value)

    pre_order(node.left)
    pre_order(node.right)


def post_order(node):
    if node is None:
        return

    post_order(node.left)
    post_order(node.right)
    print(node.value)


def in_order(node):
    if node is None:
        return

    in_order(node.left)
    print(node.value)
    in_order(node.right)


def vertical_view(node, hd, nodes_map):
    if node is None:
        return
    vertical_view(node.left, hd - 1, nodes_map)
    nodes_map[hd].append(node.value)
    vertical_view(node.right, hd + 1, nodes_map)


tree = Tree(1)
tree.left = Tree(2)
tree.right = Tree(3)
tree.left.left = Tree(4)
tree.left.right = Tree(5)
tree.right.left = Tree(6)
tree.right.right = Tree(7)
print("pre_order")
pre_order(tree)
print("post_order")
post_order(tree)
print("in_order")
in_order(tree)

print("vertical_view")
m = defaultdict(list)
vertical_view(tree, 0, m)
print(m)
for elm in m:
    for item in m[elm]:
        print(item)


def bottom_view(node, hd, nodes_map):
    # Override all previous values and keep only the last value for a given horizontal distance
    if node is None:
        return
    bottom_view(node.left, hd - 1, nodes_map)
    nodes_map[hd] = node.value
    bottom_view(node.right, hd + 1, nodes_map)


print("get_horizontal_distance")

m = dict()
bottom_view(tree, 0, m)
print(m)
for elm in m:
    print(m[elm])

#
# def left_view(node, hd, nodes_map):
#     if node is None:
#         return
#
#     nodes_map[hd].append(node.value)
#     left_view(node.left, hd - 1, nodes_map)
#     left_view(node.right, hd + 1, nodes_map)
#
#
# print("left_view")
#
# m = dict()
# left_view(tree, 0, m)
# print(m)
# for elm in m:
#     print(m[elm])
