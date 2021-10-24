import cv2
import dlib

#choses camera
camera_id = 0
#capture the image
cap = cv2.VideoCapture(camera_id)

while True:
    #read the image
    ret, frame = cap.read()
    #convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #find center
    (h, w) = frame.shape[:2]
    center = (int(w/2), int(h/2))
    #dilb load face detector
    face_detector = dlib.get_frontal_face_detector()
    #find landmark
    faces = face_detector(gray)

    #for loop
    for face in faces:
        x1 = face.left() #left point
        y1 = face.top() #top point
        x2 = face.right() #right point
        y2 = face.bottom() #bottom point

        if (x1 < center[0] and x2 > center[0]):
            # FORWARD
            if (y2 < center[1]):
                print("FORWARD")
            # BACKWARD
            if (y1 > center[0]):
                print("BCKWARD")
        if (y1 < center[1] and y2 > center[1]):
            # LEFT
            if (x2 < center[0]):
                print("TURN LEFT")
            # RIGHT
            if (x1 > center[0]):
                print("TURN RIGHT")

        #draw rectangle
        cv2.rectangle(img = frame, pt1 = (x1, y1), pt2 = (x2, y2),
                      color = (0, 255, 0), thickness = 3)
        break

    if ret:
        cv2.imshow("Cam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cap.destroyAllWindows()
