class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def has_path_sum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        if sum == root.val and root.left is None and root.right is None:
            return True

        return self.has_path_sum(root.left, sum - root.val) or self.has_path_sum(root.right, sum - root.val)
