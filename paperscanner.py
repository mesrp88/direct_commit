import cv2
import numpy as np

widthImg=480
heightImg=640
cap = cv2.VideoCapture(0)       #0 means default camera
cap.set(10,150)                 #10 for brightness index and 150 means intensity

def pre_processing(img):
    imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur, 200,200)
    kernal= np.ones((5,5))
    imgDialation= cv2.dilate(imgCanny, kernal, iterations=2)
    imgThres= cv2.erode(imgDialation, kernal, iterations=1)
    return imgThres

def get_contours(img):
    biggest= np.array([])
    maxArea= 0
    contours, hierarchy= cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area= cv2.contourArea(cnt)
        if area>5000:
            #cv2.drawContours(imgContour, cnt, -1,(255, 0, 0), 3)
            peri=cv2.arcLength(cnt, True)
            approx= cv2.approxPolyDP(cnt, 0.02*peri, True)
            if area>maxArea and len(approx)==4:
                biggest= approx
                maxArea= area
    cv2.drawContours(imgContour,biggest,-1,(255,0,0),20)
    return biggest

def reorder(myPoints):
    myPoints= myPoints.reshape((4,2))
    myPointsNew= np.zeros((4,1,2), np.int32)
    add= myPoints.sum(axis=1)

    myPointsNew[0]=myPoints[np.argmin(add)]
    myPointsNew[3]=myPoints[np.agrmax(add)]
    diff= np.diff(myPoints, axis=1)
    myPointsNew[1]= myPoints[np.argmin(diff)]
    myPointsNew[2]=myPoints[np.argmax(diff)]

    return myPointsNew


def getWrap(img, biggest):
    biggest=reorder(biggest)
    pts1= np.float32(biggest)
    pts2= np.float32([[0,0],[widthImg,0],[0,heightImg], [widthImg, heightImg]])
    matrix=cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput= cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    
    return imgOutput


while True:
    Success, img= cap.read()
    img= cv2.resize(img,(widthImg, heightImg))
    imgContour= img.copy()
    imgThres=pre_processing(img)
    biggest= get_contours(imgThres)
    imgWraped=getWrap(img, biggest)
    cv2.imshow("imageWrap",imgWraped)  #imageWrap in windowname 
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break