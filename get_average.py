#The `get_average(region)` function updates a global `background` variable to maintain a running average of an image region using OpenCV. 
# If `background` is `None`, it initializes it with the current `region`. 
# If `background` is already set, it updates the average using `cv2.accumulateWeighted(region, background, BG_WEIGHT)`, 
# allowing the background model to adapt over time while incorporating new image data.


def get_average(region):
    global background
    if background is None:
        background = region.copy().astype("float")
        return
    cv2.accumulateWeighted(region, background, BG_WEIGHT)