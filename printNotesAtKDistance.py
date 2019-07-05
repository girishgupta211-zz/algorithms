class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


def print_notes_at_k_distance(root, k):
    print("printing nodes at label: {}".format(k))
    if root is None:
        return
    if k == 0:
        print(root.value)
    else:
        # print k-1
        print_notes_at_k_distance(root.left, k - 1)
        print_notes_at_k_distance(root.right, k - 1)


def get_level_diff(root):
    if root is None:
        return 0
    else:
        return root.value - get_level_diff(root.left) - get_level_diff(
            root.right)


def print_at_a_level(root, label):
    if root is None:
        return
    if label == 1:
        print(root.value)

    print_at_a_level(root.left, label - 1)
    print_at_a_level(root.right, label - 1)


def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1


tree_root = Node(1)
tree_root.left = Node(2)
tree_root.right = Node(3)
tree_root.left.left = Node(4)
tree_root.left.right = Node(5)
tree_root.right.left = Node(6)
tree_root.right.right = Node(7)
# print height(root)
print_notes_at_k_distance(tree_root, 2)

# Driver program to test above function
tree_root = Node(5)
tree_root.left = Node(2)
tree_root.right = Node(6)
tree_root.left.left = Node(1)
tree_root.left.right = Node(4)
tree_root.left.right.left = Node(3)
tree_root.right.right = Node(8)
tree_root.right.right.right = Node(9)
tree_root.right.right.left = Node(7)


# print_notes_at_k_distance(root,0)
# print get_level_diff(root)

# print_at_a_level(root,4)

# for i in range(0,5):
# 	print_at_a_level(root,i)

# Function to  print level order traversal of tree
def print_level_order(root):
    h = height(root)
    for i in range(1, h + 1):
        print("printing at level: {}".format(i))
        print_at_a_level(root, i)


print_level_order(tree_root)
