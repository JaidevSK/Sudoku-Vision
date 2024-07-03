import streamlit as st
import cv2
import numpy as np
import sudopy
import ConvertBoard
import pandas as pd

st.markdown("<h1 style='text-align: center; color: blue;'>Sudoku Solver Textfile</h1>", unsafe_allow_html=True)

uploaded_files = st.file_uploader("Choose a Text File", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    st.write("filename:", uploaded_file.name)
    
    sud = uploaded_file.read().decode("utf-8")
    
    mat = []

    for i in  range(9):
        lis = []
        for j in range(9):
            if sud[i*9+j] != ".":
                lis.append(int(sud[i*9+j]))
            else:
                lis.append(0)
        mat.append(lis)

    if st.button("Solve"):
        with st.spinner("Solving the Sudoku puzzle..."):
            sudo = sudopy.Sudoku(mat)
            sudo.solve()

        st.success("Solved Sudoku")
        df = pd.DataFrame(sudo.grid, columns=("%d" % i for i in range(0, 9)))
        st.dataframe(df, use_container_width=True)


