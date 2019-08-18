max_height = 0


def find_diameter(root):
    if root is None:
        return 0

    left_heigth = find_diameter(root.left)
    right_heigth = find_diameter(root.right)
    diameter = left_heigth + right_heigth
    max_height = max(max_height, diameter)

    return 1 + max(left_heigth, right_heigth)
