#Counts the number of fingers in a thresholded image:
#Calculates a line height above the hand.
#Creates a mask and draws a horizontal line.
#Isolates the area of interest using a bitwise AND.
#Finds contours in the line image.
#Counts contours that indicate fingers based on their width.
#Returns the number of detected fingers.

def count_fingers(thresholded_image):
 
    line_height = int(hand.top[1] + (0.2 * (hand.bottom[1] - hand.top[1])))
    
   
    line_mask = np.zeros(thresholded_image.shape[:2], dtype=np.uint8)
    

    cv2.line(line_mask, (0, line_height), (thresholded_image.shape[1], line_height), 255, 1)
    
    line = cv2.bitwise_and(thresholded_image, thresholded_image, mask=line_mask)

    contours, _ = cv2.findContours(line.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    fingers = 0

    for curr in contours:
        width = len(curr)
        if width < 3 * abs(hand.right[0] - hand.left[0]) / 4 and width > 5:
            fingers += 1
    
    return fingers

# Finds the most frequently occurring item in a list:
# Initializes a count dictionary and tracking variables.
# Counts occurrences of each item in reverse order.
# Updates the most frequent item if a higher count is found.
# Returns the most frequent item.
    

def most_frequent(input_list):
    dict_count = {}
    count = 0
    most_freq = 0

    for item in reversed(input_list):
        dict_count[item] = dict_count.get(item, 0) + 1
        if dict_count[item] >= count:
            count, most_freq = dict_count[item], item

    return most_freq