import cv2
import numpy as np
img1 = cv2.imread(r"pc.jpg") # чтение изображения. Изображение предоставляется в виде массива кортежей по 3 элемента.
#каждый кортеж отвечает за пиксель. Его элементы - 3 цвета RGB от 0 до 255. Если это белый пиксель, то будет ячейка вида [255,255,255]
print(img1) #проверка изображения, которое я считал.
def rotate(image, direction, angle): #Функция поворота. Аргументы: изображение, направление по,против часовой (0/1), угол поворота.
   if direction == 1: #случай поворота по и против отличаются только отниманием 360-angle (повернуть на 2 по часовой = на 358 против часовой.
      rotate_mat = np.array(
         [[np.cos(angle * np.pi / 180), np.sin(angle * np.pi / 180)], [-np.sin(angle * np.pi / 180), np.cos(angle * np.pi / 180)]])
      print(rotate_mat)#матрицы поворота (cosa, sina, -sina, cosa)
   if direction == 0:
      rotate_mat = np.array(
         [[np.cos((360-angle) * np.pi / 180), np.sin((360-angle) * np.pi / 180)], [-np.sin((360-angle) * np.pi / 180), np.cos((360-angle) * np.pi / 180)]])
      print(rotate_mat)
   height, width = image.shape[:2] #длина и ширина картинки в пикселях
   result_image = np.zeros(image.shape, dtype='u1') #инициализировали пустую картинку с такими же размерами, заполнив 0
   p_point_x, p_point_y = 0, height #ВАРИАНТ 1. Левый нижний угол. Выбор точки поворота. Можно занести в аргументы функции при желании
   for i in range(height):
      for j in range(width):
         xy_mat = np.array([[j-p_point_x],[i-p_point_y]]) #это одна точка с 2 координатами относительно точки поворота
         r_mat = np.dot(rotate_mat,xy_mat) #np.dot - матричное умножение. Тут просто умножаем матрицу поворота на нашу точку, чтобы получить новые координаты
         #мы получиди новые координаты исходной точки, но они хранятся в виде относительно точки поворота.
         new_x = p_point_x + int(r_mat[0])  # Добавим координаты точки пов. для получения норм.координат
         new_y = p_point_y + int(r_mat[1])  # Добавим координаты точки пов. для получения норм.координат
         if (0<=new_x<width-1) and (0<new_y<height-1): #запоминаем точку только в том случае, если она не вылезает за пределы изображения.
            result_image[new_y,new_x] = image[i,j]
   return result_image


def sub(image1, image2):
   result_image = np.zeros(image1.shape, dtype='u1')
   height, width = image1.shape[:2]
   for i in range(height):
      for j in range(width):
         result_image[i, j] = np.abs(image1[i, j] - image2[i, j])
   return result_image
result1 = rotate(img1, 1, 53)
result2 = rotate(result1, 0, 53)
cv2.imshow("earth", img1)
cv2.imshow("results1", result1)
cv2.imshow("result2", result2)
image_sub = sub(img1, result2)
image_sub2 = sub(img1, image_sub)
cv2.imshow("result3",image_sub)
cv2.imshow("result4",image_sub2)
cv2.waitKey(0)
