import pytesseract
from PIL import Image

# Wczytanie obrazu
image = Image.open(r"C:\Users\las-lab-miesz\Desktop\1.jpeg")

# Wykonanie OCR
recognized_text = pytesseract.image_to_string(image)

# Wyświetlenie rozpoznanego tekstu
#print(recognized_text)