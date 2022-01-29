import cv2

def take_snapshot():
    videocaptureO=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptureO.read()
        cv2.imwrite("newpictue1.jpg",frame)
        result=False
    videocaptureO.release()
    cv2.destroyAllWindows()
take_snapshot()