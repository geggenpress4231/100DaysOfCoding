# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:  # Added 'self' here
        def helper(node):
            nonlocal max_sum
            if not node:
                return 0
            
            # Traverse left and right subtrees first (postorder traversal)
            left_gain = max(helper(node.left), 0)
            right_gain = max(helper(node.right), 0)
            
            # The maximum path sum through this node (includes both left and right)
            current_max_path = node.val + left_gain + right_gain
            
            # Update the global maximum path sum
            max_sum = max(max_sum, current_max_path)
            
            # Return the max sum that includes this node and either left or right path
            return node.val + max(left_gain, right_gain)
        
        max_sum = float('-inf')
        helper(root)
        return max_sum
