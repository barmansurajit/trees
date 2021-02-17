class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


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


# tree_root = Node(10)
# tree_root.insert(20)
# tree_root.insert(5)
# # tree_root.left = Node(2)
# # tree_root.right = Node(3)
# # tree_root.left.left = Node(4)
# # tree_root.left.right = Node(5)
# print("--PRE--")
# pre_order_traversal(tree_root)
# print("--IN--")
# in_order_traversal(tree_root)
# print("--POST--")
# post_order_traversal(tree_root)
