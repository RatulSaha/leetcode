"""
STATEMENT
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
The update(i, val) function modifies nums by updating the element at index i to val.

CLARIFICATIONS
- Are these two the only functions available to access/modify the array? Yes.
- How many times would the update and finding sum be called? They can be called the same number of times.
- Is the list sorted? Not necessarily.

EXAMPLES
[1, 3, 5]
sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

COMMENTS
- The usual array has constant time update but O(n) to find the sum.
- We can store another array to indicate the sum till i-th point, then the time complexity
  to update would be linear, but finding sum would be constant. We'd need additional O(n)
  space complexity array.
- We can use binary index tree to do both the operations in O(log n). We'd need additional
  O(n) array, though.
"""

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.arr = nums
        self.size = len(nums)
        self.btree = [0 for _ in range(len(nums)+1)]
        for j in range(len(nums)):
            val = nums[j]
            i = j +1
            while i <= self.size:
                self.btree[i] += val
                i += i&(-i)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.arr[i], diff = val, val- self.arr[i]
        i += 1
        while i <= self.size:
            self.btree[i] += diff
            i += i&(-i)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumTill(j)-self.sumTill(i-1)

    
    def sumTill(self, i):
        i += 1
        to_return = 0
        while i > 0:
            to_return += self.btree[i]
            i -= i&(-i)
        return to_return
