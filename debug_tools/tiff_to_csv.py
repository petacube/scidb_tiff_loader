from PIL import Image
import numpy

im = Image.open("_MG_4674.tiff")
imarray=numpy.array(im)
# the tiff image is 3d (i,j,rgb) but the grey image has the values acorss rah band
imarray_2d=imarray[:,:,0]
print imarray_2d.shape
numpy.savetxt("tiff_output.csv",imarray_2d,delimiter=",",fmt='%-7f',newline="\n")
