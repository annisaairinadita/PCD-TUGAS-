import cv2

image = cv2.imread("D:\SEMESTER 4\PENGOLAHAN CITRA DIGITAL\pythonProject2\mammogram.tif", 0)
img_1 =  255 - image

cv2.imshow("Original Image", image)
cv2.imshow("Image Negative", img_1)

cv2.waitKey(0)
cv2.destroyWindow()