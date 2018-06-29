import serial
import time
import datetime

#check
#list serial ports: ls /dev/{tty,cu}.* 
#screen -L /dev/tty.usbXXXXX 9600

ser = serial.Serial('/dev/cu.usbmodem1411', 9600) 
   
while True:
    outputfile = open("temperature_multi.txt","a")  
    output = str(datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")) + " " + str(ser.readline())
    outputfile.write(output)
    outputfile.close()
        
