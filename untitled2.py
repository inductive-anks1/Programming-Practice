import cv2
import matplotlib.pyplot as plt

def show_image(image):
    cv2.imread(image)
    plt.show()

image = cv2.imread("wallpaperflare-cropped(3).jpg")
show_image(image)