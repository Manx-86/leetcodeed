class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node, depth):
            if node:
                if len(view) == depth:
                    view.append(node.val)
                traverse(node.right, depth + 1)
                traverse(node.left, depth + 1)
            return 
        view = []
        traverse(root, 0)
        return view
