"""
STATEMENT
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

CLARIFICATIONS
- Can we assume that the node values have a well-defined equals (== in python, say) operator? Yes.

EXAMPLES
[1,2,2,3,4,4,3] -> True
[1,2,2,null,3,null,3] -> False

COMMENTS
- Recursively, we need to check that the left subtree is the mirror of the right subtree.
- Which essentially boils down to the two root values of the subtrees are equal and the right subtree
  of the left is same as the left subtree of the right (and vice versa).
"""

def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True

    if _isMirror(root.left, root.right):
        return True
    else:
        return False

def isMirror(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    if (tree1.val == tree2.val):
        return (_isMirror(tree1.left, tree2.right) and _isMirror(tree1.right, tree2.left))
    return False
