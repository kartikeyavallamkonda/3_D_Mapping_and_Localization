import cv2
import numpy as np
import matplotlib.pyplot as plt


#Reading images
img_left = cv2.imread('tsukuba_l.png',0)
img_right = cv2.imread('tsukuba_r.png',0)

#Converting into float
img_left = np.double(img_left)
img_right = np.double(img_right)

#Counting the number of rows and number of elements in each row
count_row,count_ele = img_left.shape
search = 30
img_dispmap = np.zeros((count_row,count_ele),dtype=float)
img_dispmap = np.double(img_dispmap)

#Making a window
n=5
n1=np.floor(n/2)
n1=int(n1)

#Loop to take min
fin_l = []
for row in range(n1,count_row-n1):
    for ele_l in range(n1,count_ele-n1):
        lst = []
        lst.clear()
        c_r=(img_right[row-n1:row+n1+1,ele_l-n1:ele_l+n1+1])
        for ele_r in range(ele_l,min(ele_l+(search),count_ele-n1)):
            c_l=(img_left[row-n1:row+n1+1,ele_r-n1:ele_r+n1+1])
            lst.append(np.sum(np.abs(np.subtract(c_r,c_l))))
        i=lst.index(min(lst))+1
        fin_l.append(i)
img_dispmap = np.array(fin_l).reshape(284,380)
print(img_dispmap)
plt.imshow(img_dispmap,cmap="gray")
plt.show()