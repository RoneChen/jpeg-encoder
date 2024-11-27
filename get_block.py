import argparse
import itertools
import math

from skimage.metrics import structural_similarity as compute_ssim
import numpy as np
import cv2 as cv



img = cv.imread('input.jpg', cv.IMREAD_COLOR)
img = np.float32(img)


def block_seperation(img, block_size=8):
    img_ycc = cv.cvtColor(img, code=cv.COLOR_BGR2YCrCb)

    # get the Y component of the image (luminance)
    img_y = img_ycc[:, :, 0]

    # Split the image into blocks of the specified size
    img_y_blocks = [
        [img_y[j:j + block_size, i:i + block_size] for i in range(0, img_y.shape[1], block_size)]
        for j in range(0, img_y.shape[0], block_size)
    ]

    # Save each block as a separate image file
    for row_idx, row in enumerate(img_y_blocks):
        for col_idx, block in enumerate(row):
            # Construct the filename using row and column indices
            filename = f"blocks/row_{row_idx}_col_{col_idx}.jpg"
            # Save the block
            cv.imwrite(filename, block)

    return img_y_blocks

def intra_block_prediction(img_blocks):
    pred_blocks = img_blocks[1:, 1:]
    for row_idx, block in enumerate(pred_blocks):
        