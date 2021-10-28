import cv2

def main():
    casc = cv2.CascadeClassifier("ds.xml")
    
    fr = cv2.imread('test.jpg')
    rec = casc.detectMultiScale(fr, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    
    for x, y, w, h in rec:
        cv2.rectangle(fr, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    cv2.imwrite('out_test.jpg',fr)

if __name__ == '__main__':
    main()
