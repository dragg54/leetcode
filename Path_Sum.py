class Solution:
    def pathSum(self, root, target):
        def dfs(node, curSum):
            if not node:
                return False
            curSum += node.val
            if not node.right and not node.left:
                return curSum == target
            return(dfs(node.left, curSum) or dfs(node.right, curSum))
        return dfs(root, 0)