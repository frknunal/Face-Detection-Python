# Face-Detection-Python
Find faces in a image by using template matching

Program reads three images that contains face and average them then it searches big image that contains lots of face and find faces then 
it draws rectangle on faces. Program uses template matching.

originImage=cv2.imread('custom.jpg') // image that contains faces

template1=cv2.imread('c1.png') // template 1
template2=cv2.imread('c2.png') // template 2
template3=cv2.imread('c3.png') // template 3
