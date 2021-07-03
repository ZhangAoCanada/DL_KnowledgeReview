import cv2
import numpy as np

image1 = cv2.imread("./autodiff.png")
image2 = cv2.imread("./reverseautodiff.png")

x_size = min(image1.shape[0], image2.shape[1])

scale1 = x_size / image1.shape[0]
scale2 = x_size / image2.shape[0]


image1 = cv2.resize(image1, None, fx=scale1, fy = scale1)
image2 = cv2.resize(image2, None, fx=scale2, fy = scale2)

image = np.concatenate([image1, image2], axis = 1)

cv2.imwrite("./autodiffcombine.png", image)