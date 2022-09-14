from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
import cv2

img = cv2.imread("D:\Photos\img\899777.jpg")
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
invert=cv2.bitwise_not(grey_img)
blur=cv2.GaussianBlur(invert,(21,21),0)
invertedblur=cv2.bitwise_not(blur)
sketch=cv2.divide(grey_img,invertedblur,scale=200.0)
cv2.imwrite("sketch.png",sketch)