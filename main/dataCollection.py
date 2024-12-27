import cv2

positionList = []  # List to store the coordinates of the clicked points
width = 125
height = 55

def mouseclick(event, x, y, flags, params):
    # This function will handle mouse events. Add logic here if needed.
    if event == cv2.EVENT_LBUTTONDOWN:
        positionList.append((x,y))
    if event == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(positionList):
            x1, y1 =pos
            if x1<x<x1+width and y1<y<y1+height:
                positionList.pop(i)


while True:
    # Load and resize the image
    image = cv2.imread('assets/parkingimg.jpg')
    if image is None:
        raise FileNotFoundError("Image file not found at 'assets/parkingimg.jpg'")
    
    image = cv2.resize(image, (1280, 720))
    
    # Draw a rectangle on the image
    for pos in positionList:
        cv2.rectangle(image, pos, (pos[0]+width, pos[1]+height), (255, 0, 255), 2)
    

    cv2.imshow("image", image)
    cv2.setMouseCallback("image", mouseclick)
    # Wait for the user to press 'q' to quit
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

# Cleanup
cv2.destroyAllWindows()