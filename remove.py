import numpy as np
import cv2 # 
from fastapi import APIRouter

def remove_obj_background(img_path, mask_path):
   
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    mask = cv2.imread(mask_path)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB) 

    
    h, w = mask.shape[0], mask.shape[1]
    
    mask_boolean = mask[:,:,0] == 0
    img_with_removed_background = img * np.stack([mask_boolean, mask_boolean, mask_boolean], axis=2)
    
    return img_with_removed_background, mask_boolean