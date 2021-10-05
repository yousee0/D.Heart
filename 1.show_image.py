import cv2

img_basic = cv2.imread('heart1.jpg', cv2.IMREAD_COLOR)
cv2.imshow('preview', img_basic)
cv2.waitKey(0)
cv2.imwrite('result1.jpg', img_basic)
#print(cv2.__version__)

