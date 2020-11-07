import cv2

#Read the Image
# Load an color image in grayscale
img = cv2.imread('C:/Users/Hello/.spyder-py3/snjy.PNG',0)

#Display the image
cv2.imshow('image',img)

#key binding function
k = cv2.waitKey(0)
cv2.destroyAllWindows()