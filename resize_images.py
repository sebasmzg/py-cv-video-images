import cv2 as cv
import glob as gl

images= gl.glob("*.jpg") #busca todas las imagenes en la carpeta actual

for image in images:
    img = cv.imread(image,0)
    resized = cv.resize(img, (100, 100)) #redimensiona la imagen a 100x100
    cv.imshow("image", resized)
    cv.waitKey(1000)
    cv.destroyAllWindows() #cierra todas las ventanas
    cv.imwrite("resized_"+image, resized) #guarda la imagen redimensionada con el prefijo "resized_"
