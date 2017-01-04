"""
STATEMENT
Given a list, rotate the list to the right by k places, where k is non-negative.

CLARIFICATIONS
- Is the list given as an array? No, a linked list.
- Each node in the linked list is an object of a custom data structure, right? Yes.
  Define them.
- Can k be more than the length of the list? Sure.
- Do I return the head of the updated list? Yes.

EXAMPLES
1->2->3->4->5->None, 2 => 4->5->1->2->3->NULL

COMMENTS
- If k is much longer than the list length, we should not update the list unneccessarily,
  so k should be updated to the k modulo list length.
- If k is 0, return the original list.
"""

def rotateRight(head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
      if head is None:
    		return head

      temp = head
    	list_length = 1

      while temp.next is not None:
    		temp = temp.next
    		list_length += 1

      k = k%list_length
    	if k == 0:
    		return head

      prev, curr = head, head
    	count = 1

      while count <= k:
    		curr = curr.next
    		count += 1

      while curr.next is not None:
    		prev = prev.next
    		curr = curr.next
    	to_return = prev.next
    	prev.next = None
    	curr.next = head
    	return to_return
