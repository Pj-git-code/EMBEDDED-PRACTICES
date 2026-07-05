import serial

port = serial.Serial('COM3', 9600)

while(port.isOpen()):
    data = int(input("Enter 1 to 'ON' the led and 0 to 'off' the led:"))

    if(data == 1):
        port.write(b'1')
    elif(data == 0):
        port.write(b'0')
    else:
        print('Invalid Input!!!')