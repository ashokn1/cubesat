import cv2 as cv
import numpy as np

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

def is_water_plastic(image, show_images = False):
    min_percent_all_water = 98.5
    min_percent_water_with_plastic = 90

    f_img = filter_image(image)

    # Show the filtered image
    if show_images:
        n_img = cv.putText(f_img, img_name, (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (127, 127, 0), 2, cv.LINE_AA)
        cv.imshow(img_name + ' filtered', n_img)

    # Total percentage of water pixels
    water_pixels = np.sum(f_img == 255)
    non_water_pixels = np.sum(f_img == 0)
    water_pixel_percent = (100*water_pixels)/(water_pixels + non_water_pixels)

    #print('On ' + img_name + ' Water is ' + str(water_pixel_percent) + '%')
    # print(' img is ' + str(image.shape) + ' (' + str(image.size) + ') and f_img is ' + str(f_img.shape) + ' (' + str(f_img.size) + ')')
    if (water_pixel_percent >= min_percent_all_water):
        print (img_name + ' is all water')
        return False

    if (water_pixel_percent < min_percent_water_with_plastic):
        print (img_name + ' is not enough water, likely land')
        return False
    
    print (img_name + ' appears to be water with plastic in it')
    return True


    return True

#image_list = ['land.jpg']
image_list = ['land.jpg', 'water_plastic1.jpg', 'water_plastic2.jpg', 'water_plastic_at_edge.jpg', 'water.jpg', 'land_water.jpg']

for img_name in image_list:
    image = cv.imread(img_name)
    #cv.imshow(img_name, image)
    is_water_plastic(image)
  
#cv.waitKey(100000)
#cv.destroyAllWindows()
