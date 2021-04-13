import cv2, os, glob
import numpy as np
from PIL import Image
import PIL

FRAMESIZE = (2000, 2000)
FILENAME = "test001"
PATH = "generated/image/*.png"
def scaleAllImgs():
  for imageObj in glob.glob(PATH):
    image = Image.open(imageObj)
    width, height = image.size
    if width >= FRAMESIZE[0]:
      FRAMESIZE = (width, FRAMESIZE[1])
    if height >= FRAMESIZE[1]:
      FRAMESIZE = (FRAMESIZE[0], height)

  for imageObj in glob.glob(PATH):
    resized_image = image.resize(FRAMESIZE)
    resized_image = resized_image.save(imageObj)

out = cv2.VideoWriter(f'generated/videos/{FILENAME}.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.2, FRAMESIZE)

for filename in glob.glob(PATH):
    img = cv2.imread(filename)
    out.write(img)


scaleAllImgs()
out.release()
#os.system("ffmpeg -i generated/{FILENAME}.avi generated/{FILENAME}.mp4")