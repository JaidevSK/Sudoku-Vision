import streamlit as st
import numpy as np
import pandas as pd
import sudopy
import ConvertBoard
import streamlit.components.v1 as components
import random


body = """
<h1 style="color:blue; text-align:center">Play Sudoku</h1>
<p>This is a Sudoku player that generates a random Sudoku puzzle and allows you to solve it.</p>
<p>You can also check if the puzzle is valid and submit your solution to get the answer.</p>
<p>The puzzle is generated based on the difficulty level you choose.</p>
"""

st.markdown(body, unsafe_allow_html=True)

# Create a radio with easy, medium, hard, and expert as options
difficulty = st.radio("Select the difficulty level", ["Easy", "Medium", "Hard", "Expert"])

if st.button("Generate Sudoku"):
    # open file containing the sudokus of the specfied difficulty
    file_name = 'sudokus/sudokus_' + str(difficulty) + '.txt'
    file = open(file_name, 'r')
    all_lines = file.readlines()

    # choose random line from the file
    rand_num = random.randint(0, 400)
    rand_line = all_lines[rand_num]

    # if the line in the text file is blank, move to the next one
    if len(rand_line) <= 2:
        rand_line = all_lines[rand_num + 1]

    sud = rand_line
    
    components.html(
        """
    <script>
    const elements = window.parent.document.querySelectorAll('.stNumberInput div[data-baseweb="input"] > div')
    console.log(elements)
    elements[0].style.backgroundColor = 'orange'
    elements[1].style.backgroundColor = 'orange'
    elements[2].style.backgroundColor = 'orange'

    elements[3].style.backgroundColor = 'lightblue'
    elements[4].style.backgroundColor = 'lightblue'
    elements[5].style.backgroundColor = 'lightblue'

    elements[6].style.backgroundColor = 'orange'
    elements[7].style.backgroundColor = 'orange'
    elements[8].style.backgroundColor = 'orange'

    elements[9].style.backgroundColor = 'orange'
    elements[10].style.backgroundColor = 'orange'
    elements[11].style.backgroundColor = 'orange'

    elements[12].style.backgroundColor = 'lightblue'
    elements[13].style.backgroundColor = 'lightblue'
    elements[14].style.backgroundColor = 'lightblue'

    elements[15].style.backgroundColor = 'orange'
    elements[16].style.backgroundColor = 'orange'
    elements[17].style.backgroundColor = 'orange'

    elements[18].style.backgroundColor = 'orange'
    elements[19].style.backgroundColor = 'orange'
    elements[20].style.backgroundColor = 'orange'

    elements[21].style.backgroundColor = 'lightblue'
    elements[22].style.backgroundColor = 'lightblue'
    elements[23].style.backgroundColor = 'lightblue'

    elements[24].style.backgroundColor = 'orange'
    elements[25].style.backgroundColor = 'orange'
    elements[26].style.backgroundColor = 'orange'

    elements[27].style.backgroundColor = 'lightblue'
    elements[28].style.backgroundColor = 'lightblue'
    elements[29].style.backgroundColor = 'lightblue'

    elements[30].style.backgroundColor = 'orange'
    elements[31].style.backgroundColor = 'orange'
    elements[32].style.backgroundColor = 'orange'

    elements[33].style.backgroundColor = 'lightblue'
    elements[34].style.backgroundColor = 'lightblue'
    elements[35].style.backgroundColor = 'lightblue'

    elements[36].style.backgroundColor = 'lightblue'
    elements[37].style.backgroundColor = 'lightblue'
    elements[38].style.backgroundColor = 'lightblue'

    elements[39].style.backgroundColor = 'orange'
    elements[40].style.backgroundColor = 'orange'
    elements[41].style.backgroundColor = 'orange'

    elements[42].style.backgroundColor = 'lightblue'
    elements[43].style.backgroundColor = 'lightblue'
    elements[44].style.backgroundColor = 'lightblue'

    elements[45].style.backgroundColor = 'lightblue'
    elements[46].style.backgroundColor = 'lightblue'
    elements[47].style.backgroundColor = 'lightblue'

    elements[48].style.backgroundColor = 'orange'
    elements[49].style.backgroundColor = 'orange'
    elements[50].style.backgroundColor = 'orange'

    elements[51].style.backgroundColor = 'lightblue'
    elements[52].style.backgroundColor = 'lightblue'
    elements[53].style.backgroundColor = 'lightblue'

    elements[54].style.backgroundColor = 'orange'
    elements[55].style.backgroundColor = 'orange'
    elements[56].style.backgroundColor = 'orange'

    elements[57].style.backgroundColor = 'lightblue'
    elements[58].style.backgroundColor = 'lightblue'
    elements[59].style.backgroundColor = 'lightblue'

    elements[60].style.backgroundColor = 'orange'
    elements[61].style.backgroundColor = 'orange'
    elements[62].style.backgroundColor = 'orange'

    elements[63].style.backgroundColor = 'orange'
    elements[64].style.backgroundColor = 'orange'
    elements[65].style.backgroundColor = 'orange'

    elements[66].style.backgroundColor = 'lightblue'
    elements[67].style.backgroundColor = 'lightblue'
    elements[68].style.backgroundColor = 'lightblue'

    elements[69].style.backgroundColor = 'orange'
    elements[70].style.backgroundColor = 'orange'
    elements[71].style.backgroundColor = 'orange'

    elements[72].style.backgroundColor = 'orange'
    elements[73].style.backgroundColor = 'orange'
    elements[74].style.backgroundColor = 'orange'

    elements[75].style.backgroundColor = 'lightblue'
    elements[76].style.backgroundColor = 'lightblue'
    elements[77].style.backgroundColor = 'lightblue'

    elements[78].style.backgroundColor = 'orange'
    elements[79].style.backgroundColor = 'orange'
    elements[80].style.backgroundColor = 'orange'

    </script>
    """,
        height=0,
        width=0,
    )


    st.markdown("""
        <style>
        [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
            gap: 0px;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
        [data-testid=column]:nth-of-type(2) [data-testid=stVerticalBlock]{
            gap: 0rem;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
        [data-testid=column]:nth-of-type(3) [data-testid=stVerticalBlock]{
            gap: 0rem;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
        [data-testid=column]:nth-of-type(4) [data-testid=stVerticalBlock]{
            gap: 0rem;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
        [data-testid=column]:nth-of-type(5) [data-testid=stVerticalBlock]{
            gap: 0rem;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
        [data-testid=column]:nth-of-type(6) [data-testid=stVerticalBlock]{
            gap: 0rem;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
        [data-testid=column]:nth-of-type(7) [data-testid=stVerticalBlock]{
            gap: 0rem;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
        [data-testid=column]:nth-of-type(8) [data-testid=stVerticalBlock]{
            gap: 0rem;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
        [data-testid=column]:nth-of-type(9) [data-testid=stVerticalBlock]{
            gap: 0rem;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
                
                
                
        </style>
        """,unsafe_allow_html=True)


else:
    sud = "................................................................................."

    st.markdown("""
        <style>
        [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
            gap: 0px;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
        [data-testid=column]:nth-of-type(2) [data-testid=stVerticalBlock]{
            gap: 0rem;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
        [data-testid=column]:nth-of-type(3) [data-testid=stVerticalBlock]{
            gap: 0rem;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
        [data-testid=column]:nth-of-type(4) [data-testid=stVerticalBlock]{
            gap: 0rem;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
        [data-testid=column]:nth-of-type(5) [data-testid=stVerticalBlock]{
            gap: 0rem;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
        [data-testid=column]:nth-of-type(6) [data-testid=stVerticalBlock]{
            gap: 0rem;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
        [data-testid=column]:nth-of-type(7) [data-testid=stVerticalBlock]{
            gap: 0rem;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
        [data-testid=column]:nth-of-type(8) [data-testid=stVerticalBlock]{
            gap: 0rem;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
        [data-testid=column]:nth-of-type(9) [data-testid=stVerticalBlock]{
            gap: 0rem;
            padding: 0rem;
            margin: 0rem;
            margin-top: 0rem;
            margin-bottom: 0rem;
        }
                
                
                
        </style>
        """,unsafe_allow_html=True)

dis_dict = {}
mat = []

for i in  range(9):
    lis = []
    for j in range(9):
        if sud[i*9+j] != ".":
            dis_dict[i*9+j] = True
            lis.append(int(sud[i*9+j]))
        else:
            lis.append(0)
            dis_dict[i*9+j] = False
    mat.append(lis)




# Create a timer

# Create the title

# Create the 9x9 grid

col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

st.write("--------")

with col1:
    c0r0 = st.number_input("", value=mat[0][0], key="00", disabled=dis_dict[0]) 
    c0r1 = st.number_input("", value=mat[0][1], key="01", disabled=dis_dict[1])
    c0r2 = st.number_input("", value=mat[0][2], key="02", disabled=dis_dict[2])
    c0r3 = st.number_input("", value=mat[0][3], key="03", disabled=dis_dict[3])
    c0r4 = st.number_input("", value=mat[0][4], key="04", disabled=dis_dict[4])
    c0r5 = st.number_input("", value=mat[0][5], key="05", disabled=dis_dict[5])
    c0r6 = st.number_input("", value=mat[0][6], key="06", disabled=dis_dict[6])
    c0r7 = st.number_input("", value=mat[0][7], key="07", disabled=dis_dict[7])
    c0r8 = st.number_input("", value=mat[0][8], key="08", disabled=dis_dict[8])

with col2:
    c1r0 = st.number_input("", value=mat[1][0], key="10", disabled=dis_dict[9])
    c1r1 = st.number_input("", value=mat[1][1], key="11", disabled=dis_dict[10])
    c1r2 = st.number_input("", value=mat[1][2], key="12", disabled=dis_dict[11])
    c1r3 = st.number_input("", value=mat[1][3], key="13", disabled=dis_dict[12])
    c1r4 = st.number_input("", value=mat[1][4], key="14", disabled=dis_dict[13])
    c1r5 = st.number_input("", value=mat[1][5], key="15", disabled=dis_dict[14])
    c1r6 = st.number_input("", value=mat[1][6], key="16", disabled=dis_dict[15])
    c1r7 = st.number_input("", value=mat[1][7], key="17", disabled=dis_dict[16])
    c1r8 = st.number_input("", value=mat[1][8], key="18", disabled=dis_dict[17])

with col3:
    c2r0 = st.number_input("", value=mat[2][0], key="20", disabled=dis_dict[18])
    c2r1 = st.number_input("", value=mat[2][1], key="21", disabled=dis_dict[19])
    c2r2 = st.number_input("", value=mat[2][2], key="22", disabled=dis_dict[20])
    c2r3 = st.number_input("", value=mat[2][3], key="23", disabled=dis_dict[21])
    c2r4 = st.number_input("", value=mat[2][4], key="24", disabled=dis_dict[22])
    c2r5 = st.number_input("", value=mat[2][5], key="25", disabled=dis_dict[23])
    c2r6 = st.number_input("", value=mat[2][6], key="26", disabled=dis_dict[24])
    c2r7 = st.number_input("", value=mat[2][7], key="27", disabled=dis_dict[25])
    c2r8 = st.number_input("", value=mat[2][8], key="28", disabled=dis_dict[26])

with col4:
    c3r0 = st.number_input("", value=mat[3][0], key="30", disabled=dis_dict[27])
    c3r1 = st.number_input("", value=mat[3][1], key="31", disabled=dis_dict[28])
    c3r2 = st.number_input("", value=mat[3][2], key="32", disabled=dis_dict[29])
    c3r3 = st.number_input("", value=mat[3][3], key="33", disabled=dis_dict[30])
    c3r4 = st.number_input("", value=mat[3][4], key="34", disabled=dis_dict[31])
    c3r5 = st.number_input("", value=mat[3][5], key="35", disabled=dis_dict[32])
    c3r6 = st.number_input("", value=mat[3][6], key="36", disabled=dis_dict[33])
    c3r7 = st.number_input("", value=mat[3][7], key="37", disabled=dis_dict[34])
    c3r8 = st.number_input("", value=mat[3][8], key="38", disabled=dis_dict[35])

with col5:
    c4r0 = st.number_input("", value=mat[4][0], key="40", disabled=dis_dict[36])
    c4r1 = st.number_input("", value=mat[4][1], key="41", disabled=dis_dict[37])
    c4r2 = st.number_input("", value=mat[4][2], key="42", disabled=dis_dict[38])
    c4r3 = st.number_input("", value=mat[4][3], key="43", disabled=dis_dict[39])
    c4r4 = st.number_input("", value=mat[4][4], key="44", disabled=dis_dict[40])
    c4r5 = st.number_input("", value=mat[4][5], key="45", disabled=dis_dict[41])
    c4r6 = st.number_input("", value=mat[4][6], key="46", disabled=dis_dict[42])
    c4r7 = st.number_input("", value=mat[4][7], key="47", disabled=dis_dict[43])
    c4r8 = st.number_input("", value=mat[4][8], key="48", disabled=dis_dict[44])

with col6:
    c5r0 = st.number_input("", value=mat[5][0], key="50", disabled=dis_dict[45])
    c5r1 = st.number_input("", value=mat[5][1], key="51", disabled=dis_dict[46])
    c5r2 = st.number_input("", value=mat[5][2], key="52", disabled=dis_dict[47])
    c5r3 = st.number_input("", value=mat[5][3], key="53", disabled=dis_dict[48])
    c5r4 = st.number_input("", value=mat[5][4], key="54", disabled=dis_dict[49])
    c5r5 = st.number_input("", value=mat[5][5], key="55", disabled=dis_dict[50])
    c5r6 = st.number_input("", value=mat[5][6], key="56", disabled=dis_dict[51])
    c5r7 = st.number_input("", value=mat[5][7], key="57", disabled=dis_dict[52])
    c5r8 = st.number_input("", value=mat[5][8], key="58", disabled=dis_dict[53])

with col7:
    c6r0 = st.number_input("", value=mat[6][0], key="60", disabled=dis_dict[54])
    c6r1 = st.number_input("", value=mat[6][1], key="61", disabled=dis_dict[55])
    c6r2 = st.number_input("", value=mat[6][2], key="62", disabled=dis_dict[56])
    c6r3 = st.number_input("", value=mat[6][3], key="63", disabled=dis_dict[57])
    c6r4 = st.number_input("", value=mat[6][4], key="64", disabled=dis_dict[58])
    c6r5 = st.number_input("", value=mat[6][5], key="65", disabled=dis_dict[59])
    c6r6 = st.number_input("", value=mat[6][6], key="66", disabled=dis_dict[60])
    c6r7 = st.number_input("", value=mat[6][7], key="67", disabled=dis_dict[61])
    c6r8 = st.number_input("", value=mat[6][8], key="68", disabled=dis_dict[62])

with col8:
    c7r0 = st.number_input("", value=mat[7][0], key="70", disabled=dis_dict[63])
    c7r1 = st.number_input("", value=mat[7][1], key="71", disabled=dis_dict[64])
    c7r2 = st.number_input("", value=mat[7][2], key="72", disabled=dis_dict[65])
    c7r3 = st.number_input("", value=mat[7][3], key="73", disabled=dis_dict[66])
    c7r4 = st.number_input("", value=mat[7][4], key="74", disabled=dis_dict[67])
    c7r5 = st.number_input("", value=mat[7][5], key="75", disabled=dis_dict[68])
    c7r6 = st.number_input("", value=mat[7][6], key="76", disabled=dis_dict[69])
    c7r7 = st.number_input("", value=mat[7][7], key="77", disabled=dis_dict[70])
    c7r8 = st.number_input("", value=mat[7][8], key="78", disabled=dis_dict[71])

with col9:
    c8r0 = st.number_input("", value=mat[8][0], key="80", disabled=dis_dict[72])
    c8r1 = st.number_input("", value=mat[8][1], key="81", disabled=dis_dict[73])
    c8r2 = st.number_input("", value=mat[8][2], key="82", disabled=dis_dict[74])
    c8r3 = st.number_input("", value=mat[8][3], key="83", disabled=dis_dict[75])
    c8r4 = st.number_input("", value=mat[8][4], key="84", disabled=dis_dict[76])
    c8r5 = st.number_input("", value=mat[8][5], key="85", disabled=dis_dict[77])
    c8r6 = st.number_input("", value=mat[8][6], key="86", disabled=dis_dict[78])
    c8r7 = st.number_input("", value=mat[8][7], key="87", disabled=dis_dict[79])
    c8r8 = st.number_input("", value=mat[8][8], key="88", disabled=dis_dict[80])


components.html(
    """
<script>
const elements = window.parent.document.querySelectorAll('.stNumberInput div[data-baseweb="input"] > div')
console.log(elements)
elements[0].style.backgroundColor = 'orange'
elements[1].style.backgroundColor = 'orange'
elements[2].style.backgroundColor = 'orange'

elements[3].style.backgroundColor = 'lightblue'
elements[4].style.backgroundColor = 'lightblue'
elements[5].style.backgroundColor = 'lightblue'

elements[6].style.backgroundColor = 'orange'
elements[7].style.backgroundColor = 'orange'
elements[8].style.backgroundColor = 'orange'

elements[9].style.backgroundColor = 'orange'
elements[10].style.backgroundColor = 'orange'
elements[11].style.backgroundColor = 'orange'

elements[12].style.backgroundColor = 'lightblue'
elements[13].style.backgroundColor = 'lightblue'
elements[14].style.backgroundColor = 'lightblue'

elements[15].style.backgroundColor = 'orange'
elements[16].style.backgroundColor = 'orange'
elements[17].style.backgroundColor = 'orange'

elements[18].style.backgroundColor = 'orange'
elements[19].style.backgroundColor = 'orange'
elements[20].style.backgroundColor = 'orange'

elements[21].style.backgroundColor = 'lightblue'
elements[22].style.backgroundColor = 'lightblue'
elements[23].style.backgroundColor = 'lightblue'

elements[24].style.backgroundColor = 'orange'
elements[25].style.backgroundColor = 'orange'
elements[26].style.backgroundColor = 'orange'

elements[27].style.backgroundColor = 'lightblue'
elements[28].style.backgroundColor = 'lightblue'
elements[29].style.backgroundColor = 'lightblue'

elements[30].style.backgroundColor = 'orange'
elements[31].style.backgroundColor = 'orange'
elements[32].style.backgroundColor = 'orange'

elements[33].style.backgroundColor = 'lightblue'
elements[34].style.backgroundColor = 'lightblue'
elements[35].style.backgroundColor = 'lightblue'

elements[36].style.backgroundColor = 'lightblue'
elements[37].style.backgroundColor = 'lightblue'
elements[38].style.backgroundColor = 'lightblue'

elements[39].style.backgroundColor = 'orange'
elements[40].style.backgroundColor = 'orange'
elements[41].style.backgroundColor = 'orange'

elements[42].style.backgroundColor = 'lightblue'
elements[43].style.backgroundColor = 'lightblue'
elements[44].style.backgroundColor = 'lightblue'

elements[45].style.backgroundColor = 'lightblue'
elements[46].style.backgroundColor = 'lightblue'
elements[47].style.backgroundColor = 'lightblue'

elements[48].style.backgroundColor = 'orange'
elements[49].style.backgroundColor = 'orange'
elements[50].style.backgroundColor = 'orange'

elements[51].style.backgroundColor = 'lightblue'
elements[52].style.backgroundColor = 'lightblue'
elements[53].style.backgroundColor = 'lightblue'

elements[54].style.backgroundColor = 'orange'
elements[55].style.backgroundColor = 'orange'
elements[56].style.backgroundColor = 'orange'

elements[57].style.backgroundColor = 'lightblue'
elements[58].style.backgroundColor = 'lightblue'
elements[59].style.backgroundColor = 'lightblue'

elements[60].style.backgroundColor = 'orange'
elements[61].style.backgroundColor = 'orange'
elements[62].style.backgroundColor = 'orange'

elements[63].style.backgroundColor = 'orange'
elements[64].style.backgroundColor = 'orange'
elements[65].style.backgroundColor = 'orange'

elements[66].style.backgroundColor = 'lightblue'
elements[67].style.backgroundColor = 'lightblue'
elements[68].style.backgroundColor = 'lightblue'

elements[69].style.backgroundColor = 'orange'
elements[70].style.backgroundColor = 'orange'
elements[71].style.backgroundColor = 'orange'

elements[72].style.backgroundColor = 'orange'
elements[73].style.backgroundColor = 'orange'
elements[74].style.backgroundColor = 'orange'

elements[75].style.backgroundColor = 'lightblue'
elements[76].style.backgroundColor = 'lightblue'
elements[77].style.backgroundColor = 'lightblue'

elements[78].style.backgroundColor = 'orange'
elements[79].style.backgroundColor = 'orange'
elements[80].style.backgroundColor = 'orange'

</script>
""",
    height=0,
    width=0,
)



st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
        gap: 0px;
        padding: 0rem;
        margin: 0rem;
        margin-top: 0rem;
        margin-bottom: 0rem;
    }
    [data-testid=column]:nth-of-type(2) [data-testid=stVerticalBlock]{
        gap: 0rem;
        padding: 0rem;
        margin: 0rem;
        margin-top: 0rem;
        margin-bottom: 0rem;
    }
    [data-testid=column]:nth-of-type(3) [data-testid=stVerticalBlock]{
        gap: 0rem;
        padding: 0rem;
        margin: 0rem;
        margin-top: 0rem;
        margin-bottom: 0rem;
    }
    [data-testid=column]:nth-of-type(4) [data-testid=stVerticalBlock]{
        gap: 0rem;
        padding: 0rem;
        margin: 0rem;
        margin-top: 0rem;
        margin-bottom: 0rem;
    }
    [data-testid=column]:nth-of-type(5) [data-testid=stVerticalBlock]{
        gap: 0rem;
        padding: 0rem;
        margin: 0rem;
        margin-top: 0rem;
        margin-bottom: 0rem;
    }
    [data-testid=column]:nth-of-type(6) [data-testid=stVerticalBlock]{
        gap: 0rem;
        padding: 0rem;
        margin: 0rem;
        margin-top: 0rem;
        margin-bottom: 0rem;
    }
    [data-testid=column]:nth-of-type(7) [data-testid=stVerticalBlock]{
        gap: 0rem;
        padding: 0rem;
        margin: 0rem;
        margin-top: 0rem;
        margin-bottom: 0rem;
    }
    [data-testid=column]:nth-of-type(8) [data-testid=stVerticalBlock]{
        gap: 0rem;
        padding: 0rem;
        margin: 0rem;
        margin-top: 0rem;
        margin-bottom: 0rem;
    }
    [data-testid=column]:nth-of-type(9) [data-testid=stVerticalBlock]{
        gap: 0rem;
        padding: 0rem;
        margin: 0rem;
        margin-top: 0rem;
        margin-bottom: 0rem;
    }
            
            
            
    </style>
    """,unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Check if the puzzle is valid

with col1:
    checkbut = st.button("Check Your Solution")

if checkbut:
    mat2 = []
    for i in range(9):
        lis = []
        for j in range(9):
            lis.append(st.session_state[f"{i}{j}"])
        mat2.append(lis)


    valid = True
    for i in range(9):
        for j in range(1, 10):
            if j not in mat2[i]:
                valid = False
                break
    for i in range(9):
        for j in range(1, 10):
            if j not in [mat2[k][i] for k in range(9)]:
                valid = False
                break
    for i in range(3):
        for j in range(3):
            for k in range(1, 10):
                if k not in [mat2[l][m] for l in range(3*i, 3*i+3) for m in range(3*j, 3*j+3)]:
                    valid = False
                    break
    if not valid:
        st.warning("Invalid Answer, Try Again!")
    else:
        st.success("Valid Answer! Congratulations!")

with col2:
    solbut = st.button("See Solution")

if solbut:
    # Get all the values
    values = {}
    ip = []
    for i in range(9):
        lis = []
        for j in range(9):
            values[f"{i}{j}"] = st.session_state[f"{i}{j}"]
            lis.append(st.session_state[f"{i}{j}"])

        ip.append(lis)

    ip = np.array(ip)
    ip = np.transpose(ip)

    for i in range(81):
        dis_dict[i] = True

    # Solve the Sudoku
        
    sudo = sudopy.Sudoku(ip)
    sudo.solve()

    # Display the solved Sudoku
    st.write("Solved Sudoku:")
    
    df = pd.DataFrame(sudo.grid, columns=("%d" % i for i in range(0, 9)))  

    st.dataframe(df, use_container_width=True)









