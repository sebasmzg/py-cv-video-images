import cv2

##recibe 3 parametros, filename, flags
#flags es un entero que indica el modo de lectura
# 0: leer la imagen en escala de grises
# 1: leer la imagen en color
# -1: leer la imagen en color, incluyendo el canal alpha
#canal alpha es el canal de transparencia

## el tipo de dato es un numpy array
img = cv2.imread('galaxy.jpg',0)
img2 = cv2.imread('galaxy.jpg',1)
img3 = cv2.imread('galaxy.jpg',-1)

print(f'shape: {img.shape}') #tamaño de la imagen
print(f'type: { type(img)}')
print(f'img: {img}')
print(f'img ndim {img.ndim}') #ndim es el numero de dimensiones

resized_image = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

#cv2.imshow('galaxy1',img)
#cv2.imshow('galaxy2',img2)
cv2.imshow( 'galaxy',resized_image)
cv2.imwrite("galaxy_resized.jpg",resized_image) #guarda la imagen en el disco

#cv2.waitKey(2000) #espera 2000ms para cerrar la ventana
cv2.waitKey(0) #espera indefinidamente para cerrar la ventana hasta que se presione una tecla
cv2.destroyWindow() #cierra la ventana