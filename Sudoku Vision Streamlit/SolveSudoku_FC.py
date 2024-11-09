# Function to solve the Sudoku puzzle using forward checking
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
