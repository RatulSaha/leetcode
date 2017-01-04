"""
STATEMENT
Given an array of words and a length L, format the text such that
each line has exactly L characters and is fully (left and right) justified.

CLARIFICATIONS
- Can we pack as much words as can in a sentence starting from the left? Yes, greedy approach is fine.
- Does the line last has to be taken care of separately? Words can be left-aligned in the last sentence 
  filled with spaces. Yes, that's an edge case (leetcode OJ does this too).
- Can a word length exceed the given length? No.

EXAMPLES
["This", "is", "an", "example", "of", "text", "justification."] ->

[
   "This    is    an",
   "example  of text",
   "justification.  "
]

COMMENTS
- We should keep adding words till the total length of those words (and one space between each two of them) exceeds the given length L.
- If there's extra space left, we should evenly distrubute them between words.
- O(n) time complexity and O(n) space complexity.
- Whether it's the last sentence should be noted with a boolean variable.
  We'd keep a number of variables like word length etc. to minimize number of operations.
"""

def fullJustify(words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        width = maxWidth
        if not words:
            return [""]

        to_return = []
        word_index = 0
        line_width = 0
        line_words = []

        while word_index < len(words):

            temp = line_width + len(line_words)
            if temp-1 == width:
                to_return.append(' '.join(line_words))
                line_width = 0
                line_words = []
                continue
            if temp + len(words[word_index]) <= width:
                line_width += len(words[word_index])
                line_words.append(words[word_index])
                word_index += 1
            else:
                padded_line = _pad_words(line_words, width, line_width, False)
                to_return.append(padded_line)
                line_width = 0
                line_words = []

        if len(line_words) > 0:
            padded_line = _pad_words(line_words, width, line_width, True)
            to_return.append(padded_line)

        return to_return
        
    def _pad_words(line_words, width, line_width, last_line):

    	padding = width-line_width
    	if len(line_words) == 1:
            return line_words[0]+(' '*padding)
        if last_line:
            return ' '.join(line_words) + ' '*(padding-len(line_words)+1)
        min_gap_padding = ' '*(padding/(len(line_words)-1))
        extra_padding_size = padding%(len(line_words)-1)
        for i in range(extra_padding_size):
            line_words[i] += ' '

        return min_gap_padding.join(line_words)
