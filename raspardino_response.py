import serial
import time

class Raspardino(object):

    def espruino_cmd(self,command):
        ser = serial.Serial(
            port='/dev/ttyACM0',  # or /dev/ttyAMA0 for serial on the Raspberry Pi
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            xonxoff=0, rtscts=0, dsrdtr=0,
        )
        ser.isOpen()
        ser.write(command + "\n")
        endtime = time.time() + 0.2  # wait 0.2 sec
        result = ""
        while time.time() < endtime:
            while ser.inWaiting() > 0:
                result = result + ser.read(1)
        ser.close()
        return result

    def traductor(self,variable):
        if(variable is '0'):
            return False
        else:
            return True