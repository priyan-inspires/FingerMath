import cv2
import mediapipe as mp 
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)


tip_ids = [4, 8, 12, 16, 20]
buttons = {"ADD": (20, 20), "SUB": (150, 20), "MUL": (280, 20), "DIV": (410, 20)}
operation = None
result = None
def count_fingers(hand_landmarks, hand_label):
    fingers = []
    # Thumb
    if hand_label == "Right":
        fingers.append(1 if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0] - 1].x else 0)
    else:
        fingers.append(1 if hand_landmarks.landmark[tip_ids[0]].x > hand_landmarks.landmark[tip_ids[0] - 1].x else 0)
    # Other fingers
    for id in range(1, 5):
        fingers.append(1 if hand_landmarks.landmark[tip_ids[id]].y < hand_landmarks.landmark[tip_ids[id] - 2].y else 0)
    return sum(fingers)
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, _ = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    hand_count = 0
    fingers_count = []

    # Draw buttons
    for op, pos in buttons.items():
        color = (255, 255, 255) if operation != op else (0, 0, 255)
        cv2.rectangle(img, pos, (pos[0]+100, pos[1]+50), (50, 50, 50), -1)
        cv2.putText(img, op, (pos[0]+10, pos[1]+35), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    if results.multi_hand_landmarks and results.multi_handedness:
        for idx, (handLms, handType) in enumerate(zip(results.multi_hand_landmarks, results.multi_handedness)):
            label = handType.classification[0].label  # "Right" or "Left"
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
            hand_count += 1
            fingers = count_fingers(handLms, label)
            fingers_count.append(fingers)

            # Get index finger tip position
            x = int(handLms.landmark[8].x * w)
            y = int(handLms.landmark[8].y * h)

            # Show finger count
            cv2.putText(img, str(fingers), (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

            # Check if pointing to operation
            if operation is None:
                for op, pos in buttons.items():
                    if pos[0] < x < pos[0] + 100 and pos[1] < y < pos[1] + 50:
                        operation = op
                        break

    if operation:
        cv2.putText(img, f"Selected: {operation}", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        if hand_count == 2 and len(fingers_count) >= 2:
            a, b = fingers_count[0], fingers_count[1]
            if operation == "ADD":
                result = a + b
            elif operation == "SUB":
                result = abs(a - b)
            elif operation == "MUL":
                result = a * b
            elif operation == "DIV":
                result = "∞" if b == 0 else round(a / b, 2)

            # Display result
            cv2.putText(img, f"{a} {operation} {b} = {result}", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 200, 255), 3)
            cv2.putText(img, "Press R to reset", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (200, 255, 200), 2)
        else:
            cv2.putText(img, "Show 2 hands to calculate", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)
    else:
        cv2.putText(img, "Select an Operation", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    cv2.imshow("FingerMath by SHANMUGAPRIYAN J ", img)

    key = cv2.waitKey(1)
    if key == ord('r') or key == ord('R'):
        operation = None
        result = None
    elif key == 27:  # ESC key to exit
        break

cap.release()
cv2.destroyAllWindows()
