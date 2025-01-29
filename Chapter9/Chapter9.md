# Chapter 9: Face Detection

```python
import cv2

# Tải tệp Haar Cascade XML cho phát hiện khuôn mặt
faceCascade = cv2.CascadeClassifier("C:\Python\OpenCv_All_In_One\Data_Test\haarcascade_frontalface_default.xml")
img = cv2.imread("C:\Python\OpenCv_All_In_One\Data_Test\Image\z6266075397150_16b24e1aa8c8db2741a6daf1571a2276.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Phát hiện khuôn mặt trong ảnh xám
# Tham số:
# - gray_img: ảnh đầu vào (ảnh xám)
# - 1.1: scaleFactor - tỉ lệ thu nhỏ hình ảnh tại mỗi bước, giúp phát hiện đối tượng ở các kích cỡ khác nhau
# - 4: minNeighbors - số vùng lân cận tối thiểu để xác định khu vực là một khuôn mặt
faces = faceCascade.detectMultiScale(gray_img, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

cv2.imshow("Image:", img)
cv2.waitKey(0)
```