import sys
sys.path.append('/usr/local/lib/python2.7/site-packages') 

import math

import cv2
import numpy as np


img = cv2.imread('figure514.tif', 0)
image = img
cv2.imshow("input", image)
width, height = img.shape


# adaptive median filter

for x in range(1,width-1):
    for y in range(1,height-1):

        # 3x3
        neighbor = [img[x-1,y-1], img[x,y-1], img[x+1,y-1],
                    img[x-1,y], img[x,y], img[x+1,y],
                    img[x-1,y+1], img[x,y+1], img[x+1,y+1]]
        median = np.median(neighbor)
        max_nei = max(neighbor)
        min_nei = min(neighbor)

        if( ( (img[x,y] < max_nei) and (img[x,y] > min_nei)) and (2<x and x<width-2 and 2<y and y<height-2 )):

            # 5x5
            neighbor = [img[x-2,y-2], img[x-1,y-2], img[x,y-2], img[x+1,y-2], img[x+2,y-2],
                        img[x-2,y-1], img[x-1,y-1], img[x,y-1], img[x+1,y-1], img[x+2,y-1],
                        img[x-2,y], img[x-1,y], img[x,y], img[x+1,y], img[x+2,y],
                        img[x-2,y+1], img[x-1,y+1], img[x,y+1], img[x+1,y+1], img[x+2,y+1],
                        img[x-2,y+2], img[x-1,y+2], img[x,y+2], img[x+1,y+2], img[x+2,y+2]]
            median = np.median(neighbor)
            max_nei = max(neighbor)
            min_nei = min(neighbor)

            if( ( (img[x,y] < max_nei) and (img[x,y] > min_nei)) and (3<x and x<width-3 and 3<y and y<height-3 )):
            
                # 7x7
                neighbor = [img[x-3,y-3], img[x-2,y-3], img[x-1,y-3], img[x,y-3], img[x+1,y-3], img[x+2,y-3], img[x+3,y-3],
                            img[x-3,y-2], img[x-2,y-2], img[x-1,y-2], img[x,y-2], img[x+1,y-2], img[x+2,y-2], img[x+3,y-2],
                            img[x-3,y-1], img[x-2,y-1], img[x-1,y-1], img[x,y-1], img[x+1,y-1], img[x+2,y-1], img[x+3,y-1],
                            img[x-3,y], img[x-2,y], img[x-1,y], img[x,y], img[x+1,y], img[x+2,y], img[x+3,y],
                            img[x-3,y+1], img[x-2,y+1], img[x-1,y+1], img[x,y+1], img[x+1,y+1], img[x+2,y+1], img[x+3,y+1],
                            img[x-3,y+2], img[x-2,y+2], img[x-1,y+2], img[x,y+2], img[x+1,y+2], img[x+2,y+2], img[x+3,y+2],
                            img[x-3,y+3], img[x-2,y+3], img[x-1,y+3], img[x,y+3], img[x+1,y+3], img[x+2,y+3], img[x+3,y+3]]
                median = np.median(neighbor)
            else:
                img[x,y] = int(median)

        else:
            img[x,y] = int(median)



cv2.imshow("output", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
