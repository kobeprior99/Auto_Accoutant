import os
import sys
import cv2
import pytesseract
import numpy as np
import pandas as pd

def Read_reciept(image_path):
    """
    Reads a receipt image and extracts text from it using Tesseract OCR.
    
    Args:
        image_path (str): The path to the receipt image.
    
    Returns:
        str: The extracted text from the receipt.
    """
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Use Tesseract to extract text from the image
    text = pytesseract.image_to_string(blurred)
    
    return text
