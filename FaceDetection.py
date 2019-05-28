import cv2
import math
import numpy as np


originImage=cv2.imread('custom.jpg')
grayScaleImage = cv2.cvtColor(originImage, cv2.COLOR_BGR2GRAY)


template1=cv2.imread('c1.png')
template2=cv2.imread('c2.png')
template3=cv2.imread('c3.png')

template1Gray=cv2.cvtColor(template1,cv2.COLOR_BGR2GRAY)
template2Gray=cv2.cvtColor(template2,cv2.COLOR_BGR2GRAY)
template3Gray=cv2.cvtColor(template3,cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image', originImage)
cv2.imshow('Gray image', grayScaleImage)
cv2.imshow('temp1',template1)
cv2.imshow('temp1 gray',template1Gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


rows, cols = template1Gray.shape
print(rows,cols)

meanArray=[[0 for x in range(cols)] for y in range(rows)]


for i in range(rows):
    for j in range(cols):
        print("temp1",template1Gray[i][j],"temp2",template2Gray[i][j],"temp3",template3Gray[i][j])
        meanArray[i][j]=(int)((template1Gray[i][j]/3+template2Gray[i][j]/3+template3Gray[i][j]/3))
        print("mean",meanArray[i][j])

gen=np.array(meanArray,dtype=np.uint8)
cv2.imshow('mean',gen)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("template.png", gen)

rowsFace, colsFace = template1Gray.shape
rows, cols = grayScaleImage.shape

sumOfTemplate = 0
meanOfTemplate = 0

correlationArray=np.zeros((rows, cols))

for i in range(rowsFace):
    for j in range(colsFace):
        sumOfTemplate+=meanArray[i][j]

meanOfTemplate=sumOfTemplate/(rowsFace*colsFace)

print("rows",rows,"cols",cols,"row Face",rowsFace,"col face",colsFace)

for i in range(0,rows-rowsFace, 5):
    for j in range(0,cols-colsFace, 5):
        print(i,j)
        sumOfOrigin=0
        meanOfOrigin=0
        for k in range(rowsFace):
            for e in range(colsFace):
                sumOfOrigin+=grayScaleImage[i+k][j+e]
        meanOfOrigin=(sumOfOrigin/(rowsFace*colsFace))
        top=0
        left=0
        right=0
        for x in range(rowsFace):
            for y in range(colsFace):
                top += ((meanArray[x][y] - meanOfTemplate) * (grayScaleImage[i + x][y + j] - meanOfOrigin))
                left += ((meanArray[x][y]) - meanOfTemplate) * ((meanArray[x][y]) - meanOfTemplate)
                right += ((grayScaleImage[i + x][y + j]) - meanOfOrigin) * ((grayScaleImage[i + x][y + j]) - meanOfOrigin)
        left = math.sqrt(left)
        right = math.sqrt(right)
        correlationArray[i][j] = top / (left * right)
k=0
t=0
maxIndexX=0
maxIndexY=0



edge=0.5

list=np.zeros((rows, cols))

index=0

for i in correlationArray:
    t=0
    j=0
    while j < cols:
        if abs(i[j])>edge and list[index,j]!=1:
            maxIndexX=k
            maxIndexY=t
            cv2.rectangle(grayScaleImage, (maxIndexY, maxIndexX), (maxIndexY + colsFace, maxIndexX + rowsFace),(0, 76, 0), 1)
            j+=colsFace
            for z in range(0,rowsFace):
                for x in range(0,colsFace):
                    list[z,x]=1
        else:
            j+=1
        t+= 1
    k+=1
    index+=1
cv2.imshow('Final image', grayScaleImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("finalImaged.png", grayScaleImage)
