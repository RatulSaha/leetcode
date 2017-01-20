"""
STATEMENT
Given a string s, find the longest palindromic substring in s.

CLARIFICATIONS
- If there is no palindrome that is more than one character, we can report
  any character? Yes.

EXAMPLES
"babad" -> "bab"
"cbbd" -> "bb"

COMMENTS
- We can keep a cache to store the result for all possible substring.
- Technically, the cache can be a list of list, but since the cache is half filled,
  we can keep a dictionary of dictionaries.
- O(n^2) time complexity and O(n^2) space complexity.
"""

def longestPalindrome(s):
      """
      :type s: str
      :rtype: str
      """
      if not s:
          return ""
      cache = {}
      n = len(s)
      for i in range(n):
          cache[i] = {}
          for j in range(i,n):
              cache[i][j] = 0

      for k in range(n-1):
          cache[k][k] = 1
          if s[k] == s[k+1]:
              cache[k][k+1] = 1
      cache[n-1][n-1] = 1

      for gap in range(2,n):
          start, end = 0, gap
          while end < n:
              if s[start] == s[end] and cache[start+1][end-1]:
                  cache[start][end] = 1
              start += 1
              end += 1

      for gap in range(n-1,-1,-1):
          start, end = 0, gap
          while end < n:
              if cache[start][end]:
                  return s[start:end+1]
              start += 1
              end += 1
