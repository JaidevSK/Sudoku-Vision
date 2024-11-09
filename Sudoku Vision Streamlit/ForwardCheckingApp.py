from PIL import Image
import pandas as pd
import numpy as np
from PIL import Image
import Img2Arr
import plotly.graph_objects as go
import streamlit as st


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

def plot_grid(fixed_grid, title, constraints_grid):
    """
    Plot the grid with fixed values and the solution
    
    Parameters:
    grid (list): A 9x9 array of integers
    fixed_grid (list): A 9x9 array of integers with fixed values
    title (str): The title of the plot
    """
    
    fig = go.Figure()
    print(constraints_grid)
    for i in range(9):
        for j in range(9):
            if (i, j) not in constraints_grid:
                # In a green coloured box, add the fixed value as text inside the box (i.e. the fixed value)
                fig.add_trace(go.Scatter (x=[j, j + 1, j + 1, j, j], y=[i, i, i + 1, i + 1, i], fill='toself', mode='lines', fillcolor='lime', line=dict(color='black'), showlegend=False))
                fig.add_trace(go.Scatter (x=[j + 0.5], y=[i + 0.5], text=str(fixed_grid[i][j]), mode='text', hovertext=str("I am Fixed!"), hoverinfo='text', showlegend=False))

            else:
                # In a blue coloured box, add the possible values as text that are show on hover
                fig.add_trace(go.Scatter (x=[j, j + 1, j + 1, j, j], y=[i, i, i + 1, i + 1, i], fill='toself', mode='lines', fillcolor='skyblue', line=dict(color='black'), showlegend=False))
                fig.add_trace(go.Scatter (x=[j + 0.5], y=[i + 0.5], text=str("?"), mode='text', hovertext=str(constraints_grid[(i, j)]), hoverinfo='text', showlegend=False))



    # Update layout and do not also show the indices
    fig.update_layout(width=800, height=800, showlegend=False, xaxis=dict(showticklabels=False), yaxis=dict(showticklabels=False))
    fig.update_layout(title=title)

    return fig

# Streamlit App

# Use full width
st.set_page_config(layout="wide")


# Central align
st.markdown("<h1 style='text-align: center;'>Sudoku Vision - Forward Checking</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Upload an image of a Sudoku puzzle and we will solve it for you!</h3>", unsafe_allow_html=True)



# Column 1
uploaded_file = st.file_uploader("Choose an image...")

# Divide the page into two columns
col1, col2 = st.columns(2)
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    col1.image(img, caption="Uploaded Image", width=500)
    img_arr = np.array(img)
    sudarr = Img2Arr.img2arr(img_arr)
        
    # Forward checking
    iterations = sum([1 for row in sudarr for cell in row if cell == 0])
    grids = [np.copy(sudarr)]
    constraints = get_constraints(sudarr)
    constraints_list = [get_constraints(sudarr)]
    for i in range(iterations):
        sudarr = forward_checking(sudarr, constraints, 1)
        constraints = get_constraints(sudarr)
        grids.append(np.copy(sudarr))
        constraints_list.append(constraints)

    # Create a slider to navigate through the iterations
    iteration = st.slider("Select an iteration", 0, iterations, 0)
    grid = grids[iteration]
    constraints_grid = constraints_list[iteration]
    grid = np.array(grid)
    grid = grid.T
    fixed_grid = np.array(grid)
    fixed_grid = fixed_grid.T
    fig = plot_grid(fixed_grid, "Sudoku in Iteration " + str(iteration), constraints_grid)
    col2.plotly_chart(fig)

    



