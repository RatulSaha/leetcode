"""
STATEMENT
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

CLARIFICATIONS
- Do I return the subarray or the maximum product? Maximum product is fine.
- Can the list be empty? No.

EXAMPLES
[2,3,-2,4] -> 6 ([2,3])

COMMENTS
- This is similar to the Kadane's algorithm for maximum sum subarray.
- In this case, we need to keep two local variables, min and max.
- O(n) time complexity and constant space complexity.
"""

def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far=big=small=nums[0]
        len_nums = len(nums)
        for i in range(1, len_nums):
            n = nums[i]
            big,small = max(n,n*big,n*small), min(n,n*big,n*small)
            max_so_far = max(big,max_so_far)
        return max_so_far
