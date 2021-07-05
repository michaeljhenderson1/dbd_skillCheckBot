import pyautogui as au, time, os
from detection import findSpace
from filtering import filterExtraneous
from waitTime import wait

au.FAILSAFE = True
time.sleep(5)
print('Press \'q\' to quit.')
try:
    while True:
        startTime = findSpace()
        filterExtraneous(os.path.join('resources','Current.png'))
        wait(startTime,debug=False)
        au.press('space')
        time.sleep(.2)
except KeyboardInterrupt:
    print('\nDone: main.')