import cv2 as cv
import numpy as np

percent_water = 75

def filter_image(frame):
    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    low_H = 90
    high_H = 120
    low_S = 0
    low_V=0
    high_S = 255
    high_V = 255
    frame_threshold = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
    return frame_threshold

def is_water_plastic(image):
    filtered_img = filter_image(image)
    return True

#image_list = ['land.jpg']
image_list = ['land.jpg', 'water_plastic1.jpg', 'water_plastic2.jpg', 'water_plastic_at_edge.jpg', 'water.jpg', 'land_water.jpg']

for img_name in image_list:
    image = cv.imread(img_name)
    #cv.imshow(img_name, image)
    f_img = filter_image(image)
    n_img = cv.putText(f_img, img_name, (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (127, 127, 0), 2, cv.LINE_AA)
    cv.imshow(img_name + ' filtered', n_img)
    water_pixels = np.sum(f_img == 0)
    non_water_pixels = np.sum(f_img == 255)
    print('On ' + img_name + ' Water is ' + str((100*water_pixels)/(water_pixels + non_water_pixels)) + '%')

cv.waitKey(100000)
cv.destroyAllWindows()
