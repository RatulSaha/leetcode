"""
STATEMENT
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
Find the total sum of all root-to-leaf numbers.

CLARIFICATIONS
- The binary tree can be of an arbitrary structure? Yes.
- Should we return 0 in case the tree is empty? Yes.
- Do I consider when the sum may overflow (less concern in Python, though)? No.

EXAMPLES
A tree with root value 1 and two leaves 2 and 3 -> 25 (because 12+13 = 25).

COMMENTS
- One way would be to traverse the tree with something like DFS and get all possible root-to-leaf paths and add the
  corresponding numbers. However, same nodes will be stored over and over (for example, the root will be stored
  for each path).
- Instead, we can traverse the tree and build a parent relation, while noting down the leaves. The values in leaves
  are the unit's place in the corresponding numbers.
- We can then traverse back using the parent relation and add to the sum similar to the way one calculates sum of a
  number of digits by hand, starting from the unit's digit.
"""


def sumNumbers(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None: return 0
    parent, leaves = {}, []
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left is None and node.right is None:
            leaves.append(node)
            continue
        if node.left is not None:
            parent[node.left] = node
            stack.append(node.left)
        if node.right is not None:
            parent[node.right] = node
            stack.append(node.right)
    to_return, carry, i = 0, 0, 0
    while leaves:
        to_add = sum([node.val for node in leaves]) + carry
        carry, digit = divmod(to_add, 10)
        to_return += digit*(10**i)
        leaves = [parent[node] for node in leaves if node in parent]
        i += 1
    to_return += carry*(10**i)
    return to_return
