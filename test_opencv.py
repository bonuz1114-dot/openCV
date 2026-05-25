import cv2

img = cv2.imread('images/ZiJZu.png')
resizeimg = cv2.resize(img, (600,400))
cv2.arrowedLine(resizeimg, (0,0), (300,200), (255,0,0), 4)
cv2.imshow('Image', resizeimg)

cv2.waitKey(0)
cv2.destroyAllWindows()