# Python program to print nodes at distance k from a given node


# A binary tree node
class Node:
    # A constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Recursive function to print all the nodes at distance k
# int the tree(or subtree) rooted with given root. See
def printkDistanceNodeDown(root, k):
    # Base Case
    if root is None or k < 0:
        return

    # If we reach a k distant node, print it
    if k == 0:
        print(root.data)

        return

    # Recur for left and right subtee
    printkDistanceNodeDown(root.left, k - 1)
    printkDistanceNodeDown(root.right, k - 1)


# Prints all nodes at distance k from a given target node
# The k distant nodes may be upward or downward. This function
# returns distance of root from target node, it returns -1
# if target node is not present in tree rooted with root
def printkDistanceNode(root, target, k):
    # Base Case 1 : IF tree is empty return -1
    if root is None:
        return -1

    # If target is same as root. Use the downward function
    # to print all nodes at distance k in subtree rooted with
    # target or root
    if root == target:
        printkDistanceNodeDown(root, k)
        return 0

    # Recur for left subtree
    dleft = printkDistanceNode(root.left, target, k)

    # Check if target node was found in left subtree
    if dleft != -1:

        # If root is at distance k from target, print root
        # Note: dl is distance of root's left child
        # from target
        if dleft + 1 == k:
            print(root.data)


        # Else go to right subtreee and print all k-dl-2
        # distant nodes
        # Note: that the right child is 2 edges away from
        # left chlid
        else:
            printkDistanceNodeDown(root.right, k - dleft - 2)

        # Add 1 to the distance and return value for
        # for parent calls
        return 1 + dleft

    # MIRROR OF ABOVE CODE FOR RIGHT SUBTREE
    # Note that we reach here only when node was not found
    # in left subtree
    dright = printkDistanceNode(root.right, target, k)
    if dright != -1:
        if dright + 1 == k:
            print(root.data)

        else:
            printkDistanceNodeDown(root.left, k - dright - 2)
        return 1 + dright

    # If target was neither present in left nor in right subtree
    return -1


# Driver program to upload above function
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
target = root.left.right
printkDistanceNode(root, target, 2)
