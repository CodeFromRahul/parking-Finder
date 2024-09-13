# import cv2

#
import cv2
import  pickle



# pickle is used to save all theempy position and bring it to the same code

img = cv2.imread("img.png")

width,height =107,48

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)


    with open('CarParkPos','wb')as f:
        pickle.dump(posList,f)



while True:

    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)
    cv2.imshow("image",img)
    cv2.setMouseCallback("image",mouseClick)
    cv2.waitKey(1)
