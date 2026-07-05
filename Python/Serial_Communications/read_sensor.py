import serial

ser = serial.Serial('COM3',9600)

print('Processing......')

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if line:
                try:
                    counter, sensor_value = line.split(',')
                    print(f'Counter: {counter} | Sensor: {sensor_value}')
                except ValueError:
                    print(f'Raw: {line}')
except KeyboardInterrupt:
    print("\nStopped by user")
finally:
    ser.close()