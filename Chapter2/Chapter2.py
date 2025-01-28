import cv2
import numpy as np

img = cv2.imread("C:\Python\OpenCv_All_In_One\Data_Test\Image\Garbage_Img.png")
kernel = np.ones((3, 3), np.uint8)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur_img = cv2.GaussianBlur(gray_img, (7, 7), 0)
canny_img = cv2.Canny(img, 100, 100)
dilation_img = cv2.dilate(canny_img, kernel, iterations=1)
Eroded_img = cv2.erode(dilation_img, kernel, iterations=1)

cv2.imshow("Gray_img:", gray_img)
cv2.imshow("Blur_img:", blur_img)
cv2.imshow("Canny_img:", canny_img)
cv2.imshow("Dilation_img:", dilation_img)
cv2.imshow("Eroded_img:", Eroded_img)
cv2.waitKey(0)