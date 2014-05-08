import cv2
import os

path = ''
for roots,dirs,files in os.walk(path):
	pass

pics=files	
cv2.namedWindow("Image",0)
cv2.setWindowProperty("Image",0,1)

for pic in pics:
	img=cv2.imread(pic)
	cv2.imshow("Image",img)
	cv2.waitKey(500)
cv2.destroyAllWindows()
