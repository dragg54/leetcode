def postorder_transversal(root):
    stack = [root]
    visited = [False]
    res = []
    while stack:
        cur, v = stack.pop(), visited.pop()
        if cur:
            if v:
                res.append(cur.val)
            else:
                stack.append(cur)
                visited.append(True)
                stack.append(cur.right)
                visited.append(False)
                stack.append(cur.left)
                visited.append(True)
    return res