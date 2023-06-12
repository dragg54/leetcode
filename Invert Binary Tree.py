def invertTree(self, root):
    if not root:
        return None
    tmp = root.left
    root.right = tmp
    root.left = root.right
    self.invertTree(root.right)
    self.invertTree(root.left)
    return root;