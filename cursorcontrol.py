import cv2
import mediapipe as mp
import pyautogui as pag
pag.FAILSAFE = False
screen_width = pag.size()[1]*2
screen_height = pag.size()[0]
sensitivity = 0.6

finger_tips = [8,12,16,20]
finger_joint = [6, 10, 14, 18]
thumb_tip = [4]
thumb_joint = [3, 2, 1]
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Create a window
cv2.namedWindow('Camera Feed')

hands = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence = 0.5, min_tracking_confidence=0.6)
pag.mouseUp()
mousex = 0
mousey = 0
timer = 0
while True:

    # Read a frame from the camera
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    

    results = hands.process(frame)

    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Show the frame in the window
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            l0x = round(hand_landmarks.landmark[0].x, 2)
            l0y = round(hand_landmarks.landmark[0].y, 2)
            currentmousex = mousex
            currentmousey = mousey
            mousex = int(l0x * screen_width)
            mousey = int(l0y * screen_height - 300)
            if abs(mousex - currentmousex) > 5 or abs(mousey - currentmousey) > 5:
                pag.moveTo(mousex, mousey)
            cv2.putText(frame, f"({mousex}, {mousey})", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            #mp_drawing.draw_landmarks(frame, hand_landmarks, connections=mp_hands.HAND_CONNECTIONS)
            #text = f"({l9x}, {l9y})"
            #cv2.putText(frame, text, (200,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            
            if hand_landmarks.landmark[finger_tips[0]].y > hand_landmarks.landmark[finger_joint[0]].y and hand_landmarks.landmark[finger_tips[1]].y > hand_landmarks.landmark[finger_joint[1]].y and hand_landmarks.landmark[finger_tips[2]].y > hand_landmarks.landmark[finger_joint[2]].y and hand_landmarks.landmark[finger_tips[3]].y > hand_landmarks.landmark[finger_joint[3]].y:
                #cv2.putText(frame, "Closed", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                timer += 1
                if timer > 500:
                    pag.mouseDown()
            else:
                if timer < 500 and timer > 0:
                    pag.click()
                    timer = 0
                else:
                    timer = 0
                    pag.mouseUp()
                #cv2.putText(frame, "Open", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                pag.mouseUp()


    

    cv2.imshow('Camera Feed', frame)


    # Wait for 'q' key to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        break

# Release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()

