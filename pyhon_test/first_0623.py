Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> cv2.namedWindow("image")

>>> img =cv2.imread('D:\\src.bmp')
>>> cv2.imshow("image",img)
>>> cv2.waitKey(0)

>>> cv2.destroyAllWindows()
>>> 
