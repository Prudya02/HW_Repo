from skimage.io import imread, imsave, imshow
import random
from matplotlib import pyplot as plt
import cv2
from PIL import Image
img = imread('img3.png')
img1 = imread('img3.png')
fig = plt.figure
frames =[]

def random_img(img, k):
    n, m = img.shape[:2]
    print(n)
    print(m)
    for i in range(n):
        for j in range(m):
            img[i][j][0] = img[i][j][0] + random.uniform(-k, k)
            img[i][j][1] = img[i][j][1] + random.uniform(-k, k)
            img[i][j][2] = img[i][j][2] + random.uniform(-k, k)
    return img

for i in range(100):
    img = random_img(img, i)
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    frame_pil = Image.fromarray(frame)
    frames.append(frame_pil)
    img = img1.copy()
    print(i, "%")
frames[0].save(
    'random2.gif',
    save_all=True,
    append_images=frames[1:],  # Срез который игнорирует первый кадр.
    optimize=True,
    duration=130,
    loop=0
)
imshow(img)
plt.show()

