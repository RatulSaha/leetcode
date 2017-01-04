"""
STATEMENT
Given a string, find the length of the longest substring without repeating characters.

CLARIFICATIONS
- Contiguous substring, not subsequence, right? Yes. 
- Can the string be empty ? Yes.

EXAMPLES
"abcabcbb" -> 3 ("abc", starts at first)
"bbbbb" -> 1 ("b", single element substring)
"pwwkew" -> 3 ("wke", starts at middle)

COMMENTS
- We can keep a window of substring and grow/shrink it.
- The characters in the current string have to be remembered, set is good for that.
  Fast lookup, decent removal in size of the substring size.
- O(n) time complexity and O(n) space complexity.
- To do with constant space complexity, we may have to move to O(n^2) time complexity, by naively looking at every (i,j) position
  to check if that is a valid substring.
"""

def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        start, end = 0, 0
        current_set = set()
        to_return = 0
        for ch in s:
            if ch not in current_set:
                current_set.add(ch)
            else:
                to_return = max(to_return, end-start)
                while s[start] != ch:
                    current_set.remove(s[start])
                    start += 1
                start += 1
            end += 1
        to_return = max(to_return, end-start)
        return to_return
