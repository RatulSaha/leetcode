"""
STATEMENT
Reverse digits of an integer.

CLARIFICATIONS
- I am assuming the number can be negative? Yes.
- Do I have to handle 32-bit interger overflow? Yes, return 0 in that case.
- Can I convert the interger to string first (easier to reverse)? Sure.
- Are leading zeros OK? No.

EXAMPLES
123 -> 321
-123 -> -321

COMMENTS
- We can convert the absolute value of the integer to string and then reverse the string.
- We have to be careful about adding the sign of the string back after conversion.
- O(n) time complexity and O(n) space complexity.
- Constant space complexity means doing it in-place, which is not obvious to me.
- Python allows 64-bit integers, so we need to mimic 32-bit integer overflow.
"""

def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        if (x<0):
                x = abs(x)
                neg = -1
        else:
                neg = 1

        rev_x = int(str(x)[::-1])
        if abs(rev_x) < 2147483648:
                return rev_x*neg
        else:
                return 0
