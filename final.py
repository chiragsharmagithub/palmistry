import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread("images/heartLine.png")
img2 = cv.imread("images/headLine.png")
img3 = cv.imread("images/lifeLine.png")



# b,g,r = cv.split(img)
# img = cv.merge([r,g,b])
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
gray3 = cv.cvtColor(img3, cv.COLOR_BGR2GRAY)
ret1, threshold1 = cv.threshold(gray1,160,255,cv.THRESH_BINARY)
ret2, threshold2 = cv.threshold(gray2,160,255,cv.THRESH_BINARY)
ret3, threshold3 = cv.threshold(gray3,160,255,cv.THRESH_BINARY)


# gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

nonzero1 = cv.countNonZero(threshold1)
total1 = img1.shape[0] * img1.shape[1]
zero1 = total1 - nonzero1
ratio1 = nonzero1 * 100 / float(total1)


nonzero2 = cv.countNonZero(threshold2)
total2 = img2.shape[0] * img2.shape[1]
zero2 = total2 - nonzero2
ratio2 = nonzero2 * 100 / float(total2)


nonzero3 = cv.countNonZero(threshold3)
total3 = img3.shape[0] * img3.shape[1]
zero3 = total3 - nonzero3
ratio3 = nonzero3 * 100 / float(total3)
if(ratio1<50):
    ratio1+=40
if(ratio2<50):
    ratio2+=40
if(ratio3<50):
    ratio3+=40

# print("The number of black pixels are: {}".format(nonzero))
# # print(zero)
# print(total)
# print(zero)
print("Heart line values: {}".format(ratio1))
print("Head line values: {}".format(ratio2))
print("Life Line: {}".format(ratio3))

# age_parameter = 140*ratio/100

# print("The age parameter is {}".format(age_parameter))

#These value are true & are based on ideal conditions means...if you eat healthy + physically fit + mostly panic free


# plt.imshow(gray_image,'gray')
# # plt.imshow(gray)
# plt.xticks(), plt.yticks()
# plt.show()