import cv2
import pytesseract
import numpy as np


def Read_reciept(image_path):
    """
    Reads a receipt image and extracts text from it using Tesseract OCR.
    
    Args:
        image_path (str): The path to the receipt image.
    
    Returns:
        str: The extracted text from the receipt.
    """
    try:
        # Load the image
        image = cv2.imread(image_path)
        #Preporcessing the image
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #apply thresholding
        gray = cv2.adaptiveThreshold(gray,225, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)
        # Display the processed image (optional)
        cv2.imshow("Processed Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 

        # Use Tesseract to extract text from the image
        text = pytesseract.image_to_string(gray, lang = 'eng')
        
        return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
print(Read_reciept("1000-receipt.jpg"))