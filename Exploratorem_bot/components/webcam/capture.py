#thirt-party import
import cv2 as cv

#build-in import

#local import


class WebcamCapture:
    def __init__(self):
        self.capture = cv.VideoCapture(0)
        
    def webcamCapture(self):
        ret, frame = self.capture.read()  # capture frame-by-frame
        if not ret:
            print("Failed to capture webcam.")
            self.release()
            return None
        
        self.release()
        return frame
        
    
    def release(self):
        self.capture.release()