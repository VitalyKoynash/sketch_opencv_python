#http://habrahabr.ru/post/148692/
import numpy as np
import cv2
import time
from PIL import ImageGrab

current_milli_time = lambda: int(round(time.time() * 1000))
frame_time=current_milli_time()


def millis():
    global frame_time
    millis.old_time=frame_time
    frame_time=current_milli_time()
    return frame_time-millis.old_time

frame = ImageGrab.grab()

#cap = cv2.VideoCapture(0)
## Define the codec and create VideoWriter object
#fourcc=NU
#fourcc=-1
#fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
fourcc = cv2.cv.CV_FOURCC('X','V','I','D')
#fourcc = cv2.cv.CV_FOURCC('M','P','G','4')
#cv2.VideoWriter( VideoWriter_fourcc(*'MPG4')
out = cv2.VideoWriter('i:/output.avi',fourcc, 8.0, (frame.size[0],frame.size[1]))
flag = False
while(True):

    millis()
    frame = ImageGrab.grab()
    
    #print 'grub ', millis(), 'ms'
    #ret, frame = cap.read()
    ret=True
    if ret==True:
        #frame = cv2.flip(frame,0)
        
        #millis()
       
        #printscreen_numpy =   np.array(frame.getdata(),dtype=np.uint8)\
        printscreen_numpy =   np.asarray(frame)\
        .reshape((frame.size[1],frame.size[0],3)) 
    
        frame = cv2.cvtColor(printscreen_numpy,cv2.COLOR_BGR2RGB) #http://stackoverflow.com/questions/4661557/pil-rotate-image-colors-bgr-rgb
        #print 'printscreen_numpy ', millis(), 'ms'

        # write the flipped frame
        #millis()
        out.write(frame)
        #print 'write ', millis(), 'ms'
        
        if flag == False:
            flag = True
            #millis()
            cv2.imshow('frame',frame)
            #print 'show ', millis(), 'ms'

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        print 'printscreen_numpy ', millis(), 'ms'
    else:
        break

# Release everything if job is finished
#cap.release()
out.release()
cv2.destroyAllWindows()