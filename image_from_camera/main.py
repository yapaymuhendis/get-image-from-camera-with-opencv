import cv2

cap = cv2.VideoCapture("videos/video.mp4")
# To get video from camera: cv2.VideoCapture(0)
# For external camera: cv2.VideoCapture(1)


while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 0)
    # We use cv2.flip because the output looks upside down.
    # If you use your own camera instead of video, you don't need to write cv2.flip.
    

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # here, we processed the frame, that is, the image read in the cap, as the frame, for example, we made it gray.

    cv2.imshow("webcam", gray_frame)
   
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    # When I press the q key, I say stop the program from running.

cap.release()
# I'm done with the video, I mean release it here.

cv2.destroyAllWindows()




