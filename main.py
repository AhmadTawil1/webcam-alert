import glob
import os
import cv2
import time
from emailing import send_email
from threading import Thread

# Start a video
video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
status_list = []
count = 1

def clean_folder():
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)

while True:
    status = 0
    check, frame = video.read()

    if not check:
        break # Stop if the webcam is not working

    # Convert to grayscale and apply Gaussian Blur
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # Initialize first frame
    if first_frame is None:
        first_frame = gray_frame_gau
        continue

    # Compute absolute difference
    data_frame = cv2.absdiff(first_frame, gray_frame_gau)

    # Apply threshold and dilate
    thresh_frame = cv2.threshold(data_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Show the processed video
    cv2.imshow("Motion Detection", dil_frame)

    # Find contours
    contours, _ = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangle around detected motion
    for contour in contours:
        if cv2.contourArea(contour) < 5500: # Ignore small movements
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)
            count += 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) / 2)
            image_with_object = all_images[index]

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:
        email_thread = Thread(target=send_email, args=(image_with_object, ))
        email_thread.daemon = True
        clean_thread = Thread(target=clean_folder)
        clean_thread.daemon = True

        email_thread.start()


    # Show the original video with detected motion
    cv2.imshow("Live Video", frame)

    # Update the first frame periodically to adjust for lighting changes
    if time.time() % 5 == 0: # Update every 5 seconds
        first_frame = gray_frame_gau

    # Quit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# release resources
video.release()
clean_thread.start()
cv2.destroyAllWindows()
