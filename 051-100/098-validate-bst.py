"""
STATEMENT
Given a binary tree, determine if it is a valid binary search tree (BST).

CLARIFICATIONS
- For any root, the max of the left subtree is smaller than the current value and
  the min of the right subtree is bigger than the current value. Yes, and both the
  left and right subtrees are also BST.
- I am assuming the tree nodes are custom data structure? Yes, define it.
- Is an empty tree BST or a single element tree BST? Yes.

EXAMPLES
  1
2
  3
-> True

COMMENTS
- Recursion looks like a possible clean way to start.
- We would assume the finding minimum and maximum in a binary is given, and then write
  them as helper functions.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isValidBST(root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    	if root is None:
    		return True
    
    	if root.left is None and root.right is None:
    		return True

    	if root.left is None:
            temp = root.right
            return isValidBST(root.right) and (root.val < _min_value(root.right))
    
        if root.right is None:
            temp = root.left
            while temp.left is not None:
                temp = temp.left
            return isValidBST(root.left) and (root.val > _max_value(root.left))
        
        return isValidBST(root.left) and isValidBST(root.right) 
               and (root.val < _min_value(root.right)) and (root.val > _max_value(root.left))

def _max_value(root):
    if root.left is None and root.right is None:
        return root.val
    if root.left is None:
        return max(root.val, _max_value(root.right))
    if root.right is None:
        return max(root.val, _max_value(root.left))
    return max(root.val, _max_value(root.left), _max_value(root.right))

def _min_value(root):
    if root is None:
        return -1
    if root.left is None and root.right is None:
        return root.val
    if root.left is None:
        return min(root.val, _min_value(root.right))
    if root.right is None:
        return min(root.val, _min_value(root.left))
    return min(root.val, _min_value(root.left), _min_value(root.right))
