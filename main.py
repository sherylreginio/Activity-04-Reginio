import cv2
filepath = "3.jpg"
image = cv2.imread(filepath,1)
cv2.imshow("sheryl",image)
cv2.waitKey(0)
cv2.destroyAllWindows()