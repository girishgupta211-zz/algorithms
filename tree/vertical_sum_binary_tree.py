class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


# Data Structure to store a doubly linked list node
class ListNode:

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return str(self.data)


# Function to print the vertical sum stored in given doubly linked list
def print_dll_from_head(node):
    if not node:
        return

    # Search Head Node
    while node.prev:
        node = node.prev

    # Print From Head To Tail
    while node:
        print(node.data, end=" ")
        node = node.next


# Recursive function to do a pre-order traversal of the tree and calculate the
# vertical sum of given binary tree.
# Each node of doubly linked list will store the sum of tree nodes at
# corresponding vertical line in a binary tree
def update_list_with_vertical_sum(root, list):
    if not root:
        return

    # update the data of linked list node corresponding to the vertical line
    # passing through current tree node
    list.data = list.data + root.data

    # create a new linked list node corresponding to the vertical line through
    # through root's right child, if not already.
    # This node would be the next pointer of current linked list node
    if root.right:
        if not list.next:
            list.next = ListNode(0, list, None)
        # recur for  right subtree
        update_list_with_vertical_sum(root.right, list.next)

    # create a new linked list node corresponding to the vertical line passing
    # through root's left child, if not already.
    # This node would be the prev pointer of current linked list node
    if root.left:
        if not list.prev:
            list.prev = ListNode(0, None, list)
        # recur for left  subtree
        update_list_with_vertical_sum(root.left, list.prev)


# Function to find and print the vertical sum of given binary tree
def print_vertical_sum_binary_tree(root):
    # create a linked list node corresponding to the vertical line through
    # root node
    list = ListNode(0, None, None)

    # calculate vertical sum and store it in doubly linked list
    update_list_with_vertical_sum(root, list)

    # print the linked list
    print_dll_from_head(list)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.right.left = Node(5)
    root.right.right = Node(6)

    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    print_vertical_sum_binary_tree(root)
