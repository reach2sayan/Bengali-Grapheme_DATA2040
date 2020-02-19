import numpy as np
from pathlib import Path
import os
import sys
from tqdm import tqdm

datadir_filenames = Path('./images/toy_processed_images/')

for (directory, _ , image_names) in os.walk(datadir_filenames):
        for image_name in tqdm(image_names):
            temp = [int(i) for i in list(image_name) if i.isdigit()]
            image_num = ''.join([str(num) for num in temp])
            image_path = os.path.join(directory, image_name)
            new_name = os.path.join(directory, 'Train_'+image_num+'_f.png')
            os.rename(image_path,new_name)
