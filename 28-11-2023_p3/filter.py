import sys
from PIL import Image, ImageFilter

# Ensure correct usage
filename  = "bridge.png"
if len(sys.argv) == 2:
    filename = sys.argv[2]
# Open image
image = Image.open(filename).convert("RGB")

# Filter image according to edge detection kernel
kernel_aresta_laplaciana=[-1, -1, -1, -1, 8, -1, -1, -1, -1]
kernel_borda_sobel_h=[-1,0,1,-2,0,2,-1,0,1]
kernel_borda_sobel_v=[-1,-2,1,0,0,0,1,2,1]
kernel_desfoque=[1/9,1/9,1/9,1/9,1/9,1/9,1/9,1/9,1/9]
kernel_gaussiano=[1,2,1,2,4,2,1,2,1]
filtered = image.filter(
    ImageFilter.Kernel(size=(3, 3), kernel=kernel_borda_sobel_v, scale=1)
)

# Show resulting image
filtered.show()

# More operations at
# https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html
# https://docs.opencv.org/3.4/d9/d61/tutorial_py_morphological_ops.html
