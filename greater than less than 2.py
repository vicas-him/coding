length1 = input ('enter the length of a rectangle')
length1 = float (length1)
width1 = input ('enter the width of the rectangle')
width1 = float (width1)
length2 = input ('enter the length of the second rectangle')
length2 = float (length2)
width2 = input ('enter the width of the second rectangle')
width2 = float (width2)
area = length1 * width1
area = float (area)
area2 = length2 * width2
area2 = float (area2)
print ('area of rectangle:',area,'units squared')
print ('area of rectangle:',area2,'units squared')

if area > area2:
    print ('your first rectangle has a greater area')
elif area < area2:
    print ('your second rectangle has a greater area')
elif area == area2:
    print ('both rectangles are the same')

