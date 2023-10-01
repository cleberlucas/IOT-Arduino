import cv2
import serial
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

arduino = serial.Serial('COM6', 9600)

while True:
    ret, frame = cap.read()
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
            
            thumb = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring = landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            pinky = landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
            
            finger_value = 0
            
            if thumb.y < index.y:
                finger_value = 1
            elif thumb.y < middle.y:
                finger_value = 2
            elif thumb.y < ring.y:
                finger_value = 3
            elif thumb.y < pinky.y:
                finger_value = 4
            
            arduino.write(str(finger_value).encode())

            print(str(finger_value).encode())
    
    cv2.imshow('Camera', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

arduino.close()

cap.release()
cv2.destroyAllWindows()
