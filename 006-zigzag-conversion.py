"""
STATEMENT
Given a string and a number of rows, pring the string in a zigzag fashion across rows.

"PAYPALISHIRING" can be written as the following in 3 rows:
P   A   H   N
A P L S I I G
Y   I   R

CLARIFICATIONS
- Can I assume row number to be positive? Yes.
- For row number 1, it prints the identical string, right? Yes.

EXAMPLES
The given example looks OK to begin with.

COMMENTS
- We can initiate the rows as list of empty strings.
- We divide the given string in number of rows, and then print them with alternating direction in the rows.
- O(n) time complexity and (technically) O(n) space complexity.
- Our solution may involve slicing strings, which are technically in order of size of the string, but let's not worry about that right now.
  Python optimizes string slicing pretty well.
"""

def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (len(s)<=1):
            return s
        if (numRows <= 1):
            return s
        rows = ["" for i in range(numRows)]
        rows[0] = s[0]
        chunkStrings = [ s[i:i+numRows-1] for i in range(1, len(s), numRows-1) ]
        direction = 1 #true is forward
        for chunk in chunkStrings:
            if (direction==1):
                for i in range(1,numRows):
                    if chunk:
                        rows[i] += chunk[0]
                        chunk = chunk[1:]
            else:
                for i in range(numRows-2, -1, -1):
                    if chunk:
                        rows[i] += chunk[0]
                        chunk = chunk[1:]
            direction = direction*(-1)
        return ''.join(rows)
