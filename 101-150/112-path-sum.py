"""
STATEMENT
Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

CLARIFICATIONS
-

EXAMPLES
(needs to be drawn)

COMMENTS
- A recursive solution over the left and right subtree should work.
- The base cases are tricky, since we need to track both None and when the
  sum finishes.
"""

def hasPathSum(root, sum):
      """
      :type root: TreeNode
      :type sum: int
      :rtype: bool
      """
      if root is None and sum is 0:
          return False
      if not root:
          return False
      if (not root.left) and (not root.right) and (root.val == sum):
          return True
      return hasPathSum(root.left, sum-root.val) or hasPathSum(root.right, sum-root.val)
