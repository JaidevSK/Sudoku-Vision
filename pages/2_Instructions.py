# Instructions
import streamlit as st

body = """
<h1 style="color:blue; text-align:center;">Instructions</h1>

<h3 style="color:blue;">About Sudoku</h3>

<p>Sudoku is a logic-based, combinatorial number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid contain all of the digits from 1 to 9.</p>
<p>Each Sudoku puzzle begins with some cells filled in. The player uses these seed numbers as a launching point toward finding the unique solution.</p>
<p>Completing the entire puzzle requires patience, logical ability, and a good understanding of the rules of the game.</p>
<p> For more understanding, please refer to the following link: <a href="https://en.wikipedia.org/wiki/Sudoku">Sudoku</a></p>

<h3 style="color:blue;">About Sudoku Vision Solver</h3>

<p>Sudoku Vision Solver is a web application that uses computer vision to solve Sudoku puzzles. The user can upload an image of a Sudoku puzzle, and the application will solve the puzzle and display the solution. The image should be clear and be in .png, .jpg, or .jpeg format.</p>

<h3 style="color:blue;">About Sudoku Solver Textfile</h3>

<p>Sudoku Solver Textfile is a web application that uses a text file to solve Sudoku puzzles. The user can upload a text file of a Sudoku puzzle, and the application will solve the puzzle and display the solution. The text file should be in .txt format. The input in the textfile should be of the form of a single line with 81 characters with the empty characters replaced by ".".</p>

<h3 style="color:blue;">About Sudoku Solver Type input</h3>

<p>Sudoku Solver Type input is a web application that allows the user to input the Sudoku puzzle manually. The user can input the Sudoku puzzle in the form of a 9x9 grid. The user can input the numbers from 1 to 9 in the grid. The empty cells should be "0".</p>

<h3 style="color:blue;">About Play Sudoku</h3>

<p>Play Sudoku is a web application that allows the user to play Sudoku. The user can play the game by inputting the numbers in the empty cells. The user can check the solution at any time by clicking the "Check Solution" button. The user can select the difficulty level of the Sudoku puzzle from the options, namely "Easy", "Medium", "Hard", and "Expert". Then, the user can click the "Generate Puzzle" button to generate a new puzzle of the selected difficulty level.</p>

<h3 style="color:blue;">About Sudoku Solver Algorithm</h3>

<p>The image processing and computer vision techniques are used to extract the Sudoku puzzle from the image. The extracted puzzle is then solved using the backtracking algorithm. The backtracking algorithm is a recursive algorithm that tries to solve the Sudoku puzzle by filling in the empty cells with the numbers from 1 to 9. If the algorithm reaches a cell where it cannot place any number, it backtracks to the previous cell and tries the next number. The algorithm continues this process until it fills in all the cells of the puzzle.</p>

"""

st.markdown(body, unsafe_allow_html=True)