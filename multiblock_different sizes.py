#import cv2
import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt
#Read the left and right images
#file path in the cv2.imread() function
left=cv2.imread('tsukuba_l.png',0)
right=cv2.imread('tsukuba_r.png',0)
n=61
n1=np.floor(n/2)
n1=int(n1)
n2=11
left=np.double(left)
#print(left)
right=np.double(right)
#print(right)
wid=left.shape[1]
hgt=left.shape[0]
#print(wid)
#print(hgt)
ser=20
i=n1
j=n1
sub=[0]
sub1=[0]
sub2=[0]
out=[0]
out.clear()
#Vertical pixel groups:
print('startofloop')
for i in range(n1,hgt-n1):
    #print(i)
    for j in range(n1,wid-n1):
        sub.clear()
        sub1.clear()
        sub2.clear()
        cv=right[i-n1:i+n1+1,j:j+1]
        ch=right[i:i+1,j-n1:j+n1+1]
        cb=right[i-n2:i+n2+1,j-n2:j+n2+1]
        for j1 in range(j,min(j+ser,wid-n1)):
            cv1=left[i-n1:i+n1+1,j1:j1+1]
            sub.append(np.sum(np.abs(np.subtract(cv,cv1))))
        #print(sub)
        for j1 in range(j,min(j+ser,wid-n1)):
            ch1=left[i:i+1,j1-n1:j1+n1+1]
            sub1.append(np.sum(np.abs(np.subtract(ch,ch1))))
        for j1 in range(j,min(j+ser,wid-n1)):
            cb1=left[i-n2:i+n2+1,j1-n2:j1+n2+1]
            sub2.append(np.sum(np.abs(np.subtract(cb,cb1))))
        #print(sub1)
        fin=np.add(sub,sub1)
        final=np.add(fin,sub2)
        #print(final)
        i1=np.argmin(final)+1
        #print(min(final))
        #print(i1)
        out.append(i1)
pixeldata=np.array(out).reshape(288-2*n1,384-2*n1)
#np.set_printoptions(threshold=sys.maxsize)
#print(pixeldata)
plt.imshow(pixeldata,cmap="gray")
plt.show()
