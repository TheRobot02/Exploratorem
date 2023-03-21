import cv2 as cv

class webcamCapture:
    def __init__(self):
        self.capture = cv.VideoCapture(0)
        
    def capture(self):
        ret, frame = self.capture.read()  # capture frame-by-frame
        if not ret:
            print("Failed to capture webcam.")
            return None
        
        return frame
    
    def release(self):
        self.capture.release()