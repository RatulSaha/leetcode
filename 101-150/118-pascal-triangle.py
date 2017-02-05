"""
STATEMENT
Given numRows, generate the first numRows of Pascal's triangle.

CLARIFICATIONS
- Can we assume numRows is positive? Yes.

EXAMPLES
numRows = 5 ->
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

COMMENTS
- The base case is for numRows = 1 and 2.
- Then each row is started and ended with 1, and the rest of the element are sum of consecutive elements
  in the previous row.
- Technically, using a deque would be faster, but for simplicity let's use Python lists and their addition.
"""

def generate(numRows):
      """
      :type numRows: int
      :rtype: List[List[int]]
      """
      if not numRows:
          return []
      if numRows == 1:
          return [[1]]
      to_return = [[1],[1,1]]
      for row in range(2, numRows):
          last_row = to_return[-1]
          to_return.append([1]+[last_row[i]+last_row[i+1] for i in range(len(last_row)-1)]+[1])
      return to_return
