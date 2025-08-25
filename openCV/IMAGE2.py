import cv2
import numpy as np
img1 = cv2.imread(r"sista.jpg")
#img1 = cv2.threshold(img1, 100, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("input", img1)
def sobel(image):
    result_image = np.zeros(image.shape, dtype='u1')
    result_imagex = np.zeros(image.shape, dtype='u1')
    result_imagey = np.zeros(image.shape, dtype='u1')
    height, weight = image.shape[:2]
    for i in range(1, height-1):
        for j in range(1, weight-1):
            Gx = (image[i+1][j-1]+2*image[i+1][j]+image[i+1][j+1])-(image[i-1][j-1]+2*image[i-1][j]+image[i-1][j+1])
            Gy = (image[i-1][j+1]+2*image[i][j+1]+image[i+1][j+1])-(image[i-1][j-1]+2*image[i][j-1]+image[i+1][j-1])
            Gx2 = [Gx[0]**2, Gx[1]**2, Gx[2]**2]
            Gy2 = [Gy[0] ** 2, Gy[1] ** 2, Gy[2] ** 2]
            result_imagex[i, j] = Gx2
            result_imagey[i, j] = Gy2
            G = [Gx2[0]+Gy2[0], Gx2[1]+Gy2[1], Gx2[2]+Gy2[2]]
            G = np.sqrt(G)
            result_image[i, j] = G
    return result_imagex, result_imagey, result_image
imgx, imgy, img_filtred = sobel(img1)
cv2.imshow("filtred", img_filtred)
cv2.imshow("x_sobel", imgx)
cv2.imshow("y_sobel", imgy)
image2 = img1+img_filtred
image2 = np.minimum(image2, 255)
cv2.imshow("sub", image2)
cv2.waitKey(0)