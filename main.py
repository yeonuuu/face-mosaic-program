import cv2

img = cv2.imread('person.jpg')

cv2.imshow('original image', img)


def blur(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)


def blur_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = blur(dst[y:y + height, x:x + width], ratio)
    return dst


cv2.imshow('blured image', blur(img))

cv2.waitKey()
