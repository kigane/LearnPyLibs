import cv2 as cv
import matplotlib.pyplot as plt
import os
# os.chdir('..')

i = cv.imread('assets/Gon.jpg')
o = cv.applyColorMap(i, cv.COLORMAP_TURBO)
cv.imshow("Turbo",o)
cv.waitKey(0)
