"""
STATEMENT
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all the unique triplets.

CLARIFICATIONS
- Do I return tuple of elements of their indexes? Elements.
- The solution may not exist, right? Yes.
- By unique, you mean, each tuple should be considered as set and then unique set of sets? Yes.

EXAMPLES
[-1, 0, 1, 2, -1, -4] ->
[
  [-1, 0, 1],
  [-1, -1, 2]
]

COMMENTS
- We can first try to solve the problem for two elements that add up to a given target.
- Then, we can use that function to solve this for each element in the array.
- We have to be extra careful to make the tuples unique.
- First, we would assume the two_sum function exists already and write that later.
- When we find a valid tuple, we need to sort them to ensure the uniqueness.
- We'd accumulate the tuples in a set, but since lists are mutable, they can't be in a set.
  We can make the valid tuple a string joined by a delimiter, say comma.
"""

def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        to_return = set()
        for i in range(len(nums)):
            target = 0-nums[i]
            start, end = i+1, len(nums)-1
            rest_two = self.twoSum(nums, start, end, target)
            if rest_two:
                for rt in rest_two:
                    valid_tuple = rt+[nums[i]]
                    valid_tuple.sort()
                    valid_tuple = "%s,%s,%s"%(valid_tuple[0], valid_tuple[1], valid_tuple[2])
                    to_return.add(valid_tuple)
        to_return = list(to_return)
        return map(lambda x: self._splitInt(x), to_return)
    
    def _splitInt(self, arr):
        return map(lambda x: int(x), arr.split(','))

    def twoSum(self, nums, start, end, target):
        compl_dict = set()
        to_return = []
        for i in range(start, end+1):
            if nums[i] in compl_dict:
                to_return.append([nums[i], target-nums[i]])
            else:
                compl_dict.add(target-nums[i])
        return to_return
