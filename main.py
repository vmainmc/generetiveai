import cv2 # OpenCV
import numpy as np
import matplotlib.pyplot as plt
import addobj
import remove
import backmaker



backmaker.makebackground()

# Original image, which is the background 
background = cv2.imread('/home/malik/Desktop/task/resim.jpg')
background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)

    # Image of the object
img = cv2.imread('/home/malik/Desktop/task/perfume-20061.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

mask = np.zeros(img.shape[:2], dtype=np.uint8)
beyaz_pikseller = (img[:, :, 0] == 255) & (img[:, :, 1] == 255) & (img[:, :, 2] == 255)
mask[beyaz_pikseller] = 255

# Maskeyi PNG olarak kaydet
cv2.imwrite("maske.png", mask)

mask = cv2.imread('/home/malik/Desktop/task/maske.png')
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)

img = cv2.resize(img, (400, 400))
mask=cv2.resize(mask,(400,400))

print("Background shape:", background.shape)
print("Image shape:", img.shape)
print("Mask shape:", img.shape)


img_with_removed_background, mask_boolean = remove.remove_obj_background('/home/malik/Desktop/task/perfume-20061.png', '/home/malik/Desktop/task/maske.png')
    


composition_1 = addobj.add_obj(background, img, mask, 512, 512)
composition_1= cv2.cvtColor(composition_1, cv2.COLOR_BGR2RGB)
cv2.imwrite("output-generated-parfume.jpg", composition_1)
# plt.figure(figsize=(15,15))
# plt.imshow(composition_1)
# plt.show()
image_path = "/home/malik/Desktop/task/output-generated-parfume.jpg"
image = cv2.imread(image_path)

cv2.imshow("Görüntü", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


