import cv2
import mediapipe as mp
import pyautogui as pag

pag.PAUSE = 0
finger_tips = [8,12,16,20]
finger_joint = [6, 10, 14, 18]
middle_joint = [7,11,15,19]

thumb_tip = [4]
thumb_joint = [3, 2, 1] 

finger_base =[5,9,13,17]



mp_hands=mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

cv2.namedWindow('Camera Feed')

hands = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence = 0.5, min_tracking_confidence=0.6)

currentletter = None

while True:

    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame)

    if not ret:
        print("Error: Failed to grab frame.")
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, connections=mp_hands.HAND_CONNECTIONS)
            indexdown = hand_landmarks.landmark[finger_tips[0]].y > hand_landmarks.landmark[finger_base[0]].y
            middledown = hand_landmarks.landmark[finger_tips[1]].y > hand_landmarks.landmark[finger_base[1]].y
            ringdown = hand_landmarks.landmark[finger_tips[2]].y > hand_landmarks.landmark[finger_base[2]].y
            pinkydown = hand_landmarks.landmark[finger_tips[3]].y > hand_landmarks.landmark[finger_base[3]].y
            
            if hand_landmarks.landmark[finger_tips[0]].y > hand_landmarks.landmark[finger_base[0]].y and hand_landmarks.landmark[finger_tips[1]].y > hand_landmarks.landmark[finger_base[1]].y and hand_landmarks.landmark[finger_tips[2]].y > hand_landmarks.landmark[finger_base[2]].y and hand_landmarks.landmark[finger_tips[3]].y > hand_landmarks.landmark[finger_base[3]].y:
                print("1")
            else:
                print("0")
        indexdown = hand_landmarks.landmark[finger_tips[0]].y > hand_landmarks.landmark[finger_base[0]].y
        middledown = hand_landmarks.landmark[finger_tips[1]].y > hand_landmarks.landmark[finger_base[1]].y
        ringdown = hand_landmarks.landmark[finger_tips[2]].y > hand_landmarks.landmark[finger_base[2]].y
        pinkydown = hand_landmarks.landmark[finger_tips[3]].y > hand_landmarks.landmark[finger_base[3]].y

        indexright = hand_landmarks.landmark[finger_tips[0]].x > hand_landmarks.landmark[finger_base[0]].x
        middleright = hand_landmarks.landmark[finger_tips[1]].x > hand_landmarks.landmark[finger_base[1]].x
        ringright =hand_landmarks.landmark[finger_tips[2]].x > hand_landmarks.landmark[finger_base[2]].x
        pinkyright =hand_landmarks.landmark[finger_tips[3]].x > hand_landmarks.landmark[finger_base[3]].x

        if not indexdown and not middledown and not ringdown and not pinkydown and hand_landmarks.landmark[thumb_tip[0]].x > hand_landmarks.landmark[finger_base[0]].x:
            currentletter = None
    #a
        if indexdown and middledown and ringdown and pinkydown and hand_landmarks.landmark[thumb_tip[0]].y < hand_landmarks.landmark[thumb_joint[0]].y and hand_landmarks.landmark[thumb_tip[0]].x > hand_landmarks.landmark[middle_joint[0]].x and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x:
            
            #if currentletter != "A":
            #    pag.write("A")
            #currentletter = "A"
            cv2.putText(frame, "A", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
    #b
        if not (indexdown or middledown or ringdown or pinkydown) and hand_landmarks.landmark[thumb_tip[0]].x < hand_landmarks.landmark[finger_base[0]].x and hand_landmarks.landmark[thumb_tip[0]].y > hand_landmarks.landmark[finger_base[0]].y and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x:
            #if currentletter != "B":
            #    pag.write("B")
            #currentletter = "B"
            cv2.putText(frame, "B", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


    # #c 
    #finger_tips = [8,12,16,20]
#finger_joint = [6, 10, 14, 18]
#middle_joint = [7,11,15,19]

#thumb_tip = [4]
#thumb_joint = [3, 2, 1] 

#finger_base =[5,9,13,17]
        if hand_landmarks.landmark[finger_tips[0]].y > hand_landmarks.landmark[middle_joint[0]].y and hand_landmarks.landmark[finger_tips[1]].y > hand_landmarks.landmark[middle_joint[1]].y and hand_landmarks.landmark[finger_tips[2]].y > hand_landmarks.landmark[middle_joint[2]].y and hand_landmarks.landmark[finger_tips[3]].y > hand_landmarks.landmark[middle_joint[3]].y and hand_landmarks.landmark[thumb_tip[0]].y > hand_landmarks.landmark[finger_base[0]].y and hand_landmarks.landmark[thumb_joint[1]].x < hand_landmarks.landmark[thumb_tip[0]].x:
         #   if currentletter != "C":
          #      pag.write("C")
           # currentletter = "C"
            cv2.putText(frame, "C", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    #d  
        if ringdown and middledown and pinkydown and not indexdown and hand_landmarks.landmark[thumb_tip[0]].x < hand_landmarks.landmark[finger_base[0]].x and hand_landmarks.landmark[finger_tips[0]].y<hand_landmarks.landmark[middle_joint[0]].y and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x and hand_landmarks.landmark[thumb_joint[1]].y > hand_landmarks.landmark[thumb_tip[0]].y:
            #if currentletter != "D":
            #    pag.write("D")
            #currentletter = "D"
            cv2.putText(frame, "D", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    #e  
        if ringdown and middledown and pinkydown and indexdown and hand_landmarks.landmark[thumb_tip[0]].x < hand_landmarks.landmark[finger_base[1]].x and hand_landmarks.landmark[thumb_tip[0]].y > hand_landmarks.landmark[finger_tips[2]].y  and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x:
            #if currentletter != "E":
            #    pag.write("E") 
            #currentletter = "E"
            cv2.putText(frame, "E", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    #f
        if not ringdown and not middledown and not pinkydown and indexdown and hand_landmarks.landmark[thumb_tip[0]].x < hand_landmarks.landmark[finger_base[0]].x  and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x:
            #if currentletter != "F":
             #   pag.write("F")
            #currentletter = "F"
            cv2.putText(frame, "F", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    #g
        #cv2.putText(frame, str(pinkyright), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        if pinkyright and ringright and middleright and not indexright and hand_landmarks.landmark[thumb_tip[0]].y > hand_landmarks.landmark[finger_joint[0]].y and hand_landmarks.landmark[thumb_tip[0]].x>hand_landmarks.landmark[finger_joint[0]].y and hand_landmarks.landmark[thumb_tip[0]].x < hand_landmarks.landmark[thumb_joint[1]].x:
            #if currentletter != "G":
            #    pag.write("G")
            #currentletter = "G"
            cv2.putText(frame, "G", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    #h 
        if pinkyright and ringright and not middleright and not indexright and hand_landmarks.landmark[thumb_tip[0]].y > hand_landmarks.landmark[finger_joint[1]].y and hand_landmarks.landmark[thumb_tip[0]].x>hand_landmarks.landmark[finger_joint[0]].y and hand_landmarks.landmark[thumb_tip[0]].x < hand_landmarks.landmark[thumb_joint[1]].x:
            cv2.putText(frame, "H", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    #i 
        if not pinkydown and middledown and ringdown and indexdown and hand_landmarks.landmark[thumb_tip[0]].x < hand_landmarks.landmark[finger_base[0]].x  and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x:
            #if currentletter != "I":
            #    pag.write("I")
            #currentletter = "I"
            cv2.putText(frame, "I", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    #j 
        if ringright and middleright and indexright and not pinkyright and hand_landmarks.landmark[thumb_tip[0]].y<hand_landmarks.landmark[finger_joint[0]].y:
            cv2.putText(frame, "J", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    #
    #k 
        if pinkydown and ringdown and not indexdown and not middledown and hand_landmarks.landmark[finger_base[1]].x < hand_landmarks.landmark[thumb_tip[0]].x < hand_landmarks.landmark[finger_base[0]].x and hand_landmarks.landmark[finger_tips[0]].x > hand_landmarks.landmark[finger_tips[1]].x  and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x:
            #if currentletter != "K":
            #    pag.write("K")
            #currentletter = "K"
            cv2.putText(frame, "K", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    #l
        if pinkydown and ringdown and middledown and not indexdown and hand_landmarks.landmark[thumb_tip[0]].x > hand_landmarks.landmark[finger_base[0]].x  and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x and hand_landmarks.landmark[thumb_tip[0]].x > hand_landmarks.landmark[thumb_joint[1]].x:
            #if currentletter != "L":
            #    pag.write("L")
            #currentletter = "L"
            cv2.putText(frame, "L", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    #m
        if indexdown and middledown and ringdown and pinkydown and hand_landmarks.landmark[thumb_tip[0]].x < hand_landmarks.landmark[middle_joint[2]].x and hand_landmarks.landmark[thumb_tip[0]].y < hand_landmarks.landmark[middle_joint[2]].y  and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x:
            #if currentletter != "M":
            #    pag.write("M")
            #currentletter = "M"
            cv2.putText(frame, "M", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    #n
        if indexdown and middledown and ringdown and pinkydown and hand_landmarks.landmark[thumb_tip[0]].y < hand_landmarks.landmark[finger_joint[2]].y and hand_landmarks.landmark[finger_joint[1]].x > hand_landmarks.landmark[thumb_tip[0]].x > hand_landmarks.landmark[finger_joint[2]].x  and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x:
            #if currentletter != "N":
            #    pag.write("N")
            #currentletter = "N"
            cv2.putText(frame, "N", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


    #o
        thumb_tip_x = hand_landmarks.landmark[thumb_tip[0]].x
        thumb_tip_y = hand_landmarks.landmark[thumb_tip[0]].y
        index_tip_x = hand_landmarks.landmark[finger_tips[0]].x
        index_tip_y = hand_landmarks.landmark[finger_tips[0]].y
        middle_tip_x = hand_landmarks.landmark[finger_tips[1]].x
        middle_tip_y = hand_landmarks.landmark[finger_tips[1]].y
        ring_tip_x = hand_landmarks.landmark[finger_tips[2]].x
        ring_tip_y = hand_landmarks.landmark[finger_tips[2]].y
        pinky_tip_x = hand_landmarks.landmark[finger_tips[3]].x
        pinky_tip_y = hand_landmarks.landmark[finger_tips[3]].y

        if (abs(thumb_tip_x - index_tip_x) < 0.05 and abs(thumb_tip_y - index_tip_y) < 0.05 and
            abs(thumb_tip_x - middle_tip_x) < 0.08 and abs(thumb_tip_y - middle_tip_y) < 0.08 and
            abs(thumb_tip_x - ring_tip_x) < 0.1 and abs(thumb_tip_y - ring_tip_y) < 0.1 and
            abs(thumb_tip_x - pinky_tip_x) < 0.12 and abs(thumb_tip_y - pinky_tip_y) < 0.12):
            cv2.putText(frame, "O", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        

         #   if currentletter != "O":
          #      pag.write("O")
           # currentletter = "O"
            cv2.putText(frame, "O", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#p ESO IY interfere #
        if pinkyright and ringright and not indexright and not middleright and hand_landmarks.landmark[finger_base[1]].y > hand_landmarks.landmark[thumb_tip[0]].y > hand_landmarks.landmark[finger_base[0]].y and hand_landmarks.landmark[finger_tips[0]].y < hand_landmarks.landmark[finger_tips[1]].y  and hand_landmarks.landmark[finger_tips[2]].y < hand_landmarks.landmark[finger_tips[3]].y:
            cv2.putText(frame, "P", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    #r
        if pinkydown and ringdown and not indexdown and hand_landmarks.landmark[finger_tips[0]].x < hand_landmarks.landmark[finger_tips[1]].x and hand_landmarks.landmark[thumb_tip[0]].x < hand_landmarks.landmark[finger_base[1]].x  and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x:
            #if currentletter != "R":
             #   pag.write("R")
            #currentletter = "R"
            cv2.putText(frame, "R", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
   # q
       #if (
       #      not indexright and  middleright and  ringright and pinkyright and
       #       hand_landmarks.landmark[finger_tips[0]].y > hand_landmarks.landmark[finger_base[0]].y and
       #      hand_landmarks.landmark[thumb_tip[0]].y > hand_landmarks.landmark[finger_base[0]].y):
       #          cv2.putText(frame, "Q", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


    #s
        if ringdown and middledown and pinkydown and indexdown  and hand_landmarks.landmark[thumb_tip[0]].x < hand_landmarks.landmark[finger_base[0]].x and hand_landmarks.landmark[thumb_tip[0]].y < hand_landmarks.landmark[middle_joint[2]].y and hand_landmarks.landmark[thumb_tip[0]].y > hand_landmarks.landmark[finger_joint[0]].y and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x:
            #if currentletter != "S":
             #   pag.write("S")
            #currentletter = "S"
            cv2.putText(frame, "S", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    #t
        if pinkydown and ringdown and indexdown and middledown and hand_landmarks.landmark[finger_joint[1]].x < hand_landmarks.landmark[thumb_tip[0]].x < hand_landmarks.landmark[finger_joint[0]].x and hand_landmarks.landmark[thumb_tip[0]].y < hand_landmarks.landmark[finger_joint[0]].y  and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x:
            #if currentletter != "T":
            #    pag.write("T")
            #currentletter = "T"
            cv2.putText(frame, "T", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    #u
        if pinkydown and ringdown and not indexdown and not middledown and hand_landmarks.landmark[finger_base[0]].x>hand_landmarks.landmark[finger_base[1]].x >hand_landmarks.landmark[thumb_tip[0]].x and hand_landmarks.landmark[finger_tips[0]].x > hand_landmarks.landmark[finger_tips[1]].x  and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x:
            #if currentletter != "U":
            #    pag.write("U")
            #currentletter = "U"
            cv2.putText(frame, "U", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        
    
    
                    


    #w 
        if not indexdown and not middledown and not ringdown and pinkydown and hand_landmarks.landmark[thumb_tip[0]].x < hand_landmarks.landmark[finger_base[1]].x and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x:
            #if currentletter != "W":
            #    pag.write("W")
            #currentletter = "W"
            cv2.putText(frame, "W", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    #x
        if pinkydown and ringdown and middledown and not indexdown and hand_landmarks.landmark[thumb_tip[0]].x < hand_landmarks.landmark[finger_base[0]].x and hand_landmarks.landmark[finger_tips[0]].y>hand_landmarks.landmark[middle_joint[0]].y and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x:
            #if currentletter != "X":
            #    pag.write("X")
            #currentletter = "X"
            cv2.putText(frame, "X", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    #y
        if indexdown and middledown and ringdown and not pinkydown and hand_landmarks.landmark[thumb_tip[0]].y < hand_landmarks.landmark[thumb_joint[0]].y and hand_landmarks.landmark[thumb_tip[0]].x > hand_landmarks.landmark[thumb_joint[1]].x and hand_landmarks.landmark[2].x > hand_landmarks.landmark[0].x:
            #if currentletter != "Y":
                #pag.write("Y")
            #currentletter = "Y"
                 cv2.putText(frame, "Y", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    









    cv2.imshow('Camera Feed', frame)


    # Wait for 'q' key to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        break

# Release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()

