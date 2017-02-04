"""
STATEMENT
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

CLARIFICATIONS
- Do we print all 'None' values that a level may have? Yes.
- Do we start with left-to-right? Yes.

EXAMPLES
[3,9,20,null,null,15,7] -> [[3],[20,9],[15,7]]

COMMENTS
- We remember the current level of nodes, the next level of nodes and the values of the current level of nodes.
- Then, we update the level with the next level and keep going until the level is empty.
- The only thing is we need to reverse the direction. We can not do that when adding the next nodes,
  so we need to keep a variable to remember direction and then reverse the list of next nodes in
  alternative cases.
"""

def zigzagLevelOrder(root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        to_return = []
        if not root:
            return to_return
        level = [root]
        ltor = True
        while level:
            level_val, next_level = [], []
            for node in level:
                if node:
                    level_val.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
            if not ltor:
                level_val.reverse()
            if level_val:
                to_return.append(level_val)
            level = next_level
            ltor = not ltor
        return to_return
