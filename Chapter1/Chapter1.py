import cv2

# img = cv2.imread("C:\Python\OpenCv_All_In_One\Data_Test\Image\Garbage_Img.png")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture("C:\Python\OpenCv_All_In_One\Data_Test\Video\Quay màn hình 2024-12-20 221004.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

cap = cv2.VideoCapture(0) #Khoi tao mac dinh webcam la 0
cap.set(3, 640) #Đặt chiều rộng của video là 640 pixels.
cap.set(4, 480) #Đặt chiều cao của video là 480 pixels.
cap.set(10, 100)
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break