import cv2

def rgb2gray(filepath):
    img = cv2.imread(filepath)
    #print(img)
    (row, col) = img.shape[0:2]
    for i in range(row):
        for j in range(col):
            img[i, j] = sum(img[i, j])/3
    cv2.imshow('Gray image', img)
    cv2.imwrite("gray_"+filepath,img)
    return img

fileName = 'House.jpg'
rgb2gray(fileName)
