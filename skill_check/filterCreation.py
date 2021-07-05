import math, cv2, os, numpy as np

#Adjust these values to adjust the filter being created
###################################
length = 150 #image size. Should NOT be changed.
center = 75 #center of the image. Should NOT be changed.
outer_border = 6 # Determines the size of the outer ring. Typicall forms the non-skill check portion of the image.
inner_border = 2 # Determines the size of the inner ring that's removed. Typically forms the skill check ring.
radius = 65 #Should reach the skill check ring. Should NOT be changed.
###################################

outer_min_dist = radius - outer_border
outer_max_dist = radius + outer_border
inner_min_dist = radius - inner_border
inner_max_dist = radius + inner_border
im = np.zeros((length,length,3), np.uint8)

for x_coord in range(length):
    for y_coord in range(length):
        a = abs(x_coord - center)
        b = abs(y_coord - center)
        c = math.sqrt(math.pow(a,2) + math.pow(b,2))
        #c is the distance from the center to the current pixel
        if( c < outer_min_dist or c > outer_max_dist):
            im[x_coord, y_coord] = (255,255,255)
        if( c > inner_min_dist and c < inner_max_dist):
            im[x_coord, y_coord] = (255,255,255)
cv2.imwrite(os.path.join('resources','debug','ring.png'),im)