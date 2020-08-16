import cv2
img=cv2.imread('lena.jpg',-1)# change the values to 0,1 and see the difference
print(img)  #now we have just read the image
cv2.imshow('image',img) #to see the image
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('lena_copy.png',img)#to write images to other file
    cv2.destroyAllWindows()
