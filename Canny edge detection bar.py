import cv2

def nothing(x):
    pass

img = cv2.imread("C:/Users/siddh/Desktop/Image Processing data/1_Non-actuated_blue.png", 0) #Directory of the image file

cv2.namedWindow('canny')
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'canny', 0, 1, nothing)

cv2.createTrackbar('lower', 'canny', 0, 255, nothing)
cv2.createTrackbar('upper', 'canny', 0, 255, nothing)

while(True):

    lower = cv2.getTrackbarPos('lower', 'canny')
    upper = cv2.getTrackbarPos('upper', 'canny')
    s = cv2.getTrackbarPos(switch, 'canny')

    if s == 0:
        edges = img
    else:
        edges = cv2.Canny(img, lower, upper)

    cv2.imshow('original', img)
    cv2.imshow('canny', edges)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:   
        break

cv2.destroyAllWindows()
