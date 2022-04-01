import pytesseract
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/\/tesseract.exe'

img = Image.open('./images/phone-number.jpg')

text = pytesseract.image_to_string(img)
phone_number = re.sub('[!^a-zA-Z]', '', text)
print(phone_number)