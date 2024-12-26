import cv2

def mouseclick(event, x, y, flags, param):
    # This function will handle mouse events. Add logic here if needed.
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Mouse clicked at: ({x}, {y})")

while True:
    # Load and resize the image
    image = cv2.imread('assets/parkingimg.jpg')
    if image is None:
        raise FileNotFoundError("Image file not found at 'assets/parkingimg.jpg'")
    
    image = cv2.resize(image, (1280, 720))
    
    # Draw a rectangle on the image
    cv2.rectangle(image, (85, 160), (215, 225), (255, 0, 255), 2)
    
    # Display the image in a window
    cv2.imshow("image", image)
    
    # Set mouse callback for the same window name
    cv2.setMouseCallback("image", mouseclick)
    
    # Wait for the user to press 'q' to quit
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

# Cleanup
cv2.destroyAllWindows()