import machine
import utime
motor = machine.Pin(10,machine.Pin.IN)
while True:
        print("sleeping")
        utime.sleep(5)
    