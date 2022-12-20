

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # root is empty return None
    if not root or root in [p, q]:
        return root

    left_res = lowestCommonAncestor(root.left, p, q)
    right_res = lowestCommonAncestor(root.right, p, q)

    # if left_res == p and right_res == q, return root
    if left_res and right_res:
        return root
    else:
        return left_res or right_res