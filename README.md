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

### 2.1.2 Sudoku Extraction
As we are working with the images of the sudoku grid, we want to extract the values present in the grid of the sudoku as arrays instead of images. Therefore, in this part of the methodology, we will discuss the path taken by us in performing the extraction of the sudoku grid from the images. The sample image of the sudoku is as given below:
- Step 1: Image Capture
</br>![image](https://github.com/user-attachments/assets/854e8287-0ac5-449a-a517-f8e44c183d78)
This is a general image of a sudoku taken from a newspaper (taken from library) without much cropping or enhancement.
- Step 2: Conversion to Grayscale
</br>![image](https://github.com/user-attachments/assets/b53376b2-d90c-4fba-a380-e6d39923b08c)
The image was converted to grayscale to efficiently use our DigitOCR model
- Step 3: Denoising the Image
</br>![image](https://github.com/user-attachments/assets/731086a4-89c4-462d-b53c-ee8084a96922)
The image was denoised with a gaussian kernel to remove the noise (high frequency components) from the image (Gaussian Blur)
- Step 4: Adaptive Thresholding
</br>![image](https://github.com/user-attachments/assets/c6c6b00e-7b21-4674-9725-6c67cb144728)
In order to perform contour analysis (As the sudoku grid is expected to be the largest contour, it is necessary to perform edge detection which will be done in a better way if we have a binary image. So, in order to perform the binarization of the image, we have used Adaptive thresholding which creates a threshold based on the image and sets the lower pixels to zero while the higher pixels to 255.
- Step 5: Edge Detection
</br>![image](https://github.com/user-attachments/assets/75a31be7-18f8-48ca-904a-d78d8a1d97d2)
Since the sudoku grid in general is made of 9x9 smaller numbers enclosed by a box, in order to find that box which encloses the number grid, it is necessary to find the edges of the box which are given by the edge detection algorithm. We have usef the canny edge detection algoithm in this case.
- Step 6: Contour Analysis
</br>![image](https://github.com/user-attachments/assets/f1c5298d-e02d-4391-b58a-852220af5aa3)
In an image, we define a contour to be some continuous curve that traverses the boundary of some object. So, since the sudoku grid has a continuous boundary, it also has a contour.
- Step 7: Maximum Contour Extraction
</br>![image](https://github.com/user-attachments/assets/fc81d065-c8bc-4ace-9f34-e4c49fde3812)
</br>![image](https://github.com/user-attachments/assets/e9fe9c6e-d2f2-4800-afd1-1ed40ba31a9e)
Assuming that the user intended to capture the Sudoku, the main grid of the sudoku should be at the focus and therefore, the contour corresponding to the main sudoku grid should enclose the largest amount of area. Therefore, the contour corresponding to the main sudoku grid was cropped and we obtain the image of only the main sudoku grid without the unnecessary background.




