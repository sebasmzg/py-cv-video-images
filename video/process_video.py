import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv.VideoCapture(0) ##0 es la cámara default, 1 es la segunda cámara...

while True:
    check, frame = video.read() ##lee un frame de la cámara
    if not check: break
    #print(check) ##boolean que indica si se leyó correctamente el frame
    #print(frame) ##imprime el frame

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces= face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        if len(faces) > 0:
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv.imshow("Capturing", frame)


    key = cv.waitKey(1)
    if key == ord('q'): ##si se presiona la tecla 'q' se sale del bucle
        break

video.release() ##libera la cámara
cv.destroyAllWindows()
