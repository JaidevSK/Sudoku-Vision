# Streamlit App

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import Img2Arr
import SolveSudoku_BT_Viz as SolveSudoku
import matplotlib.animation as animation
import matplotlib.pyplot as plt


def animate_sudoku(all_boards):
    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        ax.set_xticks([i + 0.5 for i in range(9)], minor=True)
        ax.set_yticks([i + 0.5 for i in range(9)], minor=True)
        ax.grid(which="minor", color="black", linestyle='-', linewidth=2)
        ax.imshow([[5]*9]*9, cmap="Blues", vmin=0, vmax=9)
        
        for i in range(9):
            for j in range(9):
                num = all_boards[frame][i][j]
                if num != 0:
                    ax.text(j, i, str(num), ha="center", va="center", color="black")
        
        ax.set_xticks([])
        ax.set_yticks([])

    ani = animation.FuncAnimation(fig, update, frames=len(all_boards), interval=500, repeat=False)
    ani.save("sudoku.gif", writer="pillow")

# Use full width
st.set_page_config(layout="wide")


# Central align
st.markdown("<h1 style='text-align: center;'>Sudoku Vision - Backtracking</h1>", unsafe_allow_html=True)
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
    all_boards = grid
    animate_sudoku(all_boards)
    col2.image("sudoku.gif", caption="Solved Sudoku", width=500)
    st.markdown("<h3 style='text-align: center;'>Sudoku Solved!</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Download the solved Sudoku below:</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'><a href='sudoku.gif' download>Download Solved Sudoku</a></h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Upload another image to solve another Sudoku puzzle!</h3>", unsafe_allow_html=True)


# To run the app, run the following command in the terminal:
# streamlit run StreamlitApp.py

