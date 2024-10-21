class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxLen = 0

        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            self.maxLen = max(self.maxLen, left_height + right_height)
            
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.maxLen
