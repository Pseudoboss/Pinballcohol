import gpiozero as gpio
from time import sleep

class FakeBumper():
    global_cooldown = 1
    def __init__(self, name, power_pin, button_pin, cooldown = global_cooldown):
        self.name = name
        self.power = gpio.LED(power_pin)
        self.button = gpio.Button(button_pin, pull_up = False)
        self.cooldown = cooldown
        self.run()
    def run(self):
        run = True
        while run:
            self.power.on()
            self.button.wait_for_press()
            self.on_press()
            self.button.wait_for_release()
            self.on_release()
            self.power.off()
            sleep(self.cooldown)
            self.on_warmup()
    def on_press(self):
        print('{} pressed!'.format(self.name))
    def on_release(self):
        print('{} released.'.format(self.name))
    def on_warmup(self):
        print('{} warm.'.format(self.name))

FakeBumper('1', 27, 17, 1)
