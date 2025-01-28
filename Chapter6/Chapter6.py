import cv2
import numpy as np

img = cv2.imread("C:\Python\OpenCv_All_In_One\Data_Test\Image\Garbage_Img.png")

hor_img = np.hstack((img, img, img))
ver_img = np.vstack((img, img))

cv2.imshow("Horizontal:", hor_img)
cv2.imshow("Vertical:", ver_img)
cv2.waitKey(0)

