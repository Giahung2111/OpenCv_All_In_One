# Chapter 1: Read Images Video and Webcams
## I. Introduction to Images
- Some examples: 
  - VGA = 640 x 480
  - HD = 1280 x 720
  - FHD = 1920 x 1080
  - 4K = 3840 x 2160
## II. Read Images-Videos-Webcam
### 1. Read Images
``` python
import cv2

img = cv2.imread("C:\Python\OpenCv_All_In_One\Data_Test\Garbage_Img.png")
cv2.imshow("Output", img)
cv2.waitKey(0)
```
### 2. Read Videos
``` python
import cv2

cap = cv2.VideoCapture("C:\Python\OpenCv_All_In_One\Data_Test\Video\Quay màn hình 2024-12-20 221004.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

### 3. Read Webcams
```python
cap = cv2.VideoCapture(0) #Khoi tao mac dinh webcam la 0
cap.set(3, 640) #Đặt chiều rộng của video là 640 pixels.
cap.set(4, 480) #Đặt chiều cao của video là 480 pixels.
cap.set(10, 100)
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```
- Some common parameters:
  - cap.set(0, value) - Camera index: Chỉ định chỉ mục của webcam. Mặc định là 0 cho webcam đầu tiên, bạn có thể thay đổi nếu có nhiều webcam.

  - cap.set(3, value) - Width (chiều rộng): Điều chỉnh chiều rộng của khung hình.

  - cap.set(4, value) - Height (chiều cao): Điều chỉnh chiều cao của khung hình.

  - cap.set(10, value) - Brightness (độ sáng): Điều chỉnh độ sáng của webcam.

  - cap.set(11, value) - Contrast (độ tương phản): Điều chỉnh độ tương phản của hình ảnh.

  - cap.set(12, value) - Saturation (độ bão hòa): Điều chỉnh độ bão hòa màu sắc.

  - cap.set(13, value) - Hue (màu sắc): Điều chỉnh tông màu của hình ảnh.

  - cap.set(14, value) - Gain: Điều chỉnh mức độ khuếch đại tín hiệu hình ảnh.

  - cap.set(15, value) - Exposure: Điều chỉnh mức độ phơi sáng của camera.

  - cap.set(16, value) - Auto exposure: Bật/tắt chế độ phơi sáng tự động.

  - cap.set(17, value) - Auto white balance: Bật/tắt chế độ cân bằng trắng tự động.

  - cap.set(18, value) - Fog (sương mù): Điều chỉnh mức độ sương mù (chỉ áp dụng với một số loại webcam).