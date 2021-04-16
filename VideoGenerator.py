import cv2, os, glob
import numpy as np
from PIL import Image
import PIL

frameSize = (2000, 2000)
FILENAME = "test003"
PATH = "generated/images/*.png"

def scaleImages():
  frameSize = (2000, 2000)
  imagePaths = glob.glob(PATH)

  for image in imagePaths:
    imgObj = Image.open(image)
    width, height = imgObj.size
    if width >= frameSize[0]:
      frameSize = (width, frameSize[1])
    if height >= frameSize[1]:
      frameSize = (frameSize[0], height)

  for image in imagePaths:
    imgObj = Image.open(image)
    resized = imgObj.resize(frameSize)
    resized.save(image)

out = cv2.VideoWriter(f'generated/videos/{FILENAME}.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.2, frameSize)

for filename in glob.glob(PATH):
    img = cv2.imread(filename)
    out.write(img)

scaleImages()
out.release()

print("Finalizing")
#os.system("ffmpeg -i generated/{FILENAME}.avi generated/{FILENAME}.mp4")