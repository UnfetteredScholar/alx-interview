#!/usr/bin/env python3
import sys


def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if (
            board[i] == col
            or board[i] == col - (row - i)
            or board[i] == col + (row - i)
        ):
            return False
    return True


def solve_n_queens_util(board, row, N):
    if row == N:
        return 1

    count = 0
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            count += solve_n_queens_util(board, row + 1, N)
            board[row] = -1  # Backtrack
    return count


def print_solution(board, N):
    for i in range(N):
        row_str = ""
        for j in range(N):
            if board[i] == j:
                row_str += "Q "
            else:
                row_str += ". "
        print(row_str.strip())
    print()


def solve_n_queens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    count = solve_n_queens_util(board, 0, N)
    print("Number of solutions:", count)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(N)
