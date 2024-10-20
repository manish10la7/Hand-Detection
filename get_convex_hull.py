#The `get_convex_hull(segmented_image)` function calculates the convex hull of the input image and identifies its extreme points: top, bottom, left, and right. 
# It returns these points as tuples of coordinates.

def get_convex_hull(segmented_image):
    convex_hull = cv2.convexHull(segmented_image)
    top = tuple(convex_hull[convex_hull[:, :, 1].argmin()][0])
    bottom = tuple(convex_hull[convex_hull[:, :, 1].argmax()][0])
    left = tuple(convex_hull[convex_hull[:, :, 0].argmin()][0])
    right = tuple(convex_hull[convex_hull[:, :, 0].argmax()][0])
    return top, bottom, left, right
