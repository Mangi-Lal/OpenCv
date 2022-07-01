# contours means boundary/border of any object
import numpy as np
import cv2 as cv

original_image = cv.imread("./smarties.png")
image=cv.cvtColor(original_image,cv.COLOR_BGR2HSV) # hue saturation value (HSV)

#ret,image=cv.threshold(image,170,225,0)
#image=cv.Canny(image,30,70)

lr=np.array((0,70,70))
ur=np.array((10,255,255))
mask1=cv.inRange(image,lr,ur)

lr=np.array((170,70,70))
ur=np.array((180,255,255))
mask2=cv.inRange(image,lr,ur)

mask=mask1+mask2

contours,hierarchy=cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
cv.drawContours(original_image,contours,-1,(200,100,0),5)

print(len(contours))
cv.imshow("original",original_image)
cv.waitKey()
cv.destroyAllWindows()
