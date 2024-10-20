#Counting the number of fingers in a thresholded image
#Calculating a line height above the hand.
#Createing a mask and draws a horizontal line.
#Isolating the area of interest using a bitwise AND.
#Finding contours in the line image.
#Counting contours that indicate fingers based on their width.
#Returning the number of detected fingers.

def count_fingers(thresholded_image):

    line_height = int(hand.top[1] + (0.2 * (hand.bottom[1] - hand.top[1])))
    
  
    line = np.zeros(thresholded_image.shape[:2], dtype=int)
    
  
    cv2.line(line, (thresholded_image.shape[1], line_height), (0, line_height), 255, 1)
    
   
    line = cv2.bitwise_and(thresholded_image, thresholded_image, mask=line.astype(np.uint8))
    

    contours, _ = cv2.findContours(line.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    fingers = 0
    
    for curr in contours:
        width = len(curr)
        
        if width < 3 * abs(hand.right[0] - hand.left[0]) / 4 and width > 5:
            fingers += 1
    
    return fingers

# Finding the most frequently occurring item in a list:
# Initializing a count dictionary and tracking variables.
# Counting occurrences of each item in reverse order.
# Updating the most frequent item if a higher count is found.
# Returning the most frequent item.
    
def most_frequent(input_list):
    dict = {}
    count = 0
    most_freq = 0
    
    for item in reversed(input_list):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count :
            count, most_freq = dict[item], item
    
    return most_freq