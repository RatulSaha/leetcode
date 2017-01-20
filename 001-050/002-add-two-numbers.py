"""
STATEMENT
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

CLARIFICATIONS
- Can there be leading zeros? No, except the number zero.
- I am confirming that the number of digits in the two numbers can be different? Yes.

EXAMPLES
(2 -> 4 -> 3), (5 -> 6 -> 4) -> 7 -> 0 -> 8

COMMENTS
- Since the numbers are given in reverse order, we only have to iterate the two linked lists and 
  accumulate the result in a new linked list.
- We should remember the carry.
- If one of the numbers end early, we should add the rest of the unfinished number added to the carry.
- O(m+n) time complexity and O(m+n) space complexity, where m and n are number of digits in the given numbers.
"""

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    to_return, carry = ListNode(0), 0
    to_return_head = to_return
    num1_p, num2_p = l1, l2
    while (num1_p is not None) and (num2_p is not None):
        to_add_val = num1_p.val + num2_p.val + carry
        if to_add_val >= 10:
            carry = 1
            to_add_val %= 10
        else:
            carry = 0
        to_return.next = ListNode(to_add_val)
        to_return = to_return.next
        num1_p, num2_p = num1_p.next, num2_p.next
    while num1_p is not None:
        to_add_val = num1_p.val + carry
        if to_add_val >= 10:
            carry = 1
            to_add_val %= 10
        else:
            carry = 0
        to_return.next = ListNode(to_add_val)
        to_return, num1_p = to_return.next, num1_p.next

    while num2_p is not None:
        to_add_val = num2_p.val + carry
        if to_add_val >= 10:
            carry = 1
            to_add_val %= 10
        else:
            carry = 0
        to_return.next = ListNode(to_add_val)
        to_return, num2_p = to_return.next, num2_p.next
    if carry:
        to_return.next = ListNode(1)
    return to_return_head.next
