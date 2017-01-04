"""
STATEMENT
Given an input string, reverse the string word by word.

CLARIFICATIONS
- Are spaces at the start allowed? No.
- Can words have extra spaces between? Yes, remove them.
- Can we use a ready, in-place reverse() in python? Sure.

EXAMPLES
"the sky is blue" -> "blue is sky the"

COMMENTS
- We can split the list by single spaces, then strip extra spaces at start and end of each word and then join back.
"""

if not s:
            return s
        s = map(lambda x: x.strip(), s.split(' '))
        s = [word for word in s if word]
        s.reverse()
        return ' '.join(s)
