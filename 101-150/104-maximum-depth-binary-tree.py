"""
STATEMENT
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down
to the farthest leaf node.

CLARIFICATIONS
- We are not counting a None value to be a node, right? Correct.

EXAMPLES
[3,9,20,null,null,15,7] -> 3

COMMENTS
- We can recursively find the max depth of the left and right subtrees and add 1.
"""

def maxDepth(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(maxDepth(root.left), maxDepth(root.right))
