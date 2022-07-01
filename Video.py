import cv2 as cv
import datetime

image = cv.VideoCapture(0) # Open video file or image file sequence or a capturing device or a IP video stream for video capturing.
# In order to encode the video in Python, a four characters string is used to define the coding method.
# Define the codec and create VideoWriter object
fourcc_code = cv.VideoWriter_fourcc(*"XVID") #XVID OR ('X','V','I','D')
'''
cv2.VideoWriter( filename, fourcc, fps, frameSize )
The parameters are :
filename: Specifies the name of the output video file.
fourcc: (for recording) Defining the codec
fps: Defined frame rate of the output video stream
frameSize: Size of the video frames
'''
video = cv.VideoWriter("my video_1.avi",fourcc_code,30,(1280,720))

image.set(3, 3000)
image.set(4, 3000)

print(image.get(cv.CAP_PROP_FRAME_WIDTH))
print(image.get(cv.CAP_PROP_FRAME_HEIGHT))


print(image.isOpened())
while(image.isOpened()):
    check,frame=image.read()
    # video capture properties (https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d)
    #frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    text = 'Width :' + str(image.get(3)) + 'Height :' + str(image.get(4))
    date_time = str(datetime.datetime.now())
    frame = cv.putText(frame, date_time, (10,60), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2)
    video.write(frame)
    cv.imshow("my image",frame)
    if cv.waitKey(1) == ord("q"):
        break

    print(frame.shape)

    cv.imwrite("my image.jpg",frame)
video.release() # release the video capture object
image.release() # release the image capture object
cv.destroyAllWindows()
