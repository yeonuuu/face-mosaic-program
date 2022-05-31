import cv2

img = cv2.imread("person.jpg", cv2.IMREAD_GRAYSCALE)



cv2.imshow('Gray scaled', img)


cv2.waitKey()