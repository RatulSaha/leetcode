"""
STATEMENT
Given an index k, return the kth row of the Pascal's triangle.

CLARIFICATIONS
- Can we assume numRows is positive? Yes.

EXAMPLES
k = 3 -> [1,3,3,1]]

COMMENTS
- The base case is for numRows = 1 and 2.
- Then each row is started and ended with 1, and the rest of the element are sum of consecutive elements
  in the previous row.
- Technically, using a deque would be faster, but for simplicity let's use Python lists and their addition.
"""

def getRow(rowIndex):
      """
      :type rowIndex: int
      :rtype: List[int]
      """
      if rowIndex == 0:
          return [1]
      if rowIndex == 1:
          return [1,1]
      current_row = [1,1]
      for i in range(rowIndex-1):
          next_row = [1]+[current_row[i]+current_row[i+1] for i in range(len(current_row)-1)]+[1]
          current_row = next_row
      return current_row
