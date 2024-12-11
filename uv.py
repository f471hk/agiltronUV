# Written by Fatih Kocabas for Bio-IRL December 2024,
# Class to control Agiltron 4 head UV. 
# Only UV1 output is controlled and only on off an connection status code is applicable. 
# The print of the code is 0 for statement false, 1 for statement true, ex. "uv turned on: 1" means uv is turned on

import serial
import time

class UVcontroller:
    def __init__(self,port="COM8",baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.serial = None


    def connect(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate, timeout=1,stopbits=1)
            print(f"Connected to {self.port}.")
        except Exception as e:
            print(f"Failed to connect: {e}")
    def disconnect(self):
        if self.serial:
            self.serial.close()
            print("Disconnected.")
    def send_command(self, command):
    
        self.serial.write(command)  # Send the command as bytes
        time.sleep(1)  # Allow time for a response
        response = self.serial.read_all()  # Read all data available
        return response  # Return raw bytes
    
    def uv_port_status(self):
        cmd = bytes([0xA5, 0xC4, 0x00, 0x69])
        response = self.send_command(command=cmd).hex()
        self.isUV = response[-1]
        print("is uv on?:" + str(self.isUV))
        return self.isUV
        
    def uv_on(self):
        cmd = bytes([0xA5, 0xC0,0x01,0x66])
        response = self.send_command(command=cmd).hex()
        self.isUV = 1
        print("uv turned on: "+str(response[-1]))
        return self.isUV
    
    def uv_off(self):
        cmd = bytes([0xA5, 0xC1,0x01,0x67])
        response = self.send_command(command=cmd).hex() 
        self.isUV = 0
        print("uv turned off: "+ str(response[-1]))
        


# myUV = UVcontroller(port="COM8")
# myUV.connect()
# myUV.uv_port_status()
# myUV.uv_on()
# time.sleep(10)
# myUV.uv_off()
# myUV.disconnect()