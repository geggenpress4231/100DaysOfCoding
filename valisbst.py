class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None  # To keep track of the previous node's value in the in-order traversal

        def inorder(node: Optional[TreeNode]) -> bool:
            nonlocal prev  # Use nonlocal to modify the 'prev' variable declared outside the nested function

            if node is None:
                return True  # Base case: an empty node is valid

            # In-order traversal: Check the left subtree
            if not inorder(node.left):
                return False  # If left subtree is invalid, return False immediately

            # Check the current node value
            if prev is not None and node.val <= prev:
                return False  # If the current node is not greater than the previous, it's invalid
            prev = node.val  # Update prev to current node's value

            # In-order traversal: Check the right subtree
            return inorder(node.right)  # No explicit if, directly return the result of the right subtree check

        return inorder(root)  # Start in-order traversal from the root
