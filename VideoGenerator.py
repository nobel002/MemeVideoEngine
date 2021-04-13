import cv2, os, glob
import numpy as np
from PIL import Image
import PIL

FRAMESIZE = (2000, 2000)
FILENAME = "test001"
def scaleAllImgs():
  for imageObj in glob.glob('generated/*.png'):
    image = Image.open(imageObj)
    resized_image = image.resize(FRAMESIZE)
    resized_image = resized_image.save(imageObj)

out = cv2.VideoWriter(f'generated/{FILENAME}.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.2, FRAMESIZE)

for filename in glob.glob('generated/*.png'):
    img = cv2.imread(filename)
    out.write(img)


scaleAllImgs()
out.release()
#os.system("ffmpeg -i generated/{FILENAME}.avi generated/{FILENAME}.mp4")