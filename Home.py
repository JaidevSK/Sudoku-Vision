import streamlit as st

body = """
<h1 style='text-align: center; color: blue;'>Sudoku Vision Application</h1>

<p style='text-align: center;'>This is a the web application that has been developed for all the sudoku lovers out there. This application is capable of solving any sudoku puzzle that you throw at it. All you have to do is upload an image of the sudoku puzzle and the application will do the rest for you. It will solve the puzzle and display the solution on the screen.</p>

<p style='text-align: center;'>Apart from this, you can also play the sudoku game on this application. You can select the difficulty level of the game and start playing. The application will also provide you with the facility to load the sudoku puzzle from text files or by directly typing them from the keyboard.</p>

<p style='text-align: center;'>So, what are you waiting for? Go ahead and start playing the sudoku game or upload the image or text file or directly type the puzzle to get the solution.</p>

<p style='text-align: center;'>Enjoy the game!</p>

"""

st.markdown(body, unsafe_allow_html=True)

# Create buttons

st.markdown("<h4 style='text-align: center; color: blue;'>Select the option to proceed:</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:        
    st.write(f'''
        <a target="_self" href="/Instructions">
            <button style="background-color: red;color: white;width:20rem">
                Read the Instructions
            </button>
        </a>
        ''',
        unsafe_allow_html=True
    )

    st.write(f'''
        <a target="_self" href="/Play_Sudoku">
            <button style="background-color: red;color: white;width:20rem">
                Play Sudoku
            </button>
        </a>
        ''',
        unsafe_allow_html=True
    )

    st.write(f'''
        <a target="_self" href="/">
            <button style="background-color: red;color: white;width:20rem">
                Home
            </button>
        </a>
        ''',
        unsafe_allow_html=True
    )

with col2:
    st.write(f'''
        <a target="_self" href="/Sudoku_Vision_Solver">
            <button style="background-color: red;color: white;width:20rem">
                Sudoku Vision Solver
            </button> 
        </a>
        ''',
        unsafe_allow_html=True
    )

    st.write(f'''
        <a target="_self" href="/Sudoku_Solver_Textfile">
            <button style="background-color: red;color: white;width:20rem">
                Sudoku Solver (Text File)
            </button>
        </a>
        ''',
        unsafe_allow_html=True
    )

    st.write(f'''
        <a target="_self" href="/Sudoku_Solver_Type">
            <button style="background-color: red;color: white;width:20rem">
                Sudoku Solver (Type)
            </button>
        </a>
        ''',
        unsafe_allow_html=True
    )

st.empty()

st.markdown("<p style='text-align: center;' ><br><br><br>Built with 🍉 by <a href=https://jaidevsk.github.io/Main.html>JaidevSK</a></p>", unsafe_allow_html=True)
