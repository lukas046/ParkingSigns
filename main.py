import tensorflow
import os
import imghdr
import cv2
from matplotlib import pyplot as plt
data_dir = 'data'
os.listdir(data_dir)
image_exts = ['jpeg', 'jpg','bmp','png']
image_exts[2]
for image_class in os.listdir(data_dir):
    for image in os.listdir(os.path.join(data_dir,image_class)):
        image_path = os.path.join(data_dir,image_class, image)
        try:
            img = cv2.imread(image_path)
            tip = imghdr.what(image_path)
            if tip not in image_exts:
                print("Image not in ext list")
                os.remove(image_path)
        except Exception as e:
            print("issue")

                    