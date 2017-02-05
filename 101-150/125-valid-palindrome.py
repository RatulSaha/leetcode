"""
STATEMENT
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

CLARIFICATIONS
- We can assume the characters can be converted into lowercases? Yes.
- is Empty string a valid palindrome? Yes.

EXAMPLES
"A man, a plan, a canal: Panama" -> True
"race a car" -> False

COMMENTS
- We convert the string to a new string ignoring alphanumeric.
- Then we put two pointers at start and end of the string and compare
  each character (lowered) till either the pointers cross path or a mismatch is found.
"""

def isPalindrome(s):
      """
      :type s: str
      :rtype: bool
      """
      s = ''.join(c for c in s if c.isalnum())
      if not s:
          return True
      start, end = 0, len(s)-1
      while (abs(start-end)>1):
          if (s[start].lower() != s[end].lower()):
              return False
          start += 1
          end -= 1
      if (start==end):
          return True
      if ((end-start)==1):
          return s[start].lower()==s[end].lower()
