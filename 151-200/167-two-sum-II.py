"""
STATEMENT
Given an array of integers that is *already sorted* in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
The array indices start with 1, not 0

CLARIFICATIONS
- What happens when there is no solution? Assume solution exists.
- Can the list be empty? No.

EXAMPLES
[2, 7, 11, 15], 9 -> [0,1]
[-2, 1, 2, 3, 4], 3 -> [1,2]
[0, 2, 3, 4], 6   -> [1, 3]
[-3, 3, 4, 90], 0 -> [0, 1]

COMMENTS
- aha! notice that if the list is sorted lowest nums are at beginning, highest numbers are at the end, so you know which direction you need to check if sum is too high or too low
- Use two pointers, one ("low") starts at the beginning of the list, and one starts at the end ("high")
- Sum what's at the two pointers
- if it is too high (greater than target), reduce high's index by 1
- if it is too low (less than target), increase low's index by 1
- if it is the same as target return [low, high]

GOTCHAS
- not 0 indexed so you need to add one to final low and high
"""

def twoSumSorted(nums,target):
	high = len(nums)-1
	low = 0
	while high > low:
		sum = nums[high] + nums[low]
		if sum == target:
			return [low + 1, high + 1]
		elif sum > target:
			high = high - 1
		else: #sum < target
			low = low + 1
