from glob import glob
import os
import re
import rasterio as rio
import numpy as np

class Preprocessing():

    def __init__(self):
        pass

    def _get_products(self, products_path):
        products = glob(products_path + "\\*\\")
        print(products)
        return products

    def _get_bands(self, products):
        regex = re.compile(r'.*B[0-9]{2,3}_10m.jp')
        images_path = []
        for product in products:
            files = []
            for root, directories, filenames in os.walk(product):
                for filename in filenames:
                    files.append(os.path.join(root, filename))
                    # print("files", os.path.join(root,filename))

            selected_files = list(filter(regex.search, files))
            images_path.append((product, selected_files))

        return images_path

    def _images_to_nparrays(self, images_path):
        image_arrays = []
        for product, images in images_path:
            np_images = np.zeros((10980,10980,4))
            for i, image in enumerate(images):
                np_images[..., i] = rio.open(image).read()
            image_arrays.append((product, np_images))
        return image_arrays

    def get_3D_array(self, image_array):
        pass


# Testing
#print(os.getcwd()+"\products")
prod_path = os.getcwd()+"\products"
pp = Preprocessing()
products = pp._get_products(prod_path)
print(pp._get_bands(products))
bands = pp._get_bands(products)
b2 = rio.open(r"C:\Users\torresjj\PycharmProjects\LandClassificationProject\products\S2A_MSIL2A_20190622T171901_N0212_R012_T13QGD_20190622T225605.SAFE\GRANULE\L2A_T13QGD_A020887_20190622T173800\IMG_DATA\R10m\T13QGD_20190622T171901_TCI_10m.jp2")
print(type(b2))

array = b2.read()
print(type(array))
print(array.shape)
print(b2.width)
print(b2.height)
print(pp._images_to_nparrays(bands)[0][1].shape)
# print(glob(prod_path + "/*/"))
# print(glob(prod_path))
# files = []
# for root, directories, filenames in os.walk(prod_path):
#     for filename in filenames:
#         files.append(os.path.join(root,filename))
#         #print("files", os.path.join(root,filename))
#
# print(files)
#
# regex = re.compile(r'.*B[0-9]{2,3}_10m.jp')
#
# selected_files = list(filter(regex.search, files))
# print(selected_files)
# .*\\\\IMG_DATA\\\\