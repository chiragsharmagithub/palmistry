import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread("images/heartLine.png")
img2 = cv.imread("images/headLine.png")
img3 = cv.imread("images/lifeLine.png")

gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
gray3 = cv.cvtColor(img3, cv.COLOR_BGR2GRAY)
ret1, threshold1 = cv.threshold(gray1,160,255,cv.THRESH_BINARY)
ret2, threshold2 = cv.threshold(gray2,160,255,cv.THRESH_BINARY)
ret3, threshold3 = cv.threshold(gray3,160,255,cv.THRESH_BINARY)

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

if(ratio1>80){
	print("Your attitude towards love and quality of love is little complicated & have a deep affection towards your partner.")
}
else{
	print("Your love and marriage life go smoothly & you could have a good personal relationship.")
}

if(ratio2>80){
	print("It indicates you are smart & you have a very clear mind. You are responsive, good at thinking and more considerate than others.")
}
else{
	print("you are usually slow to respond, hasty, careless, indecisive and impulsive. However, your advantage is that you could finish the assigned task in a systematic way.")
}
if(ratio3>80){
	print("You are suited to a life of physical fitness/labor and are good at sports. highly resistant to disease.")
}
else{
	print("You are good at using mind & you are susceptible to illness.")
}