import cv2

def main():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        
        cv2.imshow("frame", frame)
        cv2.imwrite('mer.png', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        

if __name__ == '__main__':
    main()
