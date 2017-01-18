"""
STATEMENT
Given an string (represents a software license key) consisting of alphanumeric and dashes,
where the dashes are possibly misplaced, rewrite the string as group of K characters divided
by new dashes.

CLARIFICATIONS
- Is the number of alphanumeric characters multiple of K? No, the first group may contain
  less than K, but not zero.
- Can the list be empty? No.
- Any lower/uppercase restriction? Assume you have to convert all lowercase to uppercase.

EXAMPLES
S = "2-4A0r7-4k", K = 4 -> "24A0-R74K"
S = "2-4A0r7-4k", K = 3 -> "24-A0R-74K"

COMMENTS
- I should minimize string concatnation, so will use a queue/deque and then join it before returning.
- Iterate the list from end, ignore the dashes, put a fresh dash after each K items.
- We can use the in-built upper() on the whole string, or we can use upper() per character basis, checking
  if they are lower characters using ord().
"""

from collections import deque

def licenseKeyFormatting(self, S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    to_return = deque()
    chunk_size = 0
    for i in range(len(S)-1, -1, -1):
        c = S[i]
        if c == '-':
            continue
        else:
            if chunk_size < K:
                to_return.appendleft(self._uppercase(c))
                chunk_size += 1
            else:
                to_return.appendleft("-")
                to_return.appendleft(self._uppercase(c))
                chunk_size = 1
    return ''.join(to_return)

def _uppercase(self, c):
    if ord('a') <= ord(c) and ord(c) <= ord('z'):
        return c.upper()
    else:
        return c
