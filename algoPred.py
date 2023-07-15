import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
import cv2 as cv

def resize_image(image_path, output_size, image_name):
    image = Image.open(image_path)
    width, height = image.size
    max_dim = max(width, height)
    scale = output_size / max_dim
    new_width = int(width * scale)
    new_height = int(height * scale)
    resized_image = image.resize((new_width, new_height))
    output_image = Image.new('RGB', (output_size, output_size), 'black')
    x = (output_size - new_width) // 2
    y = (output_size - new_height) // 2


    output_image.paste(resized_image, (x, y))
    output_image.save(image_name)


def jaccard_similarity(image1, image2):
    # Convert images to binary masks
    image1 = np.where(image1 > 0, 1, 0).astype(np.uint8)
    image2 = np.where(image2 > 0, 1, 0).astype(np.uint8)

    # Compute the intersection and union of the masks
    intersection = np.logical_and(image1, image2).sum()
    union = np.logical_or(image1, image2).sum()

    # Calculate the Jaccard Similarity
    jaccard_similarity = intersection / union
    return jaccard_similarity

from skimage.metrics import structural_similarity

def pred_ssim(path, data, start, end):
    u_img = cv.imread(path)
    u_img = cv.cvtColor(u_img, cv.COLOR_BGR2GRAY)
    u_img = cv.Canny(200,350)

    ssimarr = []
    for i in range(start,end):
        ximg = cv.imread(data['path'][i])
        ximg = cv.cvtColor(ximg, cv.COLOR_BGR2GRAY)
        (score, diff) = structural_similarity(u_img, ximg, full=True)
        ssimarr.append([score,data['path'][i]])
        return ssimarr
    
def pred_jaccard(path, data, start, end):
    resize_image(path, 256, path)
    image = cv.imread(path)
    ui_edge = image
    ui_edge= cv.cvtColor(ui_edge, cv.COLOR_BGR2GRAY)
    ui_edge = cv.convertScaleAbs(ui_edge, alpha=1.5, beta=10)
    jaccardArr = []
# before_gray = cv2.cvtColor(u_img, cv2.COLOR_BGR2GRAY)
    for i in range(start,end):
        ximg = cv.imread(data['path'][i])
        ximg = cv.cvtColor(ximg, cv.COLOR_BGR2GRAY)
        score = jaccard_similarity(ui_edge, ximg)
        jaccardArr.append([score,data['path'][i]])