"""
STATEMENT
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord, such that:
(i) Only one letter can be changed at a time, and (ii) each transformed word must exist in
the word list. Note that beginWord is not a transformed word.

CLARIFICATIONS
- Are all words of the same length? You can assume that.
- What should the return value be if there is no such transformation sequence? Return 0.
- Can there be duplicate in the word list? No.
- Are the words only of lowercase letter? Yes.

EXAMPLES
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
-> 5 (because "hit" -> "hot" -> "dot" -> "dog" -> "cog")

COMMENTS
- We can do a BFS using a queue and remembering the path so far, and the first path returned
  would be the shortest path.
- The next set of words in the transformation can be generated from tweaking the word one character
  at a time and checking if that is in the word list.
- Such a BFS, while works, may have room for improvement. The following code times out in leetcode OJ after 21 testcases.
- A clever technique is to do a two-way BFS, that is not presented here
  (https://discuss.leetcode.com/topic/19721/share-my-two-python-solutions-a-very-concise-one-12-lines-160ms-and-an-optimized-solution-100ms).
"""

def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: Set[str]
    :rtype: int
    """

    queue = deque()
    queue.append((beginWord, [beginWord]))
    while queue:
        node, path = queue.popleft()
        for next in self.next_nodes(node, wordList) - set(path):
            if next == endWord:
                return len(path) + 1
            else:
                queue.append((next, path + [next]))
    return 0

def next_nodes(word, word_list):
    to_return = set()
    for w in word_list:
        mismatch_count, w_length = 0, len(w)
        for i in range(w_length):
            if w[i] != word[i]:
                mismatch_count += 1
        if mismatch_count == 1:
            to_return.add(w)
    return to_return
