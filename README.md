# Sudoku-Vision
### Foundations of AI: Multiagent Systems (2024)
- Jaidev Khalane (22110103)
- Vannsh Jani (22110279)

# 1. Aim
- To develop an application that solves Sudoku puzzles from images using the most optimal method for different difficulty levels (by adjusting the proportion of the problem that will be solved by Constraint satisfaction and Backtracking).
- To explore the usage of Reinforcement Learning in solving Sudoku puzzles

# 2. Methodology
## 2.1 Sudoku Vision Application
### 2.1.1 Digit Optical Character Recognition
Since we aim to solve sudokus directly from the images (without requiring the user to manually type the sudoku digits), one of the most important tasks is to have a computer vision model for the classification of the given images of individual digits into their respective classes of digits. This is the task of Optical Character Recognition or OCR. In order to perform the task of OCR, we can either use the python library of EasyOCR or develop a model from scratch. We have taken the second approach. The dataset for the model was taken from kaggle <https://www.kaggle.com/datasets/kshitijdhama/printed-digits-dataset> [1]. Some images from the dataset are as given below: </br>

![image](https://github.com/user-attachments/assets/0d58065a-639e-4485-97e2-8a911047a613)


Model Architecture: </br>

![image](https://github.com/user-attachments/assets/6e5d572f-2f31-431a-98d3-4f756546fe55)

Model Architecture Diagram: </br>

![image](https://github.com/user-attachments/assets/000a31b9-e5cd-4010-9fe8-a5a2e2791b5b)

Model Training:
The training for the Digit Optical Character Recognition model was carried out for 20 Epochs. The training dataset consisted of 5669 images while the test dataset consisted of 630 images. The images were converted to grayscale with a size of 28x28.
The training statistics are as given below: </br>
![image](https://github.com/user-attachments/assets/5a900267-6248-43e2-9cc3-d164215068e8)

Test Statistics: </br>
![image](https://github.com/user-attachments/assets/08bef52f-4ace-49aa-88f4-92e4779c5df2)

Model Usage: </br>
![image](https://github.com/user-attachments/assets/f535c064-9c4a-4e62-b3c0-52868a5abf81)

The trained model weights have been stored as .keras file and .h5 file in the DigitOCR folder.

