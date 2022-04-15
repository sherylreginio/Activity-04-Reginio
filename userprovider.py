import cv2
import os

while True:
	Fn = input("Name of your file[put '.jpg' at the end of the name]: ")
	Flag = input("\n press [1] for colored image or [0] for gray image: ")

	if os.path.exists(Fn) and Flag == '1':
		img= cv2.imread(Fn, 1)
		cv2.imshow(Fn, img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		break

	elif os.path.exists(Fn) and Flag == '0':
		img= cv2.imread(Fn, 0)
		cv2.imshow(Fn, img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		break

	else:
		print("File name doesn't exist! ")
