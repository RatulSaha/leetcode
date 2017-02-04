"""
STATEMENT
Given inorder and postorder traversal of a tree, construct the binary tree.

CLARIFICATIONS
- Can I assume that duplicates do not exist? Sure.
- Can we use Python's loosely typed nature? Then we can make it recursive. Sure.

EXAMPLES
(needs to be drawn)

COMMENTS
- The base case is when both the list is empty. Then it returns None.
- The last element of the postorder is the root.
- We can find the root in the inorder list (using the no-duplicate policy).
- Then inorder of the left (right) subtree are the left (right) part of the inorder list.
- Similarly, we can find the postorder of the left and right subtree.
- The time complexity is O(n^2), for heavily right-skewed trees.
"""

def buildTree(inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder or not inorder:
            return None
        root_val = postorder[-1]
        root_val_index = inorder.index(root_val)
        root = TreeNode(root_val)
        post_left = postorder[:root_val_index]
        post_right = postorder[root_val_index:-1]
        in_left = inorder[:root_val_index]
        in_right = inorder[root_val_index+1:]
        root.left = buildTree(in_left,post_left)
        root.right = buildTree(in_right,post_right)
        return root
