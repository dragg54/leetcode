class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val


def dfs(root, n):
    if not root:
        return False
    if root.val == n:
        return True
    return dfs(root.left, n) or dfs(root.right, n)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
b.right = d
b.left = c
a.right = e



def diameterOfBst(root):
    res = [0]
    def dfs(root):
        if not root:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)
        res[0] = max(res[0], 2 + left + right)
        return 1 + max(left, right)
    dfs(root)
    return res[0]

print(diameterOfBst(a))