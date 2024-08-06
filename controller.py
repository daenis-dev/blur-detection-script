import pickle
from scipy.ndimage import variance
from skimage import io
from skimage.color import rgb2gray
from skimage.filters import laplace as llc
from skimage.transform import resize
import numpy as np
from imutils import paths
import shutil
import os

with open('blur-detection-model.pkl', 'rb') as f:
    clf2 = pickle.load(f)
    
def get_image_paths_within(directory_path):
    return list(paths.list_images(directory_path))

def get_laplace_for(image_path):
    img = io.imread(image_path)
    img = resize(img, (400, 600))
    img = rgb2gray(img)
    return llc(img, ksize=3)

def get_variance_of_laplace(laplace):
    return variance(laplace)

def get_maximum_laplace(laplace):
    return np.amax(laplace)

def image_is_blurry(image_path):
    edge_laplace = get_laplace_for(image_path)
    value = clf2.predict([[get_variance_of_laplace(edge_laplace), get_maximum_laplace(edge_laplace)]])
    return value[0] == 0.0

input_directory_path = os.path.dirname(os.path.abspath(__file__)) + '\\datasets\\test'

image_paths = list(paths.list_images(input_directory_path))
for image_path in image_paths:
    print('Image name: ', image_path)
    if image_is_blurry(image_path):
        print('Blurry')
        shutil.move(image_path, image_path.replace('test', 'test/blurry'))
    else:
        print('Not Blurry')

