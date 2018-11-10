import gpiozero as pi
from time import sleep

led = pi.LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

