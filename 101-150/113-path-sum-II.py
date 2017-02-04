"""
STATEMENT
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

CLARIFICATIONS
- Should I return a list of paths? Yes.
- Does the order of the list of paths matter? No.
- Will each path have to be well-ordered? Yes.

EXAMPLES
(needs to be drawn)

COMMENTS
- We can recursively find if such a path exists, but we need to remember the path so far
  (prefix of a possible path).
- Since there is a unique way to reach a node from the root, for each node at recursion,
  only one path has to be remembered.
- However, since a path and all its prefix has to be remembered, it is not space-efficient.
- We somehow have to remember the path prefix efficiently, a parent relation using Python dictionary
  seems to be possible.
- We have to remember the leaves where a valid path ends, so that at the end, we can simply traverse back
  using the parent relation and get the entire path. Python deque with appendleft would be a good idea to 
  have that path, I can later convert it to a list.
- We also have to do all the recursion in-place in the sense that this parent relation and the set of valid
  leaves have to be built on-the-fly.
"""

def pathSum(root, sum):
      """
      :type root: TreeNode
      :type sum: int
      :rtype: List[List[int]]
      """
      to_return = []
      if root is None:
          return to_return
      parent, leaves = {}, []
      _path_sum_helper(root, sum, parent, leaves)
      for node in leaves:
          path = deque()
          while node in parent:
              path.appendleft(node.val)
              node = parent[node]
          path.appendleft(node.val)
          to_return.append(list(path))
      return to_return

  def _path_sum_helper(node, sum, parent, leaves):
      if node is None:
          return
      if (node.val == sum) and (node.left is None) and (node.right is None):
          leaves.append(node)
          return
      if node.left is not None:
          parent[node.left] = node
      if node.right is not None:
          parent[node.right] = node
      _path_sum_helper(node.left, sum-node.val, parent, leaves)
      _path_sum_helper(node.right, sum-node.val, parent, leaves)
