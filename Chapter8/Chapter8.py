import cv2
import numpy as np

# Đây chỉ là hàm để sắp xếp outcoming images, có thể kh quan tâm
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for i, cnt in enumerate(contours):

        # Sử dụng hierarchy để kiểm tra contour nào có parent (tức là bên trong)
        if hierarchy[0][i][3] != -1:  # Chỉ lấy contour có parent
            area = cv2.contourArea(cnt)
            print(f"Contour {i}: Area = {area}")
            if area > 500:
                cv2.drawContours(contour_img, [cnt], -1, (255, 0, 0), 10)
                peri = cv2.arcLength(cnt, True)
                print(peri)
                approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
                print(len(approx))
                objCor = len(approx)
                x, y, w, h = cv2.boundingRect(approx)

                if objCor == 3:
                    objectType = "Triangle"
                elif objCor == 4:
                    aspRatio = w/float(h)
                    if aspRatio >0.98 and aspRatio <1.03: objectType= "Square"
                    else:objectType="Rectangle"
                elif objCor>4: objectType= "Circles"
                else:objectType="None"

                cv2.rectangle(contour_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(contour_img, objectType, (x + (w//2) - 10, y + (h//2) - 10), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255), 3)

path = "C:\Python\OpenCv_All_In_One\Data_Test\Image\shape_img2.webp"
img = cv2.imread(path)
contour_img = img.copy()

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur_img = cv2.GaussianBlur(gray_img, (7, 7), 1)
canny_img = cv2.Canny(blur_img, 50, 50)
black_img = np.zeros_like(img) 

get_contours(canny_img)

stack_img = stackImages(0.3, ([img, gray_img, blur_img], [canny_img, contour_img, black_img]))

cv2.imshow("Image:", stack_img)
cv2.waitKey(0)