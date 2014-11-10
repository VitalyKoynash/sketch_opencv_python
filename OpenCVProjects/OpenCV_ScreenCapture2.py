import cv2
from cv2 import adaptors
from cv2 import cv
from cv2 import highgui
import win32gui, win32ui, win32con, win32api
import PIL.Image, PIL.ImageGrab, time
def capture_window(hwnd):
    global iplimage
    try:
        del iplimage
    except:
        pass
    if not hwnd:
        raise 'Window not found'
    t0=time.clock()
    # compute height h and width w
    l,t,r,b=win32gui.GetWindowRect(hwnd)
    h=b-t
    w=r-l
    # get DrawCanvas of the window
    hwndDC = win32gui.GetWindowDC(hwnd)
    # create the DC from handle
    mfcDC=win32ui.CreateDCFromHandle(hwndDC)
    # create compatible DC from it
    saveDC=mfcDC.CreateCompatibleDC()
    # create PyCBitmap
    saveBitMap = win32ui.CreateBitmap()
    # create compatible bitmap with width w and height h
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    # screencopy the contents
    saveDC.BitBlt((0,0),(w, h) , mfcDC, (0,0), win32con.SRCCOPY)
    # get the bitmap info
    bmpinfo = saveBitMap.GetInfo()
    # get the string of image data
    bmpstr = saveBitMap.GetBitmapBits(True)
    # win32gui.ReleaseDC(hwnd, mfcDC)
    # win32gui.ReleaseDC(hwnd, saveDC)
    del mfcDC
    del saveDC
    del saveBitMap
    # convert it to PIL image
    im = PIL.Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
    # convert it to IPL image
    iplimage = adaptors.PIL2Ipl(im)
    del im
    t = time.clock()
    return [iplimage, float(t-t0)]

if __name__ == '__main__':
    MPEG4 = 0x58564944
    fps = 8
    hwnd = win32gui.GetForegroundWindow()
    l,t,r,b = win32gui.GetWindowRect(hwnd)
    [iplimage, t] = capture_window(hwnd)
    frame_size = cv.cvGetSize (iplimage)
    writer = highgui.cvCreateVideoWriter ("i:/captured.avi", MPEG4,
    fps, frame_size, True)
    i = 0
    while 1:
        print i,
        i = i + 1
        [iplimage, t] = capture_window(hwnd)
        highgui.cvWriteFrame (writer, iplimage)
        k = highgui.cvWaitKey (1)
        print k
        if k == '\x1b':
            break
highgui.cvReleaseVideoWriter (writer)