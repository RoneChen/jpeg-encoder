import argparse
import itertools
import math

from skimage.metrics import structural_similarity as compute_ssim
import numpy as np
import cv2 as cv



img = cv.imread('input.jpg', cv.IMREAD_COLOR)
img = np.float32(img)

img_ycc = cv.cvtColor(img, code=cv.COLOR_BGR2YCrCb)

# get the Y component of the image (luminance)
img_y = img_ycc[:, :, 0]
cv.imwrite('block.jpg', img_y)

img_y_blocks = [img_y[j:j + 8, i:i + 8] for (j, i) in itertools.product(range(0, img_y.shape[0], 8), range(0, img_y.shape[1], 8))]

index = 0
for block in img_y_blocks:
    filename = f'block{index}.jpg'
    cv.imwrite(f'blocks/{filename}.jpg', block)
    index += 1
