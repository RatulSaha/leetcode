"""
STATEMENT
Given a binary array, find the maximum number of consecutive 1s in this array.

CLARIFICATIONS
- Reiterating, the items in the array can only be 0 and 1? Yes.

EXAMPLES
[1,1,0,1,1,1] -> 3

COMMENTS
- This is similar to maximum sum subarray problem, and a variation of Kadane's algorithm can be used.
- We can keep a global max and a local max and reset the local max each time we hit a zero.
"""

def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        local_max, global_max = 0, 0
        for num in nums:
            if num == 0:
                global_max = max(global_max, local_max)
                local_max = 0
            else:
                local_max += 1
        return max(global_max, local_max)
