"""
STATEMENT
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

CLARIFICATIONS
- What happens when there is no solution? Assume solution exists.
- Can the list be empty? No.
- Is the list sorted? Not necessarily.

EXAMPLES
[2, 7, 11, 15], 9 -> [0,1]

COMMENTS
- We can 'remember' what we have seen so far in O(n) space complexity using a set.
- Iterate the list and at every step, we can look back and see there is a possible candidate for complement of the current item.
- O(n) time complexity and O(n) space complexity.
- To do without the space complexity, we may have to move to O(n log n) time complexity, by sorting the list
  and then using two pointers from start and end.
"""


def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_dict = {}
        for i in range(len(nums)):
            compl = target-nums[i]
            if compl in hash_dict:
                return [hash_dict[compl], i]
            hash_dict[nums[i]] = i
