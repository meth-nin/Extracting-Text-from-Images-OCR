import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Methupa-Thyaga\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
from PIL import Image
import cv2
import numpy as np

def basic_tesseract_ocr(image_path):
    
    # Open image
    image = Image.open(image_path)
    
    # Extract text
    text = pytesseract.image_to_string(image)
    
    print("Extracted Text:")
    print("-" * 50)
    print(text)
    
    return text

if __name__ == "__main__":
    image_path = "images\download.jpg"
    text = basic_tesseract_ocr(image_path)