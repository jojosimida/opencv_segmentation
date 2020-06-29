from PIL import Image
import os
from os import listdir
from os.path import isfile, join
import json
import cv2

d = '/home/ubuntu/storage/dataset/'
dirs = [join(d, f, 'images') for f in listdir(d)]
print(dirs)

for dir in dirs:
    try: 
        image_folder = [f for f in listdir(dir) if not isfile(join(dir, f))]
    except: 
        continue
    
    new_dir = '/'.join(dir.split('/')[:-1])


    for f in image_folder:
        try:
            os.makedirs(join(new_dir, 'convert_image', f))
        except:
            continue
        for image in listdir(join(dir, f)):
            i = cv2.imread(join(dir, f, image))
            image = image.split('.')[0]+'.jpg'
            cv2.imwrite(join(new_dir, 'convert_image', f, image), i)

        print('Done', f)

    print('Done', dir)







