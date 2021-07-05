import pyautogui as au, cv2, numpy as np, statistics as stat, os, time, math
from python_imagesearch.imagesearch import imagesearch as imFind
import keyboard

#Constantly searches for the spacebar image, per Spacebar.png
#When the Spacebar is found, a screenshot is taken, and the method ends.
def findSpace():
    au.PAUSE = 1
    au.FAILSAFE = True

    im = os.path.join('resources','Spacebar.png')
    y_center = 67 # used to center the image 
    x_center = 45 # used to center the image 
    size = 150 #size of the picture. Should require NO additional changes.
    
    while True:
        if keyboard.is_pressed('q'):
            raise KeyboardInterrupt()
        coords = imFind(im)
        status = coords != [-1,-1]
        if(status): #Takes a picture of the screen when the image is found, and ends the program.
            im = au.screenshot(os.path.join('resources','Current.png'),(coords[0] - x_center, coords[1] - y_center, size, size))
            return time.time()

#Finds the median coordinates of the non-black pixels in an image.
def findCoords(imagePath,debug=False):
    im = cv2.imread(imagePath)
    arr = np.array(im)
    indices = np.where(arr != [0])

    y_coords = indices[0]
    x_coords = indices[1]
    
    if len(y_coords) == 0:
        raise Exception("findCoords: No valid coordinates were found.")

    y_med = stat.median_high(y_coords)
    x_med = stat.median_high(x_coords)
    
    
    #Based on the median coordiante's degree, we will either favor the median x or y coordiante.
    #y will be favored if the degree is in (45,135) or (225,315), else x.
    deg = findDeg((x_med,y_med))
    if (deg > 45 and deg < 135) or (deg > 225 and deg < 315):
        #favor y
        valid_indices = np.where(indices[0] == y_med)
        x_med = stat.median_high(indices[1][valid_indices])
    else:
        #favor x        
        valid_indices = np.where(indices[1] == x_med)
        y_med = stat.median_high(indices[0][valid_indices])
        
    #Under the debug folder, an image is created with the selected coordinate being changed to green.
    if(debug):
        print("Median coord for " + imagePath)
        print("(" + str(x_med) + "," + str(y_med) + ")")
        arr[y_med][x_med] = (0,255,0)
        cv2.imwrite(os.path.join('resources','debug',os.path.basename(imagePath)),arr)
    
    return (x_med,y_med)

#Returns the value in degrees with respect to the circle centered at: (75,75)
def findDeg(coords):
    x_center = 75
    y_center = 75

    adj = abs(x_center - coords[0])
    opp = abs(y_center - coords[1])
    
    #Edge case where x is directly at the center
    if adj == 0:
        return 180 #degrees

    radians = math.atan(opp/adj)
    degrees = math.degrees(radians)

    #Determines which section of the unit circle a given value is in.
    #Please note that as y increases, it goes down to the bottom of the image.
    #As x increases, it goes to the right of the image.
    if(coords[0] > x_center):
        if(coords[1] > y_center):
            degrees += 90
        else:
            degrees = 90 - degrees 
    elif(coords[1] > y_center):
        degrees = 270 - degrees
    else:
        degrees = 270 + degrees
    return degrees

if __name__ == '__main__':
    findCoords(os.path.join('resources','red.png'),debug=True)
    findCoords(os.path.join('resources','white.png'),debug=True)