#The `segment(region)` function segments an object from the current image frame. 
# It computes the absolute difference between the frame and a background model, thresholds this difference to create a binary image, and finds contours in the thresholded image. 
# If no contours are detected, it updates the `hand` object's `isInFrame` property to `False` and returns `None`. If contours are found, it sets `hand.isInFrame` to `True`, identifies the largest contour, and returns both the binary image and the segmented region.


def segment(region):
    global hand
    diff = cv2.absdiff(background.astype(np.uint8), region)
    thresholded_region = cv2.threshold(diff, OBJ_THRESHOLD, 255, cv2.THRESH_BINARY)[1]

    contours, _ = cv2.findContours(thresholded_region.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        if hand is not None:
            hand.isInFrame = False
        return None, None
    else:
        if hand is not None:
            hand.isInFrame = True
        segmented_region = max(contours, key=cv2.contourArea)
        return thresholded_region, segmented_region