import cv2
import mediapipe as mp
import keyboard
import math
import time           


def main():
    time.sleep(2.0)

    video = cv2.VideoCapture(0)

    last_action = None
    count = 0
    check = 3

    # Take modules drawing_utilities and hands from mediapipe solutions’s
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    mp_drawing_styles = mp.solutions.drawing_styles

    with mp_hands.Hands(max_num_hands=1,
                        min_detection_confidence=0.7,
                        min_tracking_confidence=0.7) as hands:
        # Read a Camera frame
        while video.isOpened():
            ret, image = video.read()
            if not ret:
                print("Ignoring empty camera frame.")
                continue
            
            height, wide, _ = image.shape
            
            image.flags.writeable = False
            # Convert frame from BGR to RGB because Hand object 
            # expects image as a RGB format
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    
                    # Finger landmarks are extracted. Once extraction is complete,
                    # we return to the world of pixel coordinates.
                    index_tip = mp_drawing._normalized_to_pixel_coordinates(
                        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x, 
                        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y, 
                        wide, height)
                    
                    thumb_tip = mp_drawing._normalized_to_pixel_coordinates(
                        hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x, 
                        hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y, 
                        wide, height)
                    
                    middle_tip = mp_drawing._normalized_to_pixel_coordinates(
                        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x, 
                        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y, 
                        wide, height)
                    
                    if index_tip is not None:
                        if count == check:
                            if index_tip is not None and middle_tip is not None:
                                print(math.dist(index_tip, middle_tip))
                                if math.dist(index_tip, middle_tip) < 75:
                                    last_action = "jump"
                                else:
                                    if last_action == "jump":
                                        last_action = None
                            
                            if thumb_tip is not None and index_tip is not None:
                                print(math.dist(index_tip, thumb_tip))
                                if math.dist(thumb_tip, index_tip) < 75:
                                    last_action = "duck"
                                else:
                                    if last_action == "duck":
                                        last_action = None
                            count = 0
                    
                    if count == 0:
                        if last_action == "jump":
                            keyboard.press_and_release("space")
                        elif last_action == "duck":
                            keyboard.press("down")
                        else:
                            keyboard.release("down")
                        print(last_action)

                    count += 1

                    mp_drawing.draw_landmarks(
                        image, hand_landmarks, 
                        mp_hands.HAND_CONNECTIONS, 
                        mp_drawing_styles.get_default_hand_landmarks_style(), 
                        mp_drawing_styles.get_default_hand_connections_style()
                    )
                
            cv2.imshow("Hand Controller", cv2.flip(image, 1))
        
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()