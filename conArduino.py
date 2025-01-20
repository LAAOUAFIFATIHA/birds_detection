import serial
import time


def conARD():
    # Open the serial port and set the baudrate
    arduino = serial.Serial(port="COM7", baudrate=9600, timeout=1)

    # # Wait for Arduino to initialize
    time.sleep(3)

    # Send a message to the Arduino
    arduino.write(b'Hello Arduino\n')  

    # Read the response from the Arduino
    response = arduino.readline().decode('utf-8').strip()  
    if response :
        return response
    print(f"Arduino says: {response}")

# conARD()



