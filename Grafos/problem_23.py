# This problem was asked by Google.

# You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you
#  can walk on.
# Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If
#  there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the
#  board.
# For example, given the following board:
# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7,
#  since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

def min_steps(board, start, end): # DFS
    return _min_steps(board, start, end, {}, 0)

def _min_steps(board, actual, end, vistos, pasos):
    if actual == end:
        return pasos
    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    min_pasos = float("inf")
    for movimiento in movimientos:
        nuevo = (actual[0] + movimiento[0], actual[1] + movimiento[1])
        if (0 <= nuevo[0] < len(board) and
            0 <= nuevo[1] < len(board[0]) and
            not board[nuevo[0]][nuevo[1]] and
            nuevo not in vistos):
            vistos[nuevo] = True
            pasos_actuales = _min_steps(board, nuevo, end, vistos, pasos + 1)
            if pasos_actuales is not None:
                min_pasos = min(min_pasos, pasos_actuales)
            vistos.pop(nuevo)
    if min_pasos == float("inf"):
        board[nuevo[0]][nuevo[1]] = True  # Mark as wall to avoid
        return None
    return min_pasos

from collections import deque
def walkable(board, row, col):
    if row < 0 or row >= len(board):
        return False
    if col < 0 or col >= len(board[0]):
        return False
    return not board[row][col]
def get_walkable_neighbours(board, row, col):
    return [(r, c) for r, c in [
        (row, col - 1),
        (row - 1, col),
        (row + 1, col),
        (row, col + 1)]
        if walkable(board, r, c)
    ]
def shortest_path(board, start, end): # BFS
    seen = set()
    queue = deque([(start, 0)])
    while queue:
        coords, count = queue.popleft()
        if coords == end:
            return count
        seen.add(coords)
        neighbours = get_walkable_neighbours(board, coords[0], coords[1])
        queue.extend((neighbour, count + 1) for neighbour in neighbours
                if neighbour not in seen)

matriz = [
    [False, False, False, False],
    [True, True, False, True],
    [False, False, False, False],
    [False, False, False, False]
]
inicio = (3, 0)  # (fila, columna)
fin = (0, 0)  # (fila, columna)
print(min_steps(matriz, inicio, fin))  # Output: 7