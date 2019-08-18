# Python3 program to connect nodes at same
# level using extended pre-order traversal

class newnode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.nextRight = None


# Sets the nextRight of root and calls
# connectRecur() for other nodes
def connect(p):
    # Set the nextRight for root
    p.nextRight = None

    # Set the next right for rest of
    # the nodes (other than root)
    connectRecur(p)


# Set next right of all descendents of p.
# Assumption: p is a compete binary tree
def connectRecur(p):
    # Base case
    if not p:
        return

    # Set the nextRight pointer for p's
    # left child
    if p.left:
        p.left.nextRight = p.right

    # Set the nextRight pointer for p's right
    # child p.nextRight will be None if p is
    # the right most child at its level
    # if p.right:
    #     p.right.nextRight = p.nextRight != (p.nextRight.left != None) ?  p.nextRight.left: p.nextRight.right: None;

    if p.right:
        if p.nextRight:
            p.right.nextRight = p.nextRight if p.nextRight else p.nextRight.left
        else:
            p.right.nextRight = None

    # Set nextRight for other nodes in
    # pre order fashion
    connectRecur(p.left)
    connectRecur(p.right)


# Driver Code
if __name__ == '__main__':

    # Constructed binary tree is
    #	  10
    #	 / \
    #	 8	 2
    # /
    # 3
    root = newnode(10)
    root.left = newnode(8)
    root.right = newnode(2)
    root.left.left = newnode(3)
    root.right.right = newnode(11)

    # Populates nextRight pointer in all nodes
    connect(root)

    # Let us check the values of nextRight pointers
    print("Following are populated nextRight",
          "pointers in the tree (-1 is printed",
          "if there is no nextRight)")
    print("nextRight of", root.data, "is ", end="")
    if root.nextRight:
        print(root.nextRight.data)
    else:
        print(-1)
    print("nextRight of", root.left.data, "is ", end="")
    if root.left.nextRight:
        print(root.left.nextRight.data)
    else:
        print(-1)
    print("nextRight of", root.right.data, "is ", end="")
    if root.right.nextRight:
        print(root.right.nextRight.data)
    else:
        print(-1)
    print("nextRight of", root.left.left.data, "is ", end="")
    if root.left.left.nextRight:
        print(root.left.left.nextRight.data)
    else:
        print(-1)

    # This code is contributed by PranchalK
