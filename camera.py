import cv2
import cv

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0) # 0 stands for camera #0
        self.video.set(cv.CV_CAP_PROP_FRAME_WIDTH, 640);
        self.video.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 480);
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tostring()