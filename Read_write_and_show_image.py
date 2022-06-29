
import cv2 as cv # adding opencv library to the code
# reading any image using path of the image and "r" is used to convert normal string to raw string
img = cv.imread(r"C:\Users\SHRAWAN PRO\Desktop\College book\benz.jpg") 

cv.imshow("benz",img) # showing image 
cv.waitKey(1000) # waitKey wait for any key to press, if nothing in '()', and then 
cv.destroyAllWindows() # destroyAllWindows close the the windows

print(img.shape) #print the shape of image e.g. [width, height, colors] bcz image is a 3-dimensional array/tensor (https://codecraft.tv/courses/tensorflowjs/tensors/what-are-tensors/)

cv.imwrite("benz_1.jpg",img) # writing image or Save each frame using cv2.imwrite()
img = cv.imread("./benz_1.jpg") # reading any image in same directory
cv.imshow("benz_1",img) 
cv.waitKey(1000)
cv.destroyAllWindows()

grey_benz = cv.cvtColor(img,cv.COLOR_BGR2GRAY) # converting color of any image BGR to black & white or (gray)
img = cv.imshow("benz",grey_benz)
cv.waitKey()
cv.destroyAllWindows()
print(grey_benz.shape)

img = cv.imread("./benz_1.jpg")
B,G,R = cv.split(img) #spliting color in blue, green and red
print(B.shape)
cv.imshow("original_benz",img) # showing original image
cv.imshow("Blue_benz",B) # showing image with highting blue color in grayscale color.
cv.imshow("Green_benz",G) # showing image with highting Green color in grayscale color.
cv.imshow("Red_benz",R) # showing image with highting red color in grayscale color.
cv.waitKey()
cv.destroyAllWindows()

merge = cv.merge([B+100,G+100,R+100]) # merging splited image
cv.imshow("merged image",merge) 
cv.waitKey()
cv.destroyAllWindows()

