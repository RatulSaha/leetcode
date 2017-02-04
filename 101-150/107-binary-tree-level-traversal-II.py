"""
STATEMENT
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

CLARIFICATIONS
- Do we print all 'None' values that a level may have? Yes.

EXAMPLES
[3,9,20,null,null,15,7] -> [[15,7],[9,20],[3]]

COMMENTS
- The usual tree level traversal would work
  (https://github.com/RatulSaha/leetcode/blob/master/101-150/102-binary-tree-level-order-reversal.py).
- We can use deque from collections module to do appendleft instead of append.
"""

def levelOrderBottom(root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        to_return = []
        if not root:
            return to_return
        level = [root]
        while level:
            current_level_val = [node.val for node in level]
            to_return = [current_level_val] + to_return
            next_level = []
            for node in level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            level = next_level
        return to_return
