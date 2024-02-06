import cv2
from cvzone.HandTrackingModule import HandDetector


cap=cv2.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,720)

detector = HandDetector(detectionCon=0.8)

while True:
    try:
        check,cameraFeedImg=cap.read()
        cameraFeedImg_flipped=cv2.flip(cameraFeedImg,1)
        handsDetector=detector.findHands(cameraFeedImg_flipped,flipType=False)
        # print("handsDetector", handsDetector)

        hands=handsDetector[0]
        cameraFeedImg_flipped=handsDetector[1]
        # print(hands)

        if hands:
            hand1=hands[0]
            lmList=hand1['lmList']
            handType1=hand1["type"]

            
            
            # print(handType1)
            #identifying the fingers
            fingers1=detector.fingersUp(hand1)
            # print(fingers1)
            currentFingersUp=''

            if fingers1[0] == 1:
                currentFingersUp="Thumb"
            elif fingers1[1] == 1:
                currentFingersUp="Pointer"
            elif fingers1[2] == 1:
                currentFingersUp="Middle"
            elif fingers1[3] == 1:
                currentFingersUp="Ring"
            elif fingers1[4] == 1:
                currentFingersUp="Pinky"
            else:
                currentFingersUp=""
            cv2.putText(cameraFeedImg_flipped, handType1+":"+currentFingersUp,(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)

            hand2=hands[1]
            lmList2=hand2['lmList']
            handType2=hand2["type"]
            fingers2=detector.fingersUp(hand2)

            currentFingersUp2=""

            if fingers2[0] == 1:
                currentFingersUp2="Thumb"
            elif fingers2[1] == 1:
                currentFingersUp2="Pointer"
            elif fingers2[2] == 1:
                currentFingersUp2="Middle"
            elif fingers2[3] == 1:
                currentFingersUp2="Ring"
            elif fingers2[4] == 1:
                currentFingersUp2="Pinky"
            else:
                currentFingersUp2=""
            cv2.putText(cameraFeedImg_flipped, handType2+":"+currentFingersUp2,(50,100),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)

            
    except Exception as e:
        print(e)

    # cv2.imshow("MyVideo", cameraFeedImg)
    cv2.imshow("MyVideo_flip", cameraFeedImg_flipped)

    if cv2.waitKey(1) == 32:
        break

cap.release()