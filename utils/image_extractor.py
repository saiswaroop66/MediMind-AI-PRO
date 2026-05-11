import pytesseract
from PIL import Image

# Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_file):

    # Open image
    image = Image.open(image_file)

    # Extract text using OCR
    extracted_text = pytesseract.image_to_string(image)

    return extracted_text
