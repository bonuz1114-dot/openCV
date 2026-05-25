import cv2

img = cv2.imread('images/ZiJZu.png')
resizeimg = cv2.resize(img, (600,400))
cv2.arrowedLine(resizeimg, (0,0), (300,200), (255,0,0), 4)
cv2.rectangle(resizeimg, (200,100), (500,400), (0,0,255), 5)
cv2.circle(resizeimg, (300,200), 10, (0,255,0), -1)
cv2.imshow('Image', resizeimg)

cv2.waitKey(0)
cv2.destroyAllWindows()