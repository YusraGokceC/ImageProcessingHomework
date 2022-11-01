
import cv2

originalImage = cv2.imread("penguin.jpg")

flipVertical = cv2.flip(originalImage, 0)

cv2.imshow('Original image', originalImage)
cv2.imshow('Flipped vertical image', flipVertical)

cv2.waitKey(0)
cv2.destroyAllWindows()