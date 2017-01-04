"""
STATEMENT
Given a list of non negative integers, arrange them such that they form the largest number.

CLARIFICATIONS
- Do I return the integer? No, return it as a string, the interger can be very large.

EXAMPLES
[3, 30, 34, 5, 9] -> "9534330"

COMMENTS
- We can pass the list and insert each element in the to-be-returned list (can be joined later)
  at appropriate place.
- O(n^2) time complexity and O(n) space complexity.
"""

def largestNumber(nums):
    	if not nums:
    		return ""
    	to_return = [str(nums[0])]
    	for i in range(1, len(nums)):
    	    to_insert = str(nums[i])
    	    for j in range(len(to_return)):
    	        n = to_return[j]
    	       # return int(to_insert+n),
    	        if int(to_insert+n) >= int(n+to_insert):
    	            to_return = to_return[:j]+[to_insert]+to_return[j:]
    	            break
            else:
                to_return.append(to_insert)
    	return ''.join(to_return).lstrip('0') or '0'
