
import cv2

# read image
imgA = cv2.imread('p1.jpg', cv2.IMREAD_UNCHANGED)
imgB = cv2.imread('p2.jpg', cv2.IMREAD_UNCHANGED)

# height, width
heightA = imgA.shape[0]
widthA = imgA.shape[1]

heightB = imgB.shape[0]
widthB = imgB.shape[1]


print('Image A :')
print(' Height       : ',heightA)
print(' Width        : ',widthA)
print(' -------------------------------- ')
print('Image B :')
print(' Height       : ',heightB)
print(' Width        : ',widthB)
