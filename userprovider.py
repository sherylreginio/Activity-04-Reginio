import cv2
import os

while True:
	Fn = input("Name of your file[put '.jpg' at the end of the name]: ")

	if os.path.exists(Fn):
		img= cv2.imread(Fn, 1)
		cv2.imshow(Fn, img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		break

	else:
		print("File name doesn't exist! ")
