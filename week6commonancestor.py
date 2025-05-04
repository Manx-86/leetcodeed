class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left_sub = self.lowestCommonAncestor(root.left, p, q)
        right_sub = self.lowestCommonAncestor(root.right, p, q)
        if left_sub and right_sub:
            return root
        return left_sub or right_sub
