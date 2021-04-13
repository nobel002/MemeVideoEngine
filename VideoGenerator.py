import cv2
import numpy as np
import glob

from PIL import Image
import os
import PIL

FRAMESIZE = (2000, 2000)

def scaleAllImgs():
  for imageObj in glob.glob('generated/*.png'):
    image = Image.open(imageObj)
    resized_image = image.resize(FRAMESIZE)
    resized_image = resized_image.save(imageObj)

out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, FRAMESIZE)

for filename in glob.glob('generated/*.png'):
    img = cv2.imread(filename)
    out.write(img)


scaleAllImgs()
out.release()