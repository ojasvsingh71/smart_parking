import cv2
import mediapipe as mp

# Initialize MediaPipe Hand Detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Define 20 parking spaces (x, y, width, height)
parking_spaces = [
    (50, 50, 100, 100),   # Slot 1
    (200, 50, 100, 100),  # Slot 2
    (350, 50, 100, 100),  # Slot 3
    (500, 50, 100, 100),  # Slot 4
    (650, 50, 100, 100),  # Slot 5

    (50, 200, 100, 100),  # Slot 6
    (200, 200, 100, 100), # Slot 7
    (350, 200, 100, 100), # Slot 8
    (500, 200, 100, 100), # Slot 9
    (650, 200, 100, 100), # Slot 10

    (50, 350, 100, 100),  # Slot 11
    (200, 350, 100, 100), # Slot 12
    (350, 350, 100, 100), # Slot 13
    (500, 350, 100, 100), # Slot 14
    (650, 350, 100, 100), # Slot 15

    (50, 500, 100, 100),  # Slot 16
    (200, 500, 100, 100), # Slot 17
    (350, 500, 100, 100), # Slot 18
    (500, 500, 100, 100), # Slot 19
    (650, 500, 100, 100), # Slot 20
]

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to access camera!")
        break

    # Flip frame horizontally for natural view
    frame = cv2.flip(frame, 1)
    height, width, _ = frame.shape

    # Convert to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # Default status for parking spaces
    parking_status = ["empty" for _ in parking_spaces]

    # Process detected hands
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Wrist landmark index: 0
            wrist_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * width)
            wrist_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * height)

            # Check wrist in parking spaces
            for i, (x, y, w, h) in enumerate(parking_spaces):
                if x <= wrist_x <= x + w and y <= wrist_y <= y + h:
                    parking_status[i] = "occupied"

            # Draw landmarks on the hand
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Draw parking spaces with status
    for i, (x, y, w, h) in enumerate(parking_spaces):
        color = (0, 255, 0) if parking_status[i] == "empty" else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        status_text = "Empty" if parking_status[i] == "empty" else "Occupied"
        cv2.putText(frame, status_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Display the frame
    cv2.imshow("Parking System (Wrist Detection)", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
