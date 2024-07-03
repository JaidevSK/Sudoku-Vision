import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, morphology, img_as_bool, segmentation
from scipy import ndimage as ndi
import operator
import tensorflow as tf
model = tf.keras.models.load_model("model/model.keras")

def basic_preprocessing(img):
    img_plt = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    x, y = max(img.shape[0]//200, 5), max(img.shape[1]//200, 5)
    clahe = cv2.createCLAHE(clipLimit=0.8, tileGridSize=(x,y))
    enhanced = clahe.apply(img_plt)
    x, y = max(img.shape[0]//200, 3), max(img.shape[1]//200, 3)
    blurred = cv2.GaussianBlur(enhanced, (x+(x+1)%2, y+(y+1)%2), 0)
    blurred = cv2.bilateralFilter(blurred,7,75,75)
    return blurred

def to_binary(img):
    se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, se)
    thresholded_img = cv2.adaptiveThreshold(opened, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,2)
    inverted = cv2.bitwise_not(thresholded_img)
    return inverted

def fill_gaps(img, iterations=2):
  for i in range(iterations):
    out = ndi.distance_transform_edt(~img)
    out = out < 0.05 * out.max()
    out = morphology.skeletonize(out)
    out = segmentation.clear_border(out)
    out = np.array(out*255, dtype=np.uint8)
    out = cv2.bitwise_or(np.uint8(out), img)
    img = out
  return out


def perspective_transform(image, corners):

    def order_corner_points(corners):
        bottom_r, _ = max(enumerate([pt[0][0] + pt[0][1] for pt in corners]), key=operator.itemgetter(1))
        top_l = (bottom_r + 2)%4
        left_corners = [corners[i] for i in range(len(corners)) if((i!=bottom_r) and (i!=top_l))]
        bottom_l, _ = min(enumerate([pt[0][0] - pt[0][1] for pt in left_corners]), key=operator.itemgetter(1))
        top_r = (bottom_l + 1)%2
        return (corners[top_l][0], left_corners[top_r][0], corners[bottom_r][0], left_corners[bottom_l][0])
    
    ordered_corners = order_corner_points(corners)
    top_l, top_r, bottom_r, bottom_l = ordered_corners
    width_A = np.sqrt(((bottom_r[0] - bottom_l[0]) ** 2) + ((bottom_r[1] - bottom_l[1]) ** 2))
    width_B = np.sqrt(((top_r[0] - top_l[0]) ** 2) + ((top_r[1] - top_l[1]) ** 2))
    width = max(int(width_A), int(width_B))
    height_A = np.sqrt(((top_r[0] - bottom_r[0]) ** 2) + ((top_r[1] - bottom_r[1]) ** 2))
    height_B = np.sqrt(((top_l[0] - bottom_l[0]) ** 2) + ((top_l[1] - bottom_l[1]) ** 2))
    height = max(int(height_A), int(height_B))
    dimensions = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]], dtype = "float32")
    ordered_corners = np.array(ordered_corners, dtype="float32")
    matrix = cv2.getPerspectiveTransform(ordered_corners, dimensions)
    return cv2.warpPerspective(image, matrix, (width, height))


def centering_se(shape: tuple, shape_ones: (int, int)):
  x = np.zeros(shape)
  assert (shape_ones[0] < shape[0]) and (shape_ones[1] < shape[1])
  width = shape_ones[0]
  height = shape_ones[1]
  
  rows, cols = shape
  for i in range(width):
    for j in range(height):
      x[i][j], x[rows-1-i][j], x[i][cols-1-j], x[rows-1-i][cols-1-j] = 1, 1, 1, 1
  return x

def recentre(img: np.ndarray, prev_center: tuple, h_se: np.ndarray, v_se: np.ndarray, h_mov_range: (int, int), v_mov_range: (int, int)):
  # reference: https://web.stanford.edu/class/ee368/Project_Spring_1415/Reports/Wang.pdf
  max_res, max_center = 0, prev_center

  for i in range(v_mov_range[0], v_mov_range[1]):
    curr_center = (prev_center[0] + 0, prev_center[1] + i)
    start_row = max(curr_center[1] - v_se.shape[0]//2, 0)
    start_col = max(curr_center[0] - v_se.shape[1]//2, 0)
    partial = img[start_row:start_row+v_se.shape[0], start_col:start_col+v_se.shape[1]]

    curr_dot = np.sum(partial*(v_se[0:partial.shape[0], 0:partial.shape[1]]))
    # curr_dot = np.sum(img[x1:x1+v_se.shape[0], y1:y1+v_se.shape[1]]*(v_se))
    # print(curr_center, curr_dot)
    if max_res < curr_dot:
      max_res = curr_dot
      max_center = curr_center

  # # print("max_center after v_se: ", max_center)
  prev_center = max_center
  max_res = 0
  for i in range(h_mov_range[0], h_mov_range[1]):
    curr_center = (prev_center[0] + i, prev_center[1] + 0)
    start_row = max(curr_center[1] - h_se.shape[0]//2, 0)
    start_col = max(curr_center[0] - h_se.shape[1]//2, 0)
    partial = img[start_row:start_row+h_se.shape[0], start_col:start_col+h_se.shape[1]]

    curr_dot = np.sum(partial*(h_se[0:partial.shape[0], 0:partial.shape[1]]))
    # print(curr_center, curr_dot)
    if max_res < curr_dot:
      max_res = curr_dot
      max_center = curr_center
      
  # print("max_center after h_se: ", max_center)
  return max_center

def preprocess_digit(digit_img):
  digit_img[0:3,:] = 0
  digit_img[:,0:3] = 0
  digit_img[-3:,:] = 0
  digit_img[:,-3:] = 0
  return digit_img

def predict_digit(digit_img):
    img = cv2.resize(digit_img, (28, 28))
    img = np.array(img).reshape(-1, 28, 28, 1)
    predictions = model.predict(img)
    return np.argmax(predictions)

def predict_sudoku(digits: list):
  sudoku = []
  for digit in digits:
    if np.sum(digit) > 255*30:
      sudoku.append(predict_digit(digit))
    else:
      sudoku.append(0)
  return sudoku

def convert_board(orig_img):
    assert(orig_img.shape[0] > 200) and (orig_img.shape[1] > 200)
    inp_img = basic_preprocessing(orig_img)
    ret_img = to_binary(inp_img)
    kernel = np.ones((2,2))
    eroded = cv2.erode(ret_img, kernel, iterations=1)
    refined_img = fill_gaps(ret_img, iterations=4)
    contours, hierarchy = cv2.findContours(eroded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    main_contour = max(contours, key=cv2.contourArea)
    peri = cv2.arcLength(main_contour, True)
    approx = cv2.approxPolyDP(main_contour, 0.1 * peri, True)
    transformed_processed = perspective_transform(eroded, approx[0:4])
    transformed_orig = perspective_transform(orig_img, approx)
    test = transformed_processed.copy()
    test_orig = transformed_orig.copy()
    lines_X = np.linspace(0, test.shape[1], num=10, dtype=int)
    lines_Y = np.linspace(0, test.shape[0], num=10, dtype=int)
    centers_X = [(lines_X[i] + lines_X[i-1])//2 for i in range(1, len(lines_X))]
    centers_Y = [(lines_Y[i] + lines_Y[i-1])//2 for i in range(1, len(lines_Y))]
    centers = [(centers_X[i], centers_Y[j]) for i in range(len(centers_X)) for j in range(len(centers_Y))]
    kernel_shape = (centers_X[1] - centers_X[0], centers_Y[1] - centers_Y[0])
    ones_length = (kernel_shape[0]+kernel_shape[1])//20
    v_se = centering_se(kernel_shape, (2,ones_length))
    h_se = centering_se(kernel_shape, (ones_length,2))
    tt = test_orig.copy()
    new_centers = []
    for i in range(len(centers)):
      v_mov_range, h_mov_range = (-kernel_shape[0]//8, kernel_shape[0]//8), (-kernel_shape[1]//8, kernel_shape[1]//8)
      if (i<9)            : h_mov_range = (-kernel_shape[1]//64, kernel_shape[1]//8)
      elif (i>71)         : h_mov_range = (-kernel_shape[1]//8, kernel_shape[1]//64)
      if (i%9 == 0)       : v_mov_range = (-kernel_shape[0]//64, kernel_shape[0]//8)
      elif ((i+1)%9 == 0) : v_mov_range = (-kernel_shape[0]//8, kernel_shape[0]//64)
      new_centers.append(recentre(transformed_processed, centers[i], h_se, v_se, h_mov_range, v_mov_range))
    i=0
    digits = []
    for center in new_centers:
      top_l = [center[0]-kernel_shape[1]//2, center[1]-kernel_shape[0]//2]
      top_r = [center[0]+kernel_shape[1]//2, center[1]-kernel_shape[0]//2]
      bottom_l = [center[0]-kernel_shape[1]//2, center[1]+kernel_shape[0]//2]
      bottom_r = [center[0]+kernel_shape[1]//2, center[1]+kernel_shape[0]//2]
      M = cv2.getPerspectiveTransform(np.float32([top_l, top_r, bottom_l, bottom_r]), np.float32([[0,0], [28,0], [0,28], [28,28]]))
      dst = cv2.warpPerspective(transformed_processed,M,(28,28))
      dst_mod = preprocess_digit(dst)
      if(np.sum(dst_mod) > 255*30):
        digits.append(dst_mod)
      else:
        digits.append(np.zeros(dst_mod.shape))
      i+=1
    sudoku = predict_sudoku(digits)
    sudoku = np.array(sudoku).reshape(9,9)
    sudoku = np.transpose(sudoku)
    sudoku = sudoku.tolist()
    return sudoku
