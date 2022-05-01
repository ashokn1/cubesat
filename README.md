# cubesat



## imgrec v1 @androidkn

threshold = 150

def isWhite(pixel):
    #print(pixel)
    if (pixel[0] > threshold and pixel[1] > threshold and pixel[2] > threshold):
        return True
    return False

def convertImage(image):
    (h, w, c) = image.shape[:3]
    for i in range(h):
        for j in range(w):
            if(isWhite(image[i, j])):
                image[i, j][0] = 0
                image[i, j][1] = 0
                image[i, j][2] = 255

    cv.imshow('pic2', image)
    print('showed image 2')

image = cv.imread(img)
print('Loaded image')
cv.imshow('pic', image)
print('showed image')

convertImage(image)