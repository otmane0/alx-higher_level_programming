#!/usr/bin/python3
"""
N queens problem
"""

import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen in a given position"""

    for i in range(row):
        if (board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row):
            return False


def solve_nqueens(board, row, n, solutions):
    """Recursively solve N Queens problem using backtracking"""
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
    else:
        for col in range(n):
            if is_safe(board, row, col, n):

                board[row] = col
                solve_nqueens(board, row + 1, n, solutions)

def print_solutions(n):
    """Print all solutions for N Queens problem"""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [0] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./101-nqueens.py N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        print_solutions(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
