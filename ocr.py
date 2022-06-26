import cv2
import pytesseract
import numpy as np
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

image_file = "C:/Users/Mukhammad/Desktop/projects/car-predict/tex_data_front.jpg"
img = cv2.imread(image_file)

custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)
text = text.replace("  ","")
text_lower = text.lower()
cars_names = ["LACETTI"]
if "MATIZ" in text:
    print("topildi")
else:
    print("topilmadi")