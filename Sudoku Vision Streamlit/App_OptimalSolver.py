# Streamlit App

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import Img2Arr
import SolveSudoku_OS as SolveSudoku

# Use full width
st.set_page_config(layout="wide")


# Central align
st.markdown("<h1 style='text-align: center;'>Sudoku Vision - Optimal Solver</h1>", unsafe_allow_html=True)
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
    grid = SolveSudoku.SolveSudoku(sudarr)
    grid = np.array(grid)
    grid = grid.T
    fig, ax = plt.subplots()
    for i in range(10):
        if i % 3 == 0:
            linewidth = 2
        else:
            linewidth = 1

        ax.plot([i, i], [0, 9], color='black', linewidth=linewidth)
        ax.plot([0, 9], [i, i], color='black', linewidth=linewidth)

    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                ax.text(j + 0.5, 8.5 - i, grid[i][j], ha='center', va='center', fontsize=16)

    plt.axis('off')
    plt.title("Solved Sudoku")
    col2.pyplot(fig)

