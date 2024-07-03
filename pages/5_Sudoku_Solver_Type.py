import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import sudopy
import ConvertBoard
import pandas as pd

st.markdown("""
<h1 style="text-align: center; color: blue">Sudoku Solver Typing</h1>
<p style="text-align: center;">Enter the Sudoku board below and click on the submit button to get the solved Sudoku.<br> Use 0 to represent an empty cell.</p>

""", unsafe_allow_html=True)

# Create the 9x9 grid

col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

st.write("--------")

with col1:
    st.number_input("", value=0, key="00")
    st.number_input("", value=0, key="01")
    st.number_input("", value=0, key="02")

    st.number_input("", value=0, key="03")
    st.number_input("", value=0, key="04")
    st.number_input("", value=0, key="05")

    st.number_input("", value=0, key="06")
    st.number_input("", value=0, key="07")
    st.number_input("", value=0, key="08")

with col2:
    st.number_input("", value=0, key="10")
    st.number_input("", value=0, key="11")
    st.number_input("", value=0, key="12")

    st.number_input("", value=0, key="13")
    st.number_input("", value=0, key="14")
    st.number_input("", value=0, key="15")

    st.number_input("", value=0, key="16")
    st.number_input("", value=0, key="17")
    st.number_input("", value=0, key="18")

with col3:
    st.number_input("", value=0, key="20")
    st.number_input("", value=0, key="21")
    st.number_input("", value=0, key="22")

    st.number_input("", value=0, key="23")
    st.number_input("", value=0, key="24")
    st.number_input("", value=0, key="25")

    st.number_input("", value=0, key="26")
    st.number_input("", value=0, key="27")
    st.number_input("", value=0, key="28")

with col4:
    st.number_input("", value=0, key="30")
    st.number_input("", value=0, key="31")
    st.number_input("", value=0, key="32")

    st.number_input("", value=0, key="33")
    st.number_input("", value=0, key="34")
    st.number_input("", value=0, key="35")

    st.number_input("", value=0, key="36")
    st.number_input("", value=0, key="37")
    st.number_input("", value=0, key="38")

with col5:
    st.number_input("", value=0, key="40")
    st.number_input("", value=0, key="41")
    st.number_input("", value=0, key="42")

    st.number_input("", value=0, key="43")
    st.number_input("", value=0, key="44")
    st.number_input("", value=0, key="45")

    st.number_input("", value=0, key="46")
    st.number_input("", value=0, key="47")
    st.number_input("", value=0, key="48")

with col6:
    st.number_input("", value=0, key="50")
    st.number_input("", value=0, key="51")
    st.number_input("", value=0, key="52")

    st.number_input("", value=0, key="53")
    st.number_input("", value=0, key="54")
    st.number_input("", value=0, key="55")

    st.number_input("", value=0, key="56")
    st.number_input("", value=0, key="57")
    st.number_input("", value=0, key="58")

with col7:
    st.number_input("", value=0, key="60")
    st.number_input("", value=0, key="61")
    st.number_input("", value=0, key="62")

    st.number_input("", value=0, key="63")
    st.number_input("", value=0, key="64")
    st.number_input("", value=0, key="65")

    st.number_input("", value=0, key="66")
    st.number_input("", value=0, key="67")
    st.number_input("", value=0, key="68")

with col8:
    st.number_input("", value=0, key="70")
    st.number_input("", value=0, key="71")
    st.number_input("", value=0, key="72")

    st.number_input("", value=0, key="73")
    st.number_input("", value=0, key="74")
    st.number_input("", value=0, key="75")

    st.number_input("", value=0, key="76")
    st.number_input("", value=0, key="77")
    st.number_input("", value=0, key="78")

with col9:
    st.number_input("", value=0, key="80")
    st.number_input("", value=0, key="81")
    st.number_input("", value=0, key="82")

    st.number_input("", value=0, key="83")
    st.number_input("", value=0, key="84")
    st.number_input("", value=0, key="85")

    st.number_input("", value=0, key="86",)
    st.number_input("", value=0, key="87")
    st.number_input("", value=0, key="88")



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

if st.button("Submit"):
    # Get all the values
    values = {}
    ip = []
    for i in range(9):
        lis = []
        for j in range(9):
            # check if the input values are valid
            if st.session_state[f"{i}{j}"] not in range(10):
                st.warning("Invalid input")
                break
            values[f"{i}{j}"] = st.session_state[f"{i}{j}"]
            lis.append(st.session_state[f"{i}{j}"])

        ip.append(lis)

    ip = np.array(ip)
    ip = np.transpose(ip)
    ip = ip.tolist()
    sudo = sudopy.Sudoku(ip)

    
    if ip is None:
        st.warning("Could not detect the Sudoku board. Please try again.")
    elif not sudo.is_valid_input():
        st.warning("Invalid input. Please make sure the Sudoku is valid.")
    else:
    # Solve the Sudoku
            
        sudo = sudopy.Sudoku(ip)
        sudo.solve()

        # Display the solved Sudoku
        st.success("Sudoku Solved Successfully!")
        
        df = pd.DataFrame(sudo.grid, columns=("%d" % i for i in range(0, 9)))  

        st.dataframe(df, use_container_width=True)