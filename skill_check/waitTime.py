from detection import findCoords, findDeg
import time,os

#For a given startTime, the program will determine how much longer the program needs to wait before pressing space. The difference is slept through before ending the method.
def wait(startTime,debug=False):
    r_coords = findCoords(os.path.join('resources','red.png'))
    w_coords = findCoords(os.path.join('resources','white.png'))
    r_deg = findDeg(r_coords)
    w_deg = findDeg(w_coords)

    if(debug):
        print('r_deg:' + str(r_deg))
        print('w_deg:' + str(w_deg))

    cycleTime = 1.15

    if(r_deg > w_deg):
        print("Error: r_deg > w_deg in wait method")
    else:
        degrees = w_deg - r_deg
        percent = degrees / 360
            
        delay = time.time() - startTime
        waitTime = (cycleTime * percent) - delay
        if(waitTime > 0):
            time.sleep(waitTime)
        else:
            print('Negative wait time: ' + str(waitTime))
            
if __name__ == '__main__':
    wait(time.time(),True)