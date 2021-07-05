import cv2, numpy as np, os

#Uses color filter to specify only the pixels within the specific range.
def _filterRed(raw):
    im = np.array(raw)
    for row in im:
        for col in row:
            if(col[0] < 45 or col[0] > 60  or col[1] > 120 or col[1] < 45 or col[2] > 240 or col[2] < 200):
                col[0] = 0
                col[1] = 0
                col[2] = 0
    cv2.imwrite(os.path.join('resources','red.png'),im)

#Uses color filter to specify only the pixels within the specific range.
def _filterWhite(raw):
    im = np.array(raw)
    for row in im:
        for col in row:
            if(col[0] > 195 or col[0] < 180 or col[1] > 190 or col[1] < 180 or col[2] > 190 or col[2] < 180):
                col[0] = 0
                col[1] = 0
                col[2] = 0
    cv2.imwrite(os.path.join('resources','white.png'),im)

#Blacks out area in interior and exterior as edited in outline.png
def filterExtraneous(imPath):
    im = cv2.imread(imPath)
    im = cv2.subtract(im,cv2.imread(os.path.join('resources','ring.png')))
    cv2.imwrite(os.path.join('resources','filtered.png'),im)
    _filterRed(im)
    _filterWhite(im)
    return im

if __name__ == '__main__':
    filterExtraneous(os.path.join('resources','Current.png'))