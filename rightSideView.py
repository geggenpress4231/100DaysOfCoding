#bfs- level nodes for each level -levellength -1 th element
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        queue = []
        result = []
        
        queue.append(root)
        
        while len(queue) > 0:
            level_size = len(queue)
            level_nodes = []
            
            for i in range(level_size):
                node = queue.pop(0)
                
                # Add the last node at this level to the result (rightmost node)
                if i == level_size - 1:
                    result.append(node.val)
                
                # Enqueue left and right children of the current node
                if node.left is not None:
                    queue.append(node.left)
                
                if node.right is not None:
                    queue.append(node.right)
        
        return result
