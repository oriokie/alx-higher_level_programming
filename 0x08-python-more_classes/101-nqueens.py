#!/usr/bin/python3

"""
N Queens puzzle module
"""
import sys


class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
               self.board[i] - i == col - row or \
               self.board[i] + i == col + row:
                return False
        return True

    def solve_nqueens(self, row):
        if row == self.n:
            self.print_solution()
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.solve_nqueens(row + 1)

    def print_solution(self):
        result = [[i, self.board[i]] for i in range(self.n)]
        print(result)


def nqueens_main(n):
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(n)
    solver.solve_nqueens(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens_main(sys.argv[1])
