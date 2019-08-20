class Tree:
    def __init__(self, item):
        self.value = item
        self.left = None
        self.right = None


def create_tree_from_level_order(arr, root, i, n):
    if i < n:
        val = arr[i]
        root = Tree(val)
        root.left = create_tree_from_level_order(arr, root.left, 2 * i + 1, n)
        root.right = create_tree_from_level_order(arr, root.right, 2 * i + 2, n)
    return root


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.value, end=" ")
    in_order(root.right)


def do_cal(op1, op2, operator):
    if operator == "/":
        return op1 // op2
    if operator == "*":
        return op1 * op2
    if operator == "+":
        return op1 + op2
    return op1 - op2


def evalExpressionTree(root):
    if root is None:
        return
    # If this is last node in tree then it will be value node
    if root.left is None and root.right is None:
        return int(root.value)
    left = evalExpressionTree(root.left)
    right = evalExpressionTree(root.right)

    # if both left and right node are not None, then this will be operator node
    opr = root.value
    return do_cal(left, right, opr)


# Driver Code
if __name__ == '__main__':
    arr = ['+', '*', '-', '5', '4', '100', '20']
    # arr = ['-', '4', '7']
    n = len(arr)
    root = None
    evalTree = create_tree_from_level_order(arr, root, 0, n)
    in_order(evalTree)
    res = evalExpressionTree(evalTree)
    print(res)
