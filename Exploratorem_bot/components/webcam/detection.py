#thirt-party import
import cv2 as cv
import asyncio

#build-in import

#local import


class WebcamDetection:
    def __init__(self):
        self.capture = cv.VideoCapture(0) # Use default webcam
        self.face_cascade = cv.CascadeClassifier('Exploratorem_bot\components\webcam\haarcascade_frontalface_default.xml')

    def scanning(self):

        # Capture frame-by-frame
        success, frame = self.capture.read()

        # Check if the frame was successfully captured
        if not success:
            print("Error: Failed to capture frame from camera.")
            return None

        # Convert the frame to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)


        # Detect faces in the grayscale frame
        self.faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Draw a rectangle around each face
        for (x, y, w, h) in self.faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        return frame
            
    def webcam(self):
        print("Detection started!")
        while True:           
            frame = self.scanning()
            if frame is not None:
                if len(self.faces) > 0:
                    print("USER DETECTED!")
                    userDetected = True
                    break
              
        self.capture.release()
        cv.destroyAllWindows()
        return userDetected
    
    async def webcam_detection(self, ctx):
        loop = asyncio.get_event_loop()
        user_detected = await loop.run_in_executor(None, self.webcam)
        if user_detected == True:
             await ctx.send(f"[+] User has returned!")
        else:
            await ctx.send(f"[!] Error")


