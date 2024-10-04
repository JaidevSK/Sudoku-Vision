from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import Img2Arr
import SolveSudoku

print("Welcome to Sudoku Vision!")
input_path = input("Enter the path of the image: ")
img = Image.open(input_path)
# Plot the original image
plt.title("Original Image")
plt.imshow(img)
plt.axis('off')

img_arr = np.array(img)
sudarr = Img2Arr.img2arr(img_arr)
grid = SolveSudoku.SolveSudoku(sudarr)
grid = np.array(grid)
grid = grid.T
# Convert the retarr to a plot
fig, ax = plt.subplots()

# Create a 9x9 grid
for i in range(10):
    if i % 3 == 0:
        linewidth = 2
    else:
        linewidth = 1

    ax.plot([i, i], [0, 9], color='black', linewidth=linewidth)
    ax.plot([0, 9], [i, i], color='black', linewidth=linewidth)

# Fill in the numbers
for i in range(9):
    for j in range(9):
        if grid[i][j] != 0:
            ax.text(j + 0.5, 8.5 - i, grid[i][j], ha='center', va='center', fontsize=16)


plt.axis('off')
plt.title("Solved Sudoku")
plt.show()
