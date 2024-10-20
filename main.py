# Our region of interest will be the top right part of the frame.
region_top = 0
region_bottom = int(2 * FRAME_HEIGHT / 3)
region_left = int(FRAME_WIDTH / 2)
region_right = FRAME_WIDTH

frames_elapsed = 0

capture = cv2.VideoCapture(0)

while True:
    # Storing the frame from the video capture.
    ret, frame = capture.read()

    # Checking if the frame was successfully captured.
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Resizing the frame to the window size.
    frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
    
    # Flipping the frame over the vertical axis to work like a mirror.
    frame = cv2.flip(frame, 1)
    
    # Separating the region of interest and prep it for edge detection.
    region = get_region(frame)
    if frames_elapsed < CALIBRATION_TIME:
        get_average(region)
    else:
        region_pair = segment(region)
        if region_pair is not None:
            # If we have the regions segmented successfully, show them in another window for the user.
            (thresholded_region, segmented_region) = region_pair
            cv2.drawContours(region, [segmented_region], -1, (255, 255, 255))
            cv2.imshow("Segmented Image", region)
            
            get_hand_data(thresholded_region, segmented_region)
    
    # Writing the action the hand is doing on the screen, and draw the region of interest.
    write_on_image(frame)
    
    # Showwing the previously captured frame.
    cv2.imshow("Camera Input", frame)
    
    frames_elapsed += 1
    
    # Checking if user wants to exit.
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# When we exit the loop, we have to stop the capture too.
capture.release()
cv2.destroyAllWindows()