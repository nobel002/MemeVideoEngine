#                                  █████                         █████      ███                                       █████            █████            
#                                 ░░███                         ░░███      ░░░                                       ░░███            ░░███             
# ████████    ██████   ██████   ███████   █████      ██████      ░███████  ████   ███████    █████ ████ ████████   ███████   ██████   ███████    ██████ 
#░░███░░███  ███░░███ ███░░███ ███░░███  ███░░      ░░░░░███     ░███░░███░░███  ███░░███   ░░███ ░███ ░░███░░███ ███░░███  ░░░░░███ ░░░███░    ███░░███
# ░███ ░███ ░███████ ░███████ ░███ ░███ ░░█████      ███████     ░███ ░███ ░███ ░███ ░███    ░███ ░███  ░███ ░███░███ ░███   ███████   ░███    ░███████ 
# ░███ ░███ ░███░░░  ░███░░░  ░███ ░███  ░░░░███    ███░░███     ░███ ░███ ░███ ░███ ░███    ░███ ░███  ░███ ░███░███ ░███  ███░░███   ░███ ███░███░░░  
# ████ █████░░██████ ░░██████ ░░████████ ██████    ░░████████    ████████  █████░░███████    ░░████████ ░███████ ░░████████░░████████  ░░█████ ░░██████ 
#░░░░ ░░░░░  ░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░░░      ░░░░░░░░    ░░░░░░░░  ░░░░░  ░░░░░███     ░░░░░░░░  ░███░░░   ░░░░░░░░  ░░░░░░░░    ░░░░░   ░░░░░░  
#                                                                                ███ ░███               ░███                                            
#                                                                               ░░██████                █████                                           
#                                                                                ░░░░░░                ░░░░░                                            

import cv2, glob
import pytesseract


pytesseract.pytesseract.tesseract_cmd = 'tesseract\\tesseract.exe'

text = ''

for image in glob.glob("generated\\images\\*.png"): 
  img = cv2.imread(image)
  text += str(pytesseract.image_to_string(image=img))
  text += """\n---------------------------------------------------\n"""
  
with open("generated/Scripts/script.txt", "w+") as file:
  file.write(text)

with open("generates/Scripts/script.txt", "rw") as file:
  lines = file.readlines()
  for line in lines:
    #remove lines with a "" charactetr in them. and minimise the txt file
    #Maby even make your own format, get some basic shit together.