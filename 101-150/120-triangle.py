"""
STATEMENT
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

CLARIFICATIONS
- Starting with a single-element row, at each row, the number of elements increase by one? Yes.
- The adjacent of the jth element in the ith row are jth and (j+1)th elements in the (i+1)th row?

EXAMPLES
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
] ->
11 (because: 2 + 3 + 5 + 1 = 11)

COMMENTS
- We recursively compute the minimum path sum from each element to the bottom.
- We compute that starting from the bottom and store the results in a cache.
- The cache is initiated with the last array (that's the sum from an element in the last array
  to reach the last array).
- Then, we can use this linear space to compute for the rest of the elements.
- At the end, the first element in the cache would be the result.
"""

def minimumTotal(triangle):
      """
      :type triangle: List[List[int]]
      :rtype: int
      """
      if not triangle:
          return 0
      n = len(triangle)
      current_cache = triangle[-1]

      for i in range(n-2, -1, -1):
          for j in range(i+1):
              current_cache[j] = triangle[i][j] + min(current_cache[j], current_cache[j+1])

      return current_cache[0]
