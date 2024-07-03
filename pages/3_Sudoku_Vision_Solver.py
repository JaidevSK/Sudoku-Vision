import streamlit as st
import cv2
import numpy as np
import sudopy
import ConvertBoard
import pandas as pd

st.markdown("""<h1 style="color:blue; text-align:center;">Sudoku Vision Solver</h1>""", unsafe_allow_html=True)

uploaded_files = st.file_uploader("Choose an Image file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    st.write("filename:", uploaded_file.name)
    img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)

    st.image(img, channels="BGR")

    st.write("Image shape:", img.shape)

    if st.button("Solve"):
        with st.spinner("Solving the Sudoku puzzle..."):

            grid_ip = ConvertBoard.convert_board(img)
            if grid_ip is None:
                st.warning("Could not detect the Sudoku board. Please try again.")
                continue
            if not sudopy.Sudoku(grid_ip).is_valid_input():
                st.warning("Invalid input. Please make sure the Sudoku is valid.")
                continue
            sudo = sudopy.Sudoku(grid_ip)
            sudo.solve()

        st.success("Solved Sudoku")
        df = pd.DataFrame(sudo.grid, columns=("%d" % i for i in range(0, 9)))
        st.dataframe(df, use_container_width=True)


