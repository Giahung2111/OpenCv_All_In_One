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

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
cv2.createTrackbar("Saturation Min", "TrackBars", 110, 255, empty)
cv2.createTrackbar("Saturation Max", "TrackBars", 240, 255, empty)
cv2.createTrackbar("Value Min", "TrackBars", 152, 255, empty)
cv2.createTrackbar("Value Max", "TrackBars", 255, 255, empty)


while True:
    img = cv2.imread("C:\Python\OpenCv_All_In_One\Data_Test\Image\Garbage_Img.png")
    
    # Chuyển ảnh sang không gian màu HSV để dễ dàng xử lý màu sắc.
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Lấy các giá trị từ thanh trượt để điều chỉnh phạm vi màu (Hue, Saturation, Value).
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Saturation Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Saturation Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Value Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Value Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    
    # Tạo một mặt nạ (mask) để giữ lại các pixel trong phạm vi màu được chọn. Lúc này chỉ là ảnh trắng đen !!
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv_img, lower, upper)

    # Áp dụng mặt nạ vào ảnh gốc để có ảnh kết quả chỉ chứa các màu được chọn.
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # In ra
    imgStack = stackImages(0.6,([img,hsv_img],[mask,imgResult]))
    cv2.imshow("Stacked Images", imgStack)

    cv2.waitKey(0)