import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input file')
parser.add_argument('--output', help='output file')
parser.add_argument('--threshold', type=int, help='cutoff threshold in Hounsfield Units', default=250)
parser.add_argument('--closing-radius', type=int, help='closing radius', default=2)
args = parser.parse_args()
# print(args.input)
# print(args.output)
# print(args.threshold)
# print(args.closing_radius)

import numpy as np
import nibabel
from skimage import morphology 

nib_img = nibabel.load(args.input)
img = nib_img.get_data()
img.shape, img.dtype

binary_img = img > args.threshold 
closed_img = morphology.binary_closing(binary_img,selem=morphology.ball(radius=args.closing_radius))

out_img = nibabel.Nifti1Image(closed_img.astype(np.uint8), nib_img.affine)
out_img.to_filename(args.output)
