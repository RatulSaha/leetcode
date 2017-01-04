"""
STATEMENT
Given a complete binary tree, count the number of nodes.

CLARIFICATIONS
- So, I can assume the tree is complete, or have to check for that? You can assume that.
- To reiterate, a complete binary tree only has the last level not filled. The last
  level is filled from the left, if any.

EXAMPLES
(not drawn)

COMMENTS
- We first have to figure out the height h of the tree. We can do that going as far left
  down as we can.
- Then, the leaves can be counted separately, given the height.
"""

def countNodes(root):
  """
  :type root: TreeNode
  :rtype: int
  """
  if not root:
      return 0
  level = root
  height = 0
  while level.left != None:
      height += 1
      level = level.left
  if not height:
      return 1
  return (2**(height))-1 + _countLeaves(root, height)

def _countLeaves(root, height):
  if height == 0:
      return 0

  h, level = height, root
  while level.left != None:
      h -= 1
      level = level.left
  if h:
      return 0

  h, level = height, root
  while level.right != None:
      h -= 1
      level = level.right
  if not h:
      return 2**height

  level, h = root.left, height-1
  if level == None:
      return 1
  while level.right != None:
      h -= 1
      level = level.right
  if not h:
      return 2**(height-1) + _countLeaves(root.right, height-1)
  else:
      return _countLeaves(root.left, height-1)
