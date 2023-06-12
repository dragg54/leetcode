class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))


tree = TreeNode(1)
tree.right = 4
tree.right.right = 6
tree.right.right.right = 7
tree.right.left = 5
tree.left.left = 2
tree.left.right = 3
tree.val = 1

solution = Solution()
print(solution.maxDepth(tree.val))