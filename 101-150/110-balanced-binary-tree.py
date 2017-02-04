"""
STATEMENT
Given a binary tree, determine if it is height-balanced.

CLARIFICATIONS
- A height-balanced binary tree is defined as a binary tree in which the depth of the
  two subtrees of every node never differ by more than 1. Yes.

EXAMPLES
(needs to be drawn)

COMMENTS
- Both the left and right subtree has to be height-balanced.
- Also, the max depth of the left and right subtrees can not differ more than one.
"""

def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True
    return (abs(_max_depth(root.left) - _max_depth(root.right)) <= 1) and (isBalanced(root.left)) and (isBalanced(root.right))

def _max_depth(root):
    if root is None:
        return 0
    return 1 + max(_max_depth(root.left), _max_depth(root.right))
