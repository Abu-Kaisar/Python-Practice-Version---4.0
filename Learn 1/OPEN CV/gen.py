import numpy as np
import cv2

def main():
    img1 = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1]
        ])
    
    img1 = img1 * 255.
    dia = cv2.resize(img1, (90, 180), interpolation=cv2.INTER_AREA)
    cv2.imwrite('ug.png', dia)
    print('DONE')

if __name__ == '__main__':
    main()
