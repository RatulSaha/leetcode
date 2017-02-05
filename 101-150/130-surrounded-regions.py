"""
STATEMENT
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

CLARIFICATIONS
- Should we update the board in-place? Yes.

EXAMPLES
X X X X
X O O X
X X O X
X O X X
->
X X X X
X X X X
X X X X
X O X X

COMMENTS
- A possible region is not surrounded if it "leaks" to the boundary.
- Hence, we start with the boundary "O" values, and then traverse the board using
  DFS to find all "O" values that are not surrounded.
- Then, in one pass, we convert all "O"s that are surrounded, using the previously
  built set of "O"s that should not be converted.
"""

def solve(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    if not board:
        return
    m, n = len(board), len(board[0])
    if m < 3 or n < 3:
        return
    boundary_bad = set()
    for i in range(m):
        if board[i][0] == 'O':
            boundary_bad.add((i,0))
        if board[i][n-1] == 'O':
            boundary_bad.add((i,n-1))

    for j in range(n):
        if board[0][j] == 'O':
            boundary_bad.add((0,j))
        if board[m-1][j] == 'O':
            boundary_bad.add((m-1,j))

    insider_bad = set()
    for boundary_bad_point in boundary_bad:
        visited, stack = set(), [boundary_bad_point]
        while stack:
            point = stack.pop(0)
            for neigh_point in _neighbors(point, board, m, n):
                if neigh_point not in visited and neigh_point not in insider_bad:
                    stack.append(neigh_point)
                    insider_bad.add(neigh_point)
                visited.add(neigh_point)

    for i in range(1, m-1):
        for j in range(1, n-1):
            if (i,j) not in insider_bad:
                board[i][j] = 'X'

def _neighbors((i,j), board, m, n):
    possible_neighbors = [(i+1,j), (i-1,j), (i,j-1), (i,j+1)]
    return [(i,j) for (i,j) in possible_neighbors if i >= 0 and j >= 0 and i < m and j < n and board[i][j] == 'O']
