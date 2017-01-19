"""
STATEMENT
Given a positive integer, output its complement number.
The complement strategy is to flip the bits of its binary representation.

CLARIFICATIONS
- The numbers are 32-bit binary number? Yes.
- No leading zeros in the binary representation? Yes.

EXAMPLES
5 (101) -> 2 (010)

COMMENTS
- We can do string manipulation with linear space and time complexity.
- Bit manipulation is the expected way, I guess using left shift.
"""

def findComplement(num):
        """
        :type num: int
        :rtype: int
        """
        bin_num = bin(num)[2:]
        to_return = ""
        for c in bin_num:
            to_return += str(abs(int(c)-1))
        return int(to_return,2)
