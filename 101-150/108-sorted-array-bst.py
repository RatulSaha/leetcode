"""
STATEMENT
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

CLARIFICATIONS
- Can we assume that there is no duplicate in the array? Yes.

EXAMPLES
(needs to be drawn)

COMMENTS
- The two base cases are empty list, which transforms into None, and single element list, which
  transforms into a TreeNode.
- Then, recursively, the root is the node with (n/2)th value, and then we can recursively call
  the left and right subtree.
"""

def sortedArrayToBST(nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[n/2])
        root.left = sortedArrayToBST(nums[:n/2])
        root.right = sortedArrayToBST(nums[n/2+1:])
        return root
