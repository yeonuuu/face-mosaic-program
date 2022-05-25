import cv2

img = cv2.imread('couple.jpg')

cv2.imshow('original image', img)


def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)


def mosaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst

#얼굴 인식 파일 읽음
face_cascade = cv2.CascadeClassifier('haarcascade_frontface.xml')

dst = img


faces = face_cascade.detectMultiScale(dst, 1.1, 4)

#인식된 얼굴 갯수 출력
print('number of faces are', len(faces))

#얼굴에 사각형 출력
for (x, y, w, h) in faces:
    dst = mosaic_area(dst, x, y, w, h, 0.1)

cv2.imshow('result img', dst)

cv2.waitKey()
