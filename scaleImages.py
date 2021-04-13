from PIL import Image
import os
import PIL
import glob

for i in range(8):
  image = Image.open(f"generated/{i}.png")
  resized_image = image.resize((2000,2000))
  resized_image = resized_image.save(f"generated/{i}.png")