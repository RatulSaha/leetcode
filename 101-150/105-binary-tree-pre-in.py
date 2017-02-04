"""
STATEMENT
Given preorder and inorder traversal of a tree, construct the binary tree.

CLARIFICATIONS
- Can I assume that duplicates do not exist? Sure.
- Can we use Python's loosely typed nature? Then we can make it recursive. Sure.

EXAMPLES
(needs to be drawn)

COMMENTS
- The base case is when both the list is empty. Then it returns None.
- The first element of the preorder is the root.
- We can find the root in the inorder list (using the no-duplicate policy).
- Then inorder of the left (right) subtree are the left (right) part of the inorder list.
- Similarly, we can find the preorder of the left and right subtree.
- The time complexity is O(n^2), for heavily left-skewed trees.
"""

def buildTree(preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        root_val_index = inorder.index(root_val)
        root = TreeNode(root_val)
        pre_left = preorder[1:root_val_index+1]
        pre_right = preorder[root_val_index+1:]
        in_left = inorder[:root_val_index]
        in_right = inorder[root_val_index+1:]
        root.left = buildTree(pre_left, in_left)
        root.right = buildTree(pre_right, in_right)
        return root
