import cv2
import math
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    model_complexity=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)


def distance(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)


def is_finger_extended(landmarks, tip_idx, pip_idx, wrist):
    tip, pip = landmarks[tip_idx], landmarks[pip_idx]
    # Distance-from-wrist comparison instead of raw x/y comparison,
    # so it still works when the hand is tilted or rotated.
    return distance(tip, wrist) > distance(pip, wrist)


def is_peace_sign(hand_landmarks):
    landmarks = hand_landmarks.landmark
    wrist = landmarks[0]

    # Thumb is excluded: its closing motion (adduction) barely changes
    # tip-to-wrist distance, so it can't be judged the same way.
    index_up = is_finger_extended(landmarks, 8, 6, wrist)
    middle_up = is_finger_extended(landmarks, 12, 10, wrist)
    ring_down = not is_finger_extended(landmarks, 16, 14, wrist)
    pinky_down = not is_finger_extended(landmarks, 20, 18, wrist)

    return index_up and middle_up and ring_down and pinky_down


while True:

    success, frame = cap.read()

    if not success:
        break

    # Mirror camera
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    blur = False

    if results.multi_hand_landmarks:

        peace_signs = []

        for hand_landmarks in results.multi_hand_landmarks:

            peace_signs.append(is_peace_sign(hand_landmarks))

        if len(peace_signs) == 2 and all(peace_signs):

            blur = True

    else:

        cv2.putText(
            frame,
            "No hand detected",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

    if blur:

        frame = cv2.GaussianBlur(
            frame,
            (51, 51),
            0
        )

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)

    if key & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()