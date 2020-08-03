import cv2
import numpy as np

img=cv2.imread('color detection.png')
img=cv2.resize(img,(500,500)) #resizing the window
# Now convert BGR to HSV format

hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Now make two arrays for low range and high range of BGR color to be detected

low_array=np.array([110,50,50]) #lower array for blue color
high_array=np.array([130,255,255]) #higher array for blue color

mask=cv2.inRange(hsv, low_array, high_array) #this method will find the color in this range

cv2.imshow("original image",img)
cv2.imshow("Detected color",mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
