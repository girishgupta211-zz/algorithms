# A Binary Tree Node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_diameter = 1

    def diameterOfBinaryTree(self, root: Node) -> int:
        def find_diameter(root):
            # find diameter for each node and check with maximum
            if root is None:
                return 0

            left_heigth = find_diameter(root.left)
            right_heigth = find_diameter(root.right)
            diameter = left_heigth + right_heigth + 1
            self.max_diameter = max(self.max_diameter, diameter)
            return 1 + max(left_heigth, right_heigth)

        find_diameter(root)
        return self.max_diameter - 1


root = Node(5)
root.left = Node(4)
root.left.left = Node(3)
root.left.left.left = Node(-1)
root.right = Node(7)
root.right.left = Node(2)
root.right.left.left = Node(9)
print("Diameter of given binary tree is %d" % (Solution().diameterOfBinaryTree(root)))

# solution = Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Diameter of given binary tree is %d" % (Solution().diameterOfBinaryTree(root)))
