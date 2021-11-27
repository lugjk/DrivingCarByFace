import cv2
import dlib

#choses camera
camera_id = 0
#capture the image
cap = cv2.VideoCapture(camera_id)

    #read the image
    ret, frame = cap.read()
    #convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #get height and width
    (h, w) = frame.shape[:2]
    # division of areas
    h1=h*1/3
    h2=h*2/3
    w1=w*1/3
    w2=w*2/3
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
        
        c=(int ((x1[0]+x2[0])/2), int ((y1[1]+y2[1])/2))
        
        # forward and back
            if (c[0] <h1 ):
                key="w"
            elif (c[0] > h2):
                key="x"
            else
                key="s"
            
            if (c[1] < w1):
                key1="a"
            # RIGHT
            elif (c[1] > w2):
                key1="d"
            else
                key1="s"

        #draw rectangle
        cv2.rectangle(img = frame, pt1 = (x1, y1), pt2 = (x2, y2),
                      color = (0, 255, 0), thickness = 3)
        break

    if ret:
        cv2.imshow("Cam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   

cap.release()
