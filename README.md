# Line-Following-Robot-Using-OpenCV-and-Arduino
## Video Link
- [Video Link](https://youtu.be/vleiL5a85_Q)

## Description
- This autonomous robot follows a black line in a high contrast surrounding using OpenCV for image processing.
I have not used any sensors.
Since I have used an Arduino Board, the image processing has to be done on an external machine ( I used a laptop for this )
L298N motor drivers are used to drive the connected motors.

- One Arduino Uno board, L298N motor Driver, A mobile Phone, DroidCam App, Jumper Wires, 12v 100 RPM DC motors x2, Metal Chassis, Castor wheel, 11.1 Volt Li-Po Battery, Laptop to power the Arduino and for image processing

### Connections : 

- #### Arduino Uno to L298N					
  - pin 5 -> enA
  - pin 6 -> in1 
  - pin 7 -> in2
  - pin 8 -> in3
  - pin 9 -> in4
  - pin 10 -> enB
  - GND Pin of Arduino to GND pin of L298N ( for common ground )

- #### L298N to Li-Po Battery Pack
  - Positive terminal -> Vcc (+12 V pin)
  - Negative terminal -> GND (+5 V pin)

- #### USB port of Laptop to the Arduino (to power the Arduino)

