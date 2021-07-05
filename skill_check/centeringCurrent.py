import pyautogui as au, cv2, numpy as np, os

au.PAUSE = 1
au.FAILSAFE = True

#Editing a red cross to the image to try and improve centering
#These values should NOT be adjusted to resolve centering unless the picture size changes.
#Centering the image captured should be done under detection.py, with the findSpace method ran to capture a new "Current.png".
size = 150 #size of the picture
adj_x = 10 #determines the border (Keeps the cross in the circle)
adj_y = 10 #determines the border (Keeps the cross in the circle)
center = 74 # Center of the image, for size 150x150

def addCross(raw):
    im = np.array(raw)
    i = 0
    for row in im:
        j = 0
        for col in row:
            j += 1
            if((i == center or j == center) and (j > adj_x and j < size - adj_x) and (i > adj_y and i < size - adj_y)):
                col[0] = 0
                col[1] = 0
                col[2] = 255
        i += 1

    cv2.imwrite(os.path.join('resources','debug','cross.png'),im)

#Creates a cross.png from the existing Current.png
if __name__ == '__main__':
    im=os.path.join('resources','Current.png')
    im=cv2.imread(im)
    addCross(im)