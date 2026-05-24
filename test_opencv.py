import cv2

cap = cv2.VideoCapture('images/2026-04-05 15-37-57.mp4')

while True:
    ref, frame = cap.read()
    cv2.imshow("frame", frame)
    if  ref:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()