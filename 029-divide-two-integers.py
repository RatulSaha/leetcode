"""
STATEMENT
Divide two integers without using multiplication, division and mod operator.

CLARIFICATIONS
- Do I have to handle 32-bit integer overflow? Yes, return the MAX_INT in that case.
- Can the divisor be zero? Yes, return the MAX_INT.

EXAMPLES
34/3 -> 11

COMMENTS
- This solution is by tusizi in Leetcode (picked up from https://discuss.leetcode.com/topic/8714/clear-python-code)
"""

def divide(dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
    	sign = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        INT_MIN, INT_MAX = -2147483648, 2147483647
	
        if (not divisor) or (dividend < INT_MIN and divisor == -1):
        		return INT_MAX
    	to_return = 0
    	while dividend >= divisor:
    	    temp, i = divisor, 1
    	    while dividend >= temp: 
        		dividend -= temp
        		to_return += i
        		i <<= 1
        		temp <<= 1
    	if not sign:
    		to_return = -to_return
    	return min(max(INT_MIN, to_return), INT_MAX)
