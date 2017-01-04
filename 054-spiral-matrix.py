"""
STATEMENT
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

CLARIFICATIONS
- So, we start from top left and go clockwise? Yes.

EXAMPLES
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
] => [1,2,3,6,9,8,7,4,5]

COMMENTS
- A spiral is determined by the corners, or where it takes right turn. We could keep the width and height too,
  but let's go with stops. Should be easier to maintain and sanity check.
- We still have to keep track of the width and height for stopping criteria (<=1).
"""

def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        to_return = []

        start = (0,0)
        stop1, stop2, stop3 = (0,n-1), (m-1,n-1), (m-1,0)
        width, height = n, m
        while width > 1 and height > 1:
            i,j = start
            while (i,j) != stop1:
                to_return.append(matrix[i][j])
                j += 1
            while (i,j) != stop2:
                to_return.append(matrix[i][j])
                i += 1
            while (i,j) != stop3:
                to_return.append(matrix[i][j])
                j -= 1
            while (i,j) != start:
                to_return.append(matrix[i][j])
                i -= 1
            start = (start[0]+1, start[1]+1)
            stop1 = (stop1[0]+1, stop1[1]-1)
            stop2 = (stop2[0]-1, stop2[1]-1)
            stop3 = (stop3[0]-1, stop3[1]+1)
            width -= 2
            height -= 2
        if width == 1:
            i,j = start
            i_end = stop2[0]
            while i <= i_end:
                to_return.append(matrix[i][j])
                i += 1
            return to_return
        if height == 1:
            i,j = start
            j_end = stop1[1]
            while j <= j_end:
                to_return.append(matrix[i][j])
                j += 1
            return to_return
        return to_return
