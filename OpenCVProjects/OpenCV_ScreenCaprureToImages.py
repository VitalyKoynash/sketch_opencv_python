'''
fourcc ? ??? ?????, ????? ?????, ????????? ??????????? ?????????????????? ????? ?????? ? ???????? ??????. 
????????, CV_FOURCC('P','I','M,'1') ? ??? ?????? MPEG-1. ? ????? ????? ???????? -1 ??? ?????? 
?????? ???????????? ? ?????????? ???? ??? 0 ??? ?????? ??? 
?????? (?????? ????? ????????? ???-??!). ????????? Elsedar ????????????, 
??? ????? ?????????? ?????? ?????? ???????: www.fourcc.org/codecs.php 
'''

#import numpy as np
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

## fullscreen
frame = ImageGrab.grab()

printscreen_numpy =   np.array(frame.getdata(),dtype=np.uint8)\
.reshape((frame.size[1],frame.size[0],3)) 
cv2.imshow('frame',printscreen_numpy)

idx = 0
while(True):

    millis()
    frame = ImageGrab.grab()
    name = 'i:/screen/screenshot%0*d.jpg' % (3, idx)
    idx=idx+1
    frame.save(name, "JPEG") #"i:/screen/screenshot.jpg"
    print 'grub ', millis(), 'ms'

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()