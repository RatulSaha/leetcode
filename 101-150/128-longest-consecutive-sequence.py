"""
STATEMENT
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

CLARIFICATIONS
- Does longest consecutive mean the order of the elements can be altered? Yes.
- For empty array, we should return 0? Yes.

EXAMPLES
[100, 4, 200, 1, 3, 2] -> 4 (because [1, 2, 3, 4])

COMMENTS
- We can sort the array and use two pointers to determine the longest sequence of consecutive elements.
  It will be O(nlogn) time complexity.
- A clever O(n) time and O(n) space complexity solution
  (thanks to https://discuss.leetcode.com/topic/15383/simple-o-n-with-explanation-just-walk-each-streak)
  is to convert the array into set and for each element in the set, check if it is the start of
  a possible sequence of consecutive elements.

"""

def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    arr_set = set(nums)
    to_return = 0
    for elem in arr_set:
        if elem-1 in arr_set:
            continue
        curr_val, max_streak = elem, 0
        while curr_val in arr_set:
            max_streak += 1
            curr_val += 1
        to_return = max(to_return, max_streak)
    return to_return
