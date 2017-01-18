"""
STATEMENT
The string S consisting of only '1' and '2' is magical because concatenating the number of
contiguous occurrences of characters '1' and '2' generates the string S itself.
The first few elements of string S is the following: S = "1221121221221121122..."
Given an integer N as input, return the number of '1's in the first N number in the magical string S.

CLARIFICATIONS
- Do we assume that the string S starts as given? Yes.

EXAMPLES
6 (S=12211) => 3

COMMENTS
- We should keep generating the string S till length n, and keep an index to keep 
  track of the item that represents the subarray at the end of S currently.
- Since we may end up generating a little more than n, we should count the number of
  1s carefully.
"""

def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        if n <= 3:
            return 1
        s = "122"
        len_so_far, index = 3, 2
        while len_so_far <= n:
            curr_val = int(s[index])
            if s[-1] == "2":
                s += "1"*curr_val
            else:
                s += "2"*curr_val
            index += 1
            len_so_far += curr_val
        
        to_return = 0
        for i in range(n):
            if s[i] == '1':
                to_return += 1
        return to_return
