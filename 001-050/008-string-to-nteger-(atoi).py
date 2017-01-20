"""
STATEMENT
Implement atoi to convert a string to an integer.

CLARIFICATIONS
- Is there some basic conditions, such as how to
  handle whitespaces or non-digit characters? Ignore all whitespaces at start,
  then get the number and ignore the rest.
- What should the output for a string that is not an integer? Return 0.
- Should we assume the integer is 32 bit? Yes, for outside range, return 0.

EXAMPLES
"213" -> 213
"-1.6" -> -2
"0" -> 0
"112aeqwe" -> 112

COMMENTS
- The number can be negative.
- It can be a float, if the first digit after the point is more than or equal 5,
  the output would be incremented.
"""

def myAtoi(str):
      """
      :type str: str
      :rtype: int
      """
      to_return_val = 0
      str = str.strip()
      if not str:
          return 0
      n, sign, carry, start = len(str), 1, 0, 0
      if str[0] in ["-", "+"]:
          start = 1
      if str[0] == "-":
          sign = -1

      for i in range(start, n):
          s = str[i]
          if s in "0123456789":
              to_return_val = to_return_val*10 + ord(s)-ord('0')
          elif s == ".":
              if i == n-1:
                  return 0
              else:
                  if str[i+1] in "0123456789" and str[i+1] >= 5:
                      to_return_val += 1
                  break
          else:
              break
      to_return_val = to_return_val*sign
      if to_return_val > 2147483647:
          return 2147483647
      if to_return_val < -2147483648:
          return -2147483648
      return to_return_val
