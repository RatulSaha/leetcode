"""
STATEMENT
Given a binary tree, flatten it to a linked list in-place.

CLARIFICATIONS
- Does the order in the linked list matter? Technically it should not, but
  leetcode OJ cares about a DFS-oriented order.

EXAMPLES
(needs to be drawn)

COMMENTS
- We run a vanilla DFS and store all the values in a list.
- Then we reconstruct the tree in-place.
- Both time and space complexity are linear in size of the tree.
"""

def flatten(root):
      """
      :type root: TreeNode
      :rtype: void Do not return anything, modify root in-place instead.
      """
      if root is None:
          return
      stack, visited = deque(), []
      stack.appendleft(root.right)
      stack.appendleft(root.left)
      while stack:
          node = stack.popleft()
          if node is None:
              continue
          stack.appendleft(node.right)
          stack.appendleft(node.left)
          visited.append(node.val)
      root.left = None
      curr = root
      for val in visited:
          curr.right = TreeNode(val)
          curr = curr.right
