import cv2

faceCascade = cv2.CascadeClassifier("C:\Python\OpenCv_All_In_One\Data_Test\haarcascade_frontalface_default.xml")
img = cv2.imread("C:\Python\OpenCv_All_In_One\Data_Test\Image\z6266075397150_16b24e1aa8c8db2741a6daf1571a2276.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray_img, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)


cv2.imshow("Image:", img)
cv2.waitKey(0)