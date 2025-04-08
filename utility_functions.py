import os
from glob import glob
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt


def load_directory_images(path):
    '''
    Loads a directory's worth of image into convenient storage units.
    Requires astropy.io.fits.
    Note: All Images in directory must be of same shape.

    Parameters
    ----------
    path: str
        path to the directory you wish to load, as a string.
    Returns
    ----------
    image_stack: array_like
        A stack of all images contained in the directory.
        Array of shape (N,X,Y) where N is the number of images,
        and X,Y are the dimensions of each image.
    image_dict: dict
        A dictionary containing headers for each image, the keys
        are the same as the indices of the corresponding
        image in the image_stack
    '''
    if not isinstance(path, str):
        raise AssertionError('Path must be a string')
    if os.path.isdir(path) is False:
        raise OSError('Path does not point to a valid location.')

    files_in_dir = glob(path + '*')
    image_stack = []
    header_stack = {}
    for i,f in enumerate(files_in_dir):
        with fits.open(f) as HDU:
            image_stack.append(HDU[0].data)
            header_stack[i] = HDU[0].header
        image_stack_result = np.array(image_stack)
    return image_stack_result, header_stack
        
def median_image(image_stack):
    '''
    Taking a stack of image and returns the median image.
    Parameters
    ----------
    image_stack: array_like
        stack of images,first dimension being image index.
    Returns
    -------
    median_image: array_like
        single image of the median of the input images
    '''
    median_image = np.median(image_stack,axis=0)
    return median_image
    
    
    
def main(image_dir,cleaning_keyword,alignment_keyword,coadd_keyword):
    image_stack, header_stack = load_directory_images(image_dir)
    cleaned_images = clean_images(image_stack,cleaning_keyword)
    aligned_images = align_images(cleaned_images,alignment_keyword)
    coadded_images = coadd_images(aligned_images,coadd_keyword)
    return coadded_images
    
    
if __name__ == '__main__':
    main(image_dir, cleaning_keyword, alignment_keyword, codded_keyword)
    
    
def my_sin(x,units='radian'):
    if units=='radian':
        return np.sin(x)
    elif units =='deg':
        new_x = x * np.pi / 180.0
        return np.sin(new_x)
        
        
def func_args(x,y,z,a=1,b=25,c=None,d=False):
    if d:
        return x+y+z
    elif c is not None:
        print('wow!')
    else:
        return x+b
        
        
def mysum(a,b,*args):
    running_sum = a+b
    for i in args:
        running_sum+=i
    return running_sum
    
def pretty_print(string,**kwargs):
    print(string)
    if 'sep' in kwargs.keys():
        print(kwargs['sep'])