import serial
arduino = serial.Serial('/dev/ttyUSB0', 9600)
while True:
	data = arduino.readline().decode('ascii')
	if data:
		data = data.split("\r")
		data = int(data[0])
		
		print(data)
		
		if data < 15:

			arduino.write(b'H')
		else:
			arduino.write(b'L')

