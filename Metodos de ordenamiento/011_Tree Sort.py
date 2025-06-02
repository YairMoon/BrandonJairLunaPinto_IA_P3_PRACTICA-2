class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)

def tree_sort(arr):
    if not arr:
        return []
    root = None
    for val in arr:
        root = insert(root, val)
    result = []
    inorder(root, result)
    return result
