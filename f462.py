import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import math

import cv2
import numpy as np



img = cv2.imread('figure462.tif', 0)
image = img
width, height = img.shape
img = np.float32(img)

for x in range(width):
    for y in range(height):
        img[x,y] += 1.0

img_log = np.log(img)

dft = cv2.dft(img_log, flags = cv2.DFT_COMPLEX_OUTPUT | cv2.DFT_SCALE)
dft_real = cv2.split(dft)[0]
dft_img = cv2.split(dft)[1]

rH = 2.0
rL = 0.25
c = 1.0
D0 = 80.0
H = img

for x in range(width):
    for y in range(height):
        u = x-width/2
        v = y-height/2
        H[x,y] = (rH - rL)*(1 - np.exp( (-c)*( ( u**2 + v**2 ) / (D0*D0)) ) ) + rL

dft_real = cv2.multiply(H, dft_real)
dft_img = cv2.multiply(H, dft_img)
dft_real_img = cv2.merge(dft_real, dft_img)

idft = cv2.dft(dft, flags = cv2.DFT_REAL_OUTPUT | cv2.DFT_INVERSE)

result = np.exp(idft) - 1

result_uint = np.uint8(result)

cv2.imshow("input", image)
cv2.imshow("pp", result_uint)


cv2.waitKey(0)
cv2.destroyAllWindows()
