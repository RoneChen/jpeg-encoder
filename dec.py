import cv2 as cv
import numpy as np
from PIL import Image, ImageFile
import io

def load_image(image_path):
    with open(image_path, 'rb') as file:
        jpeg_data = file.read()

    image = Image.open(io.BytesIO(jpeg_data))
    image.show()

if __name__ == '__main__':
    image_path = 'input.jpg'
    load_image(image_path)