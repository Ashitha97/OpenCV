import cv2
cap=cv2.VideoCapture('vtest.avi') #try putting 0 or 1 for some systems to record your own video and display it
fourcc=cv2.VideoWriter_fourcc(*'XVID')
output=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

print(cap.isOpened())

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # output.write(frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame',gray)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    else:
        break

cap.release()
output.release()
cv2.destroyAllWindows()