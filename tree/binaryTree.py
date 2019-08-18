class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


def create_binary_tree(arr, start, end):
    if start > end:
        return None
    middle = start + (end - start) // 2
    root = Node(arr[middle])
    root.left = create_binary_tree(arr, start, middle - 1)
    root.right = create_binary_tree(arr, middle + 1, end)
    return root


def traverse_in_order(root):
    if root is None:
        return

    traverse_in_order(root.left)
    print(root.value)
    traverse_in_order(root.right)


arr_example = [20, 40, 50, 70, 80, 100, 120, 300]

binary_tree = create_binary_tree(arr_example, 0, len(arr_example) - 1)

traverse_in_order(binary_tree)
