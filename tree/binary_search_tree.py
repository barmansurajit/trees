class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if node.data > root.data:
            if root.right is None:
                root.right = node
            else:
                binary_insert(root.right, node)
        elif node.data < root.data:
            if root.left is None:
                root.left = node
            else:
                binary_insert(root.left, node)


def in_order_print(root):
    if root:
        in_order_print(root.left)
        print(f"{root.data}")
        in_order_print(root.right)


def pre_order_print(root):
    if root:
        print(f"{root.data}")
        pre_order_print(root.left)
        pre_order_print(root.right)


r = Node(3)
binary_insert(r, Node(7))
binary_insert(r, Node(1))
binary_insert(r, Node(5))
binary_insert(r, Node(5))

print("in order:")
in_order_print(r)

print("pre order")
pre_order_print(r)
