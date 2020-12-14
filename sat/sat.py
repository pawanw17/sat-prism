import cv2 
import numpy as np
from math import floor
from random import uniform

def sat(image,T,S,R):
	resT = randomTranslate(image,T) 
	resR = randomRotate(resT,R)
	resS = randomScale(resR,S)
	return resS

def randomTranslate(image,T):
	height, width = image.shape[:2] 

	Tx = uniform(-T,T)
	Ty = uniform(-T,T)
	new_height, new_width = height * Ty, width * Tx  

	T = np.float32([[1, 0, new_width], [0, 1, new_height]]) 
  
	res = cv2.warpAffine(image, T, (width, height)) 
	return res

def randomRotate(image,R):
	height, width = image.shape[:2]
	r_Deg = uniform(-R,R)
	M = cv2.getRotationMatrix2D((width / 2, height / 2), r_Deg, 1)
	res = cv2.warpAffine(image, M, (width, height))
	return res

def randomScale(image,S):
	height, width = image.shape[:2] 
	print(height,width)
	ds = uniform(1-S,1+S) #s=0.1, 0.01,0.5 
	h_new = ds * height
	w_new = ds * width
	h_half_orig = int (height/2)
	w_half_orig = int (width/2)
	h_half_new  = int (h_new/2)
	w_half_new  = int (w_new/2)

# if (ds>1):
	res = cv2.resize(image, (int(w_new), int(h_new)))
	if(ds>1):
		res1 = res[h_half_new-h_half_orig:h_half_new+h_half_orig,w_half_new-w_half_orig:w_half_new+w_half_orig]
	else:
		res1 = np.full((height,width,3), (0,0,0), dtype=np.uint8)
		res1[h_half_orig-h_half_new:h_half_new+h_half_orig,w_half_orig-w_half_new:w_half_new+w_half_orig] = res
	
	return res1

if __name__ == '__main__':
	image = cv2.imread('apple.png')
	height, width = image.shape[:2]
	print(height,width)
	T = 0.3
	S = 0.3
	R = 20
	img = sat(image,T,S,R)
	cv2.imshow('original',image)
	cv2.imshow('final', img)
	cv2.imwrite('final3.png',img)

	cv2.waitKey() 