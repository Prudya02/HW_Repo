import cv2
import matplotlib.pyplot as plt
import numpy as np
img1 = cv2.imread(r"nogti.jpg",0)

def gauss_noise(image, nu, d):
    result_image = np.random.normal(nu, d, image.shape)
    return result_image
def sub(image1, image2):
   result_image = np.zeros(image1.shape, dtype='u1')
   height, width = image1.shape[:2]
   for i in range(height):
      for j in range(width):
         if (image1[i, j] + image2[i, j]*255 <= 255):
            result_image[i, j] = image1[i, j]+ image2[i, j]*255
         else:  result_image[i, j] = 255
   return result_image
def fure_image(image1):
   return np.fft.fft2(image1)
def high_ideal(image1):
   height, weight = image1.shape[:2]
   H = np.zeros((height, weight), dtype=np.float32)
   D0 = 250
   for i in range(height):
      for j in range(weight):
         D = np.sqrt((i-height/2)**2+(j-weight/2)**2)
         if D <= D0: H[i,j] = 1
         else: H[i,j] = 0
   plt.imshow(H,cmap='gray')
   plt.axis('off')
   #H = 1 - H
   plt.show()
   Gshift = image1*H
   plt.imshow(np.log1p(np.abs(Gshift)), cmap='gray')
   plt.axis('off')
   plt.show()
   G = np.fft.ifftshift(Gshift)
   plt.imshow(np.log1p(np.abs(G)), cmap='gray')
   plt.axis('off')
   plt.show()
   g = np.abs(np.fft.ifft2(G))
   return g
noise_im = np.abs(gauss_noise(img1,0,0.05))
noise_show = np.zeros(noise_im.shape, dtype='u1')
for i in range(noise_show.shape[0]):
   for j in range(noise_show.shape[1]):
      noise_show[i][j] = noise_im[i][j]*255
img_with_noise = sub(img1, noise_im)
cv2.imshow("input", img1)
cv2.imshow("noise", noise_show)
cv2.imshow("noise",img_with_noise)
fur = np.fft.fft2(img_with_noise)
plt.imshow(np.log1p(np.abs(fur)), cmap='gray')
plt.show()
fshift = np.fft.fftshift(fur)
plt.imshow(np.log1p(np.abs(fshift)), cmap='gray')
plt.axis('off')
plt.show()
ideal = high_ideal(fshift)
white = np.ones(ideal.shape[:2])
plt.imshow(ideal,cmap='gray')
plt.show()
cv2.waitKey(0)
