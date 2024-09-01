
import cv2
import os
from ultralytics import YOLO
import numpy as np
import pygame
import telepot  # Import telepot for Telegram integration

os.chdir(r"F:\YOLO Projects\UnallowedArea")

model = YOLO("yolov8n.pt")

Classes = model.model.names

TargetLabel = ["person"]

pygame.init()
pygame.mixer.music.load("alarm.wav")

pts = []

# Set up the Telegram bot
bot = telepot.Bot('7002104360:AAGeYvrWkEF6dl12F7w3OMytVBOWVvmxufw')
chat_id = '1327251536'  # Replace with your actual chat ID

def draw_polygon(event, x, y, flags, param):
    global pts
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        pts.append([x, y])
    elif event == cv2.EVENT_RBUTTONDOWN:
        pts = []

def send_photo_to_telegram(image_path):
    bot.sendPhoto(chat_id, open(image_path, 'rb'))

cap = cv2.VideoCapture("thief_video.mp4")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Number of frames have been finished")
        break
    else:
        frame = cv2.resize(frame, (700, 700))
        
        if len(pts) > 0:
            cv2.polylines(frame, [np.array(pts, np.int32)], True, [0, 0, 255], 2)
        
        results = model.predict(frame)
        
        for result in results:
            boxes = result.boxes.xyxy
            labels = result.boxes.cls
            confs = result.boxes.conf
            
            for box, label, conf in zip(boxes, labels, confs):
                if Classes[int(label)] in TargetLabel:
                    x, y, w, h = box
                    x, y, w, h = int(x), int(y), int(w), int(h)
                    cx, cy = int((x + w) / 2), int((y + h) / 2)
                    label = int(label)
                    
                    cv2.rectangle(frame, (x, y), (w, h), [0, 255, 0], 2)
                    cv2.circle(frame, (cx, cy), 5, [255, 0, 0], 2)
                    
                    if len(pts) > 0 and cv2.pointPolygonTest(np.array(pts, np.int32), (w, h), False) >= 0:
                        if not pygame.mixer.music.get_busy():
                            pygame.mixer.music.play()
                        cv2.rectangle(frame, (x, y), (w, h), [0, 0, 255], 2)
                        cv2.putText(frame, f"Theif {(conf*100):0.2f}%", (x, y), 
                                    cv2.FONT_HERSHEY_COMPLEX, 0.7, [0, 0, 255], 2)
                        
                        # Save the frame as an image
                        image_path = 'thief_detected.jpg'
                        cv2.imwrite(image_path, frame)
                        
                        # Send the photo to Telegram
                        send_photo_to_telegram(image_path)
        
        cv2.namedWindow('frame')
        cv2.setMouseCallback('frame', draw_polygon)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == 27:
            break
cap.release()
cv2.destroyAllWindows()
