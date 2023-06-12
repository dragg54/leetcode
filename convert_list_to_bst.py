class Solution:
    def listToBst(self, lst):
        def helper(l, r):
            if l > r:
                return None
            m = (l + r)//2
            root = RootNode(lst[m])
            root.left = helper(l, m-1)
            root.right = helper(m+1, r)
            return root
        return helper(0, len(lst)-1)