import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file')
parser.add_argument('--output', help='output file')
args = parser.parse_args()
print(args.input)
print(args.output)

import numpy as np
import nibabel
from skimage import morphology 

nib_img = nibabel.load(args.input)
img = nib_img.get_data()
img.shape, img.dtype

binary_img = img > 250
closed_img = morphology.binary_closing(binary_img,selem=morphology.ball(radius=2))

out_img = nibabel.Nifti1Image(closed_img.astype(np.uint8), nib_img.affine)
out_img.to_filename(args.output)
