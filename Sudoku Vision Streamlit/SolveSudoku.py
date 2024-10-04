# Function for a Sudoku Solver using backtracking algorithm that takes in an array of 9x9 integers and returns a 9x9 array of integers

def SolveSudoku(board):
    """
    Takes in a 9x9 array of integers of Unsolved Sudoku Puzzle and returns a 9x9 array of integers of Solved Sudoku Puzzle

    Parameters:
    board (list): A 9x9 array of integers where 0 represents an empty cell

    Returns:
    list: A 9x9 array of integers where each row and column of the 9x9 array contains all integers from 1 to 9 without repetition
    """
    def is_valid(row, col, num):
        """
        Checks if the number is valid to be placed in the cell
        
        Parameters:
        row (int): The row index of the cell
        col (int): The column index of the cell
        num (int): The number to be placed in the cell
        
        Returns:
        bool: True if the number is valid to be placed in the cell, False otherwise
        """

        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve():
        """
        Solves the Sudoku Puzzle using backtracking algorithm

        Returns:
        bool: True if the Sudoku Puzzle is solved, False otherwise
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(i, j, num):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = 0
                    return False
        return True

    solve()
    return board
