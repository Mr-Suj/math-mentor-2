from paddleocr import PaddleOCR
import numpy as np
import cv2
from PIL import Image

# Initialize once
ocr_model = PaddleOCR(use_angle_cls=True, lang="en")

def extract_text_from_image(image_file):
    """
    Extract text from image using PaddleOCR
    """

    # Convert uploaded file to numpy image
    if isinstance(image_file, str):
        image = cv2.imread(image_file)
    else:
        image = Image.open(image_file)
        image = np.array(image)

    # Ensure image has 3 channels
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    result = ocr_model.ocr(image)
    # extracted_text = []
    # for line in result:
    #     for word in line:
    #         extracted_text.append(word[1][0])
    # return " ".join(extracted_text)
    text = " ".join([line[1][0] for line in result[0]])

    return text



    