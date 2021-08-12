import serial
import time
ser = serial.Serial('/dev/ttyUSB2', 9600)  
time.sleep(2)
ser.reset_input_buffer()

while True:
    try:
        #ser_bytes = ser.readline()
        #decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        #print(decoded_bytes)

        text = input("Write on\off: ")
        if text == "on":
            ser.write(b'H')
        if text == "off":
            ser.write(b'L')

    except:
        print("Keyboard Interrupt")
        break
