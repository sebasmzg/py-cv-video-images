import cv2
import cv2 as cv

face_cascade = cv.CascadeClassifier('Files/haarcascade_frontalface_default.xml')

img = cv.imread('Files/news.jpg')
img = cv.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2))) ##redimensiona la imagen a la mitad de su tamaño
##es más preciso si se usa escala de grises
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces= face_cascade.detectMultiScale(gray_img,
                                     scaleFactor=1.1, ##un valor mayor a 1 significa que la imagen se reduce, si se reduce demasiado, no detecta nada
                                     minNeighbors=5, ##cuantos más vecinos, más preciso, pero si es muy alto, no detecta nada
                                     )
#print(faces)
#print(type(faces)) ##numpy array con 4 elementos, x, y, w, h

for (x, y, w, h) in faces:
    img= cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) ##dibuja un rectangulo en la imagen
    ##(x, y) es la esquina superior izquierda del rectangulo
    ##(x+w, y+h) es la esquina inferior derecha del rectangulo
    ##(0, 255, 0) es el color del rectangulo (verde)
    ##2 es el grosor del rectangulo

cv.imshow("gray", img)
cv.waitKey(0)
cv.destroyAllWindows()