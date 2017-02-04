"""
STATEMENT
Given an array S integers and a target, find all unique quadruplets a, b, c, and d in S such that a + b + c + d = target.

CLARIFICATIONS
- Similar clarifications as 015-3sum.

EXAMPLES
[1, 0, -1, 0, -2, 2], 0 =>

[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

COMMENTS
- We keep a dictionary of possible sum and their indices.
- Then we do nested iteration to find the rest two values.
- The time complexity is O(n^2), probably O(n^3), when the complementary set is in order of n.
"""

from collections import defaultdict
def fourSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
    		return []
    	n = len(nums)
    	to_return = set()
    	two_dict = defaultdict(set)
    	for i in range(n):
    		for j in range(i+1, n):
    			sum_val = nums[i]+nums[j]
    			two_dict[target-sum_val].add((i,j))
    
    	for i in range(n):
    		for j in range(i+1, n):
    			sum_val = nums[i]+nums[j]
    			if sum_val in two_dict:
    				compl_set = two_dict[sum_val]
    				for (compl_i, compl_j) in compl_set:
    					if not (set([compl_i, compl_j]) & set([i,j])):
    						to_add = [nums[i],nums[j],nums[compl_i],nums[compl_j]]
    						to_add.sort()
    						to_add = ','.join([str(x) for x in to_add])
    						to_return.add(to_add)
    	return [map(lambda x: int(x), x.split(',')) for x in to_return]
