import cv2 as cv


class webcamLive:
    def __init__(self):
        self.capture = cv.VideoCapture(0) # Use default webcam
        self.face_cascade = cv.CascadeClassifier('.\Exploratorem_CL\Webcam\webcam_live\haarcascade_frontalface_default.xml')

    def webcam(self):

        # Capture frame-by-frame
        ret, frame = self.capture.read()

        # Check if the frame was successfully captured
        if not ret:
            print("Error: Failed to capture frame from camera.")
            return None

        # Convert the frame to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)


        # Detect faces in the grayscale frame
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Draw a rectangle around each face
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        return frame
            
    def start(self):
        while True:
            frame = self.webcam()
            cv.imshow('Webcam', frame)
            if cv.waitKey(1) == ord('q'): # Press q to quit
                break

        self.capture.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    live = webcamLive()
    live.start()


