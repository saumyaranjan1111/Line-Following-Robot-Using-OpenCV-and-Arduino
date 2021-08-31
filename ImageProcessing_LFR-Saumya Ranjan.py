import cv2    #importing the opencv module of python to access the image related functions (for the image processing part of the project)
import numpy as np      #importing the numpy module , gives access to mathematical functions and matrices etc. 
import serial           #for the serial port communication  
import time             #gives access to time related functions


arduino = serial.Serial('COM4', 115200, timeout=0.1) #here i specified that my arduino was connected in the COM4 port, and set up the communication with it at the baud rate of 115200 bits per second
arduino.close()                                      
arduino.open()

cap = cv2.VideoCapture('http://192.168.29.61:4747/video')       #capturing the video from the droidcam and storing it in cap variable


while True:
    error =0
    ret, frame = cap.read()             #this condition remains true as long as the read function is receiving frames from the source video
                                        #as soon as it stops receiving frames(at the end of the source video), this condition will turn false
                                        #and the loop exits
    
    print(frame.shape[:2])              #used this to output my native resolution of the image received by the phone camera = (480, 640)

    low_b = np.uint8([51,51,51])
    high_b = np.uint8([0,0,0])

    mask = cv2.inRange(frame, high_b, low_b)

    # used masking as a method to preprocess the image 

    contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE) # then I used the contours method to introduce the contours in the masked image
    
    if len(contours) > 0 :                                      # when there are more than two areas or two areas with black regions only consider the biggest area for the calculations
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] !=0 :                                       #calculating the center of the countours using the moments method
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            print("CX : "+str(cx)+"  CY : "+str(cy))                
            if cy >= 290 :                                          # my output from the droidcam was rotated by 90 degrees and I kept the camera in portrait mode so instead of
                                                                    # checking for the cx values we check for the cy values
                                                                    # a hypothetical central lane was imagined to be present, if the circle detects that the centre of the contour
                                                                    # is outside this hypothetical central lane it will alert the bot for corrections in its path  (done through the error variable, and prints the correction required)    
                print("Turn Left")                                  
                error = 290-cy

            if cy < 290 and cy > 190 :
                print("On Track!")
                error =0

            if cy <=190 :
                print("Turn Right")
                error = 190-cy

            cv2.circle(frame, (cx,cy), 5, (255,255,255), -1)            #for the better view of the center of the contour we represent it by a circle to keep track of what the camera is viewing.
    else :
        print("I don't see the line")                                   #when there is no black part in the image
        
    cv2.drawContours(frame, c, -1, (0,255,0), 1)                        #this draws the contour outlines in the image
    cv2.imshow("Mask",mask)                                             #display the mask for confirmation
    cv2.imshow("Frame",frame)                                           #display the original frame which is recieved

    arduino.write(bytes(str(error), 'utf-8'))                           #The final step is to write this error on the Serial Port which
                                                                        #would be read by the Arduino and would help in implementing
                                                                        #the PID controller.
    time.sleep(0.005)

    if cv2.waitKey(1) & 0xff == ord('d'):   # 1 is the time in ms
                                            # it tells the loop to wait for the argument inside the waitKey function (in milliseconds)
                                        # and if it detects any keystroke inside that duration it will return true, 
                                        # also the 0xFF==ord('d') returns the ASCII value of key 'd' if it is pressed
                                        # so the break statement is only executed when the 0xFF==ord('d') returns True so the 
                                        # cv.waitKey(1) & 0xFF==ord('d') will also return true and the break statement will be executed
                                        # stopping the loop and the videocapture
        break

cap.release()
cv2.destroyAllWindows()

