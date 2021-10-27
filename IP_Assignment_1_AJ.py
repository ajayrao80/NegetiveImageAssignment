import cv2

img = cv2.imread("shiva.jpg")
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()

height, width, channels = img.shape

for i in range(height):
    for j in range(width):
        for k in range(channels):
            new_col = 255 - img[i][j][k]
            img[i][j][k] = new_col

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()


