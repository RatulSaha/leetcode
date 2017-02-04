"""
STATEMENT
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

CLARIFICATIONS
- Do we print all 'None' values that a level may have? Yes.

EXAMPLES
[3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]

COMMENTS
- We remember the current level of nodes, the next level of nodes and the values of the current level of nodes.
- Then, we update the level with the next level and keep going until the level is empty.
- The time complexity is linear in the number of nodes while the space complexity is linear
  in the maximum size of the levels (which can essentially be the number of nodes).
"""

def levelOrder(root):
      """
      :type root: TreeNode
      :rtype: List[List[int]]
      """
      to_return = []
      if not root:
          return to_return
      level = [root]

      while level:
          next_level, current_level_val = [], []
          for node in level:
              if node is not None:
                  current_level_val.append(node.val)
                  next_level.append(node.left)
                  next_level.append(node.right)
          level = next_level
          if current_level_val:
              to_return.append(current_level_val)
      return to_return
