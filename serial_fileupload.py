import serial
import time


f = open('G-code/T.gcode','r')


port = serial.Serial(timeout= 10)
port.baudrate = 9600
port.port = 'COM11'
port.open()
port_data =bytes.decode(port.readall())
print(port_data)

time.sleep(.1)

for l in f:
    g_data = str.encode(l)
    if g_data == None:
        break
    print('sending '+ l)
    port.write(g_data)
    while True:
        port_data = bytes.decode(port.read_until())
        print(port_data)
        if 'ok' in port_data:
            break
    

port.close()
input('press any key to exit.....')
print('##########    job done       #################')



