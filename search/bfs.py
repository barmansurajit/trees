class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


def level_order(root: TreeNode):
    result = []
    queue = [root]
    while len(queue) != 0:
        node = queue.pop(0)
        result.append(node.data)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return result


if __name__ == '__main__':
    r = TreeNode(3)
    binary_insert(r, TreeNode(9))
    binary_insert(r, TreeNode(20))
    binary_insert(r, TreeNode(15))
    binary_insert(r, TreeNode(7))

    print(level_order(r))
