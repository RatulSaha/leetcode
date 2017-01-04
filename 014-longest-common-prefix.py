"""
STATEMENT
Write a function to find the longest common prefix string amongst an array of strings.

CLARIFICATIONS
- What happens when there is no solution? Return empty string.
- Can the list be empty? Yes, return empty string.

EXAMPLES
["ab", "a", "acd", "aaa"] -> "a"
["ab", "c", "acd"] -> ""

COMMENTS
- Since it is talking about prefix, we can keep a single index starting from left and move it as we see a matching prefix in all strings.
- O(n) time complexity and O(n) space complexity to keep the list of characters in current index.
- To do without the space complexity, we have to iterate through the given list and stop when the character in the current index
  does not match. It can be done, but let's do with basic space complexity.
- Reducing time complexity does not seem to be possible, since the list has to be iterated at least once.
"""

def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        index = 0
        to_return = ""
        if not strs:
            return to_return
        while True:
            try:
                result = [str[index] for str in strs]
                if len(set(result)) == 1:
                    to_return += result[0]
                else:
                    return to_return
                index += 1
            except IndexError:
                return to_return
