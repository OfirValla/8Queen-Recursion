import time


def create_empty_board(size=8):
    board = []
    for row_idx in range(size):
        board.append([])
        for column_idx in range(size):
            board[row_idx].append(0)
    return board


def is_queen_possible(board, row_idx, column_idx):
    # Check for queens in the same row
    for i in range(len(board)):
        if board[row_idx][i] == 1:
            return False

    # Check for queens in the same column
    for i in range(len(board)):
        if board[i][column_idx] == 1:
            return False

    # Check for queens in the diagonal
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:  # If there is no queen in the current cell -> continue
                continue

            if abs(i - row_idx) == abs(j - column_idx):
                return False

    return True


def solve_8_queens(board):
    for row_idx in range(len(board)):
        for column_idx in range(len(board)):
            # If there is a queen in the current cell -> continue
            if board[row_idx][column_idx] == 1:
                continue

            # If we can't place a queen in the current cell -> continue
            if not is_queen_possible(board, row_idx, column_idx):
                continue

            # Place a queen in the current cell
            board[row_idx][column_idx] = 1

            # Try to continue and place the next queen
            solve_8_queens(board)

            # If the number of placed queens equals the number of cells in a row we solved the problem
            if sum(sum(row) for row in board) == len(board):
                return board

            # The current cell is not good for the queen -> reset it
            board[row_idx][column_idx] = 0

    return board


def solve_8_queens_optimized(board, row_idx=0):
    if row_idx == len(board):
        return board

    for column_idx in range(len(board)):
        # If there is a queen in the current cell -> continue
        if board[row_idx][column_idx] == 1:
            continue

        # If we can't place a queen in the current cell -> continue
        if not is_queen_possible(board, row_idx, column_idx):
            continue

        # Place a queen in the current cell
        board[row_idx][column_idx] = 1

        # Try to continue and place the next queen
        solve_8_queens_optimized(board, row_idx + 1)

        # If the number of placed queens equals the number of cells in a row we solved the problem
        if sum(sum(row) for row in board) == len(board):
            return board

        # The current cell is not good for the queen -> reset it
        board[row_idx][column_idx] = 0

    return board


if __name__ == '__main__':
    print("Original function:")
    start_time = time.time()
    result_original = solve_8_queens(create_empty_board(8))
    end_time = time.time()
    for row in result_original:
        for column in row:
            print('Q' if column == 1 else '_', end=' ')
        print()
    print(f"Took: {end_time - start_time} seconds")

    print("\nOptimized function:")
    start_time = time.time()
    result_optimized = solve_8_queens_optimized(create_empty_board(8))
    end_time = time.time()
    for row in result_optimized:
        for column in row:
            print('Q' if column == 1 else '_', end=' ')
        print()
    print(f"Took: {end_time - start_time} seconds")




