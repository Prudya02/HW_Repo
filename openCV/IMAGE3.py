import cv2
import numpy as np
img1 = cv2.imread(r"sista.jpg")

def gauss_noise(image, nu, d):
    result_image = np.random.normal(nu, d, image.shape)
    return result_image
def sub(image1, image2):
   result_image = np.zeros(image1.shape, dtype='u1')
   height, width = image1.shape[:2]
   for i in range(height):
      for j in range(width):
         if (image1[i, j][0] + image2[i, j][0]*255 <= 255):
            result_image[i, j][0] = image1[i, j][0] + image2[i, j][0]*255
         else:  result_image[i, j][0] = 255
         if (image1[i, j][1] + image2[i, j][1]*255 <= 255):
            result_image[i, j][1] = image1[i, j][1] + image2[i, j][1]*255
         else:  result_image[i, j][1] = 255
         if (image1[i, j][0] + image2[i, j][0]*255 <= 255):
            result_image[i, j][2] = image1[i, j][2] + image2[i, j][2]*255
         else:  result_image[i, j][2] = 255
   return result_image
def sred_filtre(img):
   height, weight = img.shape[:2]
   result_image = np.zeros(img.shape, dtype='u1')
   for i in range(1,height-1):
      for j in range(1,weight-1):
         result_image[i][j][0] = int(img[i-1][j-1][0]/9)+int(img[i-1][j][0]/9)+int(img[i-1][j+1][0]/9)+int(img[i][j-1][0]/9)+int(img[i][j][0]/9)+int(img[i][j+1][0]/9)+int(img[i+1][j-1][0]/9)+int(img[i+1][j][0]/9)+int(img[i+1][j+1][0]/9)
         result_image[i][j][1] = int(img[i - 1][j - 1][1] / 9) + int(img[i - 1][j][1] / 9) + int(
            img[i - 1][j + 1][1] / 9) + int(img[i][j - 1][1] / 9) + int(img[i][j][1] / 9) + int(
            img[i][j + 1][1] / 9) + int(img[i + 1][j - 1][1] / 9) + int(img[i + 1][j][1] / 9) + int(
            img[i + 1][j + 1][1] / 9)
         result_image[i][j][2] = int(img[i - 1][j - 1][2] / 9) + int(img[i - 1][j][2] / 9) + int(
            img[i - 1][j + 1][2] / 9) + int(img[i][j - 1][2] / 9) + int(img[i][j][2] / 9) + int(
            img[i][j + 1][2] / 9) + int(img[i + 1][j - 1][2] / 9) + int(img[i + 1][j][2] / 9) + int(
            img[i + 1][j + 1][2] / 9)
   return result_image
noise_im = np.abs(gauss_noise(img1,0,0.05))
noise_show = np.zeros(noise_im.shape, dtype='u1')
for i in range(noise_show.shape[0]):
   for j in range(noise_show.shape[1]):
      noise_show[i][j] = noise_im[i][j]*255


def med_filtre(img):
   height, weight = img.shape[:2]
   result_image = np.zeros(img.shape, dtype='u1')
   for i in range(1,height-1):
      for j in range(1,weight-1):
         sort = np.sort([img[i-1][j-1][0], img[i][j-1][0],img[i+1][j-1][0],img[i-1][j][0],img[i][j][0],img[i+1][j][0],img[i-1][j+1][0],img[i][j+1][0],img[i+1][j+1][0]])
         result_image[i][j][0] = sort[4]
         sort = np.sort([img[i-1][j-1][1], img[i][j-1][1],img[i+1][j-1][1],img[i-1][j][1],img[i][j][1],img[i+1][j][1],img[i-1][j+1][1],img[i][j+1][1],img[i+1][j+1][1]])
         result_image[i][j][1] = sort[4]
         sort = np.sort([img[i - 1][j - 1][2], img[i][j - 1][2], img[i + 1][j - 1][2], img[i - 1][j][2], img[i][j][2],
                         img[i + 1][j][2], img[i - 1][j + 1][2], img[i][j + 1][2], img[i + 1][j + 1][2]])
         result_image[i][j][2] = sort[4]
   return result_image

img_with_noise = sub(img1, noise_im)
img_sred_fil = sred_filtre(img_with_noise)
img_med_fil = med_filtre(img_with_noise)
cv2.imshow("input", img1)
cv2.imshow("noise", noise_show)
cv2.imshow("noise_img", img_with_noise)
cv2.imshow("sred_filtre", img_sred_fil)
cv2.imshow("med_filtre",img_med_fil)
cv2.waitKey(0)