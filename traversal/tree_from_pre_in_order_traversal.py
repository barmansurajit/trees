class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(f"{root.data}")
        in_order_traversal(root.right)


def pre_order_traversal(root):
    if root:
        print(f"{root.data}")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(f"{root.data}")


def build_tree(in_order, pre_order) -> Node:

    if not in_order or not in_order:
        return None

    if len(pre_order) == 1:
        return Node(pre_order[0])

    root = Node(pre_order[0])
    root_index = in_order.index(root.data)
    root.left = build_tree(in_order[:root_index], pre_order[1: root_index + 1])
    root.right = build_tree(in_order[root_index + 1:], pre_order[root_index + 1:])

    return root


# in_order_lst = ['D', 'B', 'E', 'A', 'F', 'C']
# pre_order_lst = ['A', 'B', 'D', 'E', 'C', 'F']
in_order_lst = [9, 1, 2, 12, 7, 5, 3, 11, 4, 8]
pre_order_lst = [9, 5, 1, 7, 2, 12, 8, 4, 3, 11]

tree = build_tree(in_order_lst, pre_order_lst)
print("--IN--")
in_order_traversal(tree)
print("--PRE--")
pre_order_traversal(tree)
print("--POST--")
post_order_traversal(tree)
