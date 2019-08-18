# Python3 implementation of a O(n) time
# method for spiral order traversal

# A class to create a new node


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printSpiral(root):
    if root is None:
        return  # None check

    # Create two stacks to store
    # alternate levels
    s1 = []  # For levels to be printed
    # from right to left
    s2 = []  # For levels to be printed
    # from left to right

    # append first level to first stack 's1'
    s1.append(root)

    # Keep printing while any of the
    # stacks has some nodes
    while not len(s1) == 0 or not len(s2) == 0:

        # Print nodes of current level from s1
        # and append nodes of next level to s2
        while not len(s1) == 0:
            temp = s1[-1]
            s1.pop()
            print(temp.data, end=" ")

            # Note that is right is appended
            # before left
            if temp.right:
                s2.append(temp.right)
            if temp.left:
                s2.append(temp.left)

        # Print nodes of current level from s2
        # and append nodes of next level to s1
        while not len(s2) == 0:
            temp = s2[-1]
            s2.pop()
            print(temp.data, end=" ")

            # Note that is left is appended
            # before right
            if temp.left:
                s1.append(temp.left)
            if temp.right:
                s1.append(temp.right)

            # Driver Code


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)
    print("Spiral Order traversal of binary tree is ")
    printSpiral(root)
