def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
def solve_nq_util(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            print(f"Placing queen at ({i}, {col}):")
            print_board(board)
            print()
            if solve_nq_util(board, col + 1):
                return True
            board[i][col] = 0
            print(f"Removing queen from ({i}, {col}):")
            print_board(board)
            print()
    return False
def solve_nq():
    board = [[0 for _ in range(8)] for _ in range(8)]
    if not solve_nq_util(board, 0):
        print("Solution does not exist")
        return False
    print("Final solution:")
    print_board(board)
    return True
def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
solve_nq()
