import mediapipe as mp 
import cv2
import numpy as np 
from pose_tracking_module import PoseTracker

cap = cv2.VideoCapture("production_id_4921646 (1080p).mp4")

tracker = PoseTracker()
window_width, window_height = 500, 600
count = 0
pos = 'up'

while True:
    success, img = cap.read()

    # Check if the video has reached its end
    if not success:
        # Set the frame position back to the beginning
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    img = tracker.detectPose(img)
    lmList = tracker.trackPose(img, draw=False)
    angle = tracker.findAngle(img, 12, 14, 16, draw=True)

    img_resized = cv2.resize(img, (window_width, window_height))
    if angle <= 50 and pos == "up":
        count += 0.5
        pos = 'down'
    if angle >= 160 and pos == "down":
        count += 0.5
        pos = "up"

    min_angle, max_angle = 45, 170
    ang = np.interp(angle, [min_angle, max_angle], [250, 125])
    per = np.interp(angle, [min_angle, max_angle], [0, 100])
    
    # Adjust the height of the filled rectangle based on the 'ang' value
    filled_rect_height = int(ang)
    
    cv2.rectangle(img_resized, (75, 125), (125, 250), (0, 0, 255), 2)
    cv2.rectangle(img_resized, (75, filled_rect_height), (125, 250), (0, 255, 255), cv2.FILLED)
    cv2.putText(img_resized, str(f'{int(per)}%'), (80, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)


    cv2.putText(img_resized, str(int(count)), (230, 80), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 255), 3)
    cv2.putText(img_resized, "Curls Count:", (20, 80), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2)

    cv2.imshow("image", img_resized)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
