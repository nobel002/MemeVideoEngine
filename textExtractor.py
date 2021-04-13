import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = 'tesseract\\tesseract.exe'

img = cv2.imread("generated\\images\\Brutal.png")

text = pytesseract.image_to_string(image= img)

print(text)