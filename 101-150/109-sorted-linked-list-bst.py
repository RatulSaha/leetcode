"""
STATEMENT
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

CLARIFICATIONS
- Can we assume that there is no duplicate element in the list? Sure.

EXAMPLES
(needs to be drawn)

COMMENTS
- We can do it similar to the array version, except we need to remember the size of the
  linked list under consideration.
- We use a helper function that takes the head and the supposed size of the array and
  recursively builds the tree.
- The base case is for n<2.
"""

def sortedListToBST(head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    if head is None:
        return None
    curr = head
    n = 1
    while curr.next is not None:
        curr = curr.next
        n += 1
    return _sorted_list_BST(head,n)

def _sorted_list_BST(head, n):
    if not n:
        return None
    if n == 1:
        return TreeNode(head.val)
    curr = head
    m = n/2
    for _ in range(m):
        curr = curr.next
    root = TreeNode(curr.val)
    root.left = _sorted_list_BST(head,m)
    if not n%2:
        m = n/2-1
    root.right = _sorted_list_BST(curr.next,m)
    return root
