def get_region(frame):
    # Separating the region of interest from the rest of the frame.
    region = frame[region_top:region_bottom, region_left:region_right]
    # Making it grayscale so we can detect the edges more easily.
    region = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
    # Using a Gaussian blur to prevent frame noise from being labeled as an edge.
    region = cv2.GaussianBlur(region, (5,5), 0)

    return region