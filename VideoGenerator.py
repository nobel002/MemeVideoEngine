import cv2, os, glob
import numpy as np
from PIL import Image
import PIL

frameSize = (2000, 2000)
FILENAME = "test004"
PATH = "generated/images/*.png"


#no dynamic scaling for this version
def scaleImages():
  frameSize = (2000, 2000)
  imagePaths = glob.glob(PATH)

  for image in imagePaths:
    imgObj = Image.open(image)
    resized = imgObj.resize(frameSize)
    resized.save(image)


print("Started execution...")
print("Scaling images")
scaleImages()


out = cv2.VideoWriter(f'generated/videos/{FILENAME}.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.2, frameSize)

print("Stiching images together...")
for filename in glob.glob(PATH):
    img = cv2.imread(filename)
    out.write(img)

print("Finalizing")
out.release()


#os.system("ffmpeg -i generated/{FILENAME}.avi generated/{FILENAME}.mp4")