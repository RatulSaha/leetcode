"""
STATEMENT
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.

CLARIFICATIONS
- The root is not leaf for trees with levels more than one? Yes.

EXAMPLES
(needs to be drawn)

COMMENTS
- A recursive solution checking the existence left and right subtree should work.
"""

def minDepth(root):
      """
      :type root: TreeNode
      :rtype: int
      """
      if not root:
          return 0
      if not root.left:
          return 1 + minDepth(root.right)
      if not root.right:
          return 1 + minDepth(root.left)
      return 1 + min(minDepth(root.left), minDepth(root.right))
