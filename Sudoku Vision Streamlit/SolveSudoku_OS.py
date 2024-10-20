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

    def BT():
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
                            if BT():
                                return True
                            board[i][j] = 0
                    return False
        return True

    def get_constraints(grid):
        """
        Get the constraints for each cell in the grid
        
        Parameters:
        grid (list): A 9x9 array of integers
        
        Returns:
        dict: A dictionary containing the constraints for each cell
        """
        constraints = {}
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    allowed_values = set(range(1, 10))
                    for x in range(9):
                        if grid[row][x] in allowed_values:
                            allowed_values.remove(grid[row][x])
                        if grid[x][col] in allowed_values:
                            allowed_values.remove(grid[x][col])
                    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
                    for i in range(3):
                        for j in range(3):
                            if grid[start_row + i][start_col + j] in allowed_values:
                                allowed_values.remove(grid[start_row + i][start_col + j])
                    constraints[(row, col)] = allowed_values
        return constraints
    
    def forward_checking(grid, constraints, iterations):
        """
        Assigns values to the cells in the grid using forward checking

        Parameters:
        grid (list): A 9x9 array of integers
        constraints (dict): A dictionary containing the constraints for each cell
        iterations (int): The number of iterations to run forward checking
        """
        def assign_value(row, col, num):
            grid[row][col] = num
            for x in range(9):
                if (row, x) in constraints:
                    constraints[(row, x)].discard(num)
                if (x, col) in constraints:
                    constraints[(x, col)].discard(num)
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if (start_row + i, start_col + j) in constraints:
                        constraints[(start_row + i, start_col + j)].discard(num)

        for _ in range(iterations):
            if not constraints:
                break
            min_cell = min(constraints, key=lambda k: len(constraints[k]))
            if len(constraints[min_cell]) == 0:
                break
            num = constraints[min_cell].pop()
            # print(f"Assigning {num} to cell {min_cell} with {len(constraints[min_cell])} remaining values")
            assign_value(min_cell[0], min_cell[1], num)
            del constraints[min_cell]

        return grid
    
    constraints = get_constraints(board)
    
    # Find the numbers of zeros in the grid to determine the number of iterations
    zeros = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                zeros += 1

    if zeros < 50:
        iterations = 45
    elif zeros < 55:
        iterations = 30
    else:
        iterations = 45

    forward_checking(board, constraints, iterations)

    BT()

    return board
