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


def build_tree(in_order, post_order):
    if not in_order or not post_order:
        return None

    if len(post_order) == 1:
        return Node(post_order[-1])

    root = Node(post_order[-1])
    root_index = in_order.index(root.data)
    root.left = build_tree(in_order[:root_index], post_order[:root_index])
    root.right = build_tree(in_order[root_index + 1:], post_order[root_index: -1])

    return root


post_order_lst = [9, 1, 2, 12, 7, 5, 3, 11, 4, 8]
in_order_lst = [9, 5, 1, 7, 2, 12, 8, 4, 3, 11]

tree = build_tree(in_order_lst, post_order_lst)
print("--IN--")
in_order_traversal(tree)
# print("--PRE--")
# pre_order_traversal(tree)
print("--POST--")
post_order_traversal(tree)
